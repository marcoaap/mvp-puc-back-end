from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Aposta
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="BolaoFC API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
aposta_tag = Tag(name="Aposta", description="Incluir, visualizar e deletar apostas do Banco de Dados")



@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/incluir_aposta', tags=[aposta_tag],
          responses={"200": ApostaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_aposta(form: ApostaSchema):
    """Adiciona uma nova Aposta à base de dados

    Retorna uma representação das apostas.
    """
    aposta = Aposta(
        id_jogo=form.id_jogo,
        id_player=form.id_player,
        placar1=form.placar1,
        placar2=form.placar2)
    
    try:
        # criando conexão com a base
        session = Session()
        # adicionando aposta
        session.add(aposta)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionada uma aposta do jogo: '{aposta.id_jogo}'")
        logger.warning(f"Adicionada uma aposta do jogo: '{aposta.id_jogo}'")
        return apresenta_aposta(aposta), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Aposta de mesmo id_jogo já salvo na base :/"
        logger.warning(f"Erro ao adicionar aposta '{aposta.id_jogo}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar uma nova aposta :/"
        logger.warning(f"Erro ao adicionar aposta '{aposta.id_jogo}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/lista_apostas', tags=[aposta_tag],
         responses={"200": ListagemApostasSchema, "404": ErrorSchema})
def get_apostas():
    """Faz a busca por todos as apostas cadastradas no Banco de Dados

    Retorna uma representação da listagem de apostas.
    """
    
    logger.debug(f"Coletando apostas ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    apostas = session.query(Aposta).all()
    
    if not apostas:
        # se não há apostas cadastradas
        return {"apostas": []}, 200
    else:
        logger.debug(f"%d apostas encontradas" % len(apostas))
        # retorna a representação de aposta
        #print(apostas)
        return apresenta_apostas(apostas), 200


@app.delete('/excluir_aposta', tags=[aposta_tag],
            responses={"200": ApostaDelSchema, "404": ErrorSchema})
def del_aposta(query: ApostaBuscaSchema):
    """Deleta uma Aposta a partir do id_jogo informado

    Retorna uma mensagem de confirmação da remoção.
    """
    
    aposta_id_jogo = unquote(unquote(query.id_jogo))
    print(aposta_id_jogo)
    logger.debug(f"Deletando dados sobre o jogo #{aposta_id_jogo}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Aposta).filter(Aposta.id_jogo == aposta_id_jogo).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado a aposta #{aposta_id_jogo}")
        return {"mesage": "Aposta removida", "id": aposta_id_jogo}
    else:
        # se a aposta não foi encontrado
        error_msg = "Aposta não encontrada na base :/"
        logger.warning(f"Erro ao deletar aposta #'{aposta_id_jogo}', {error_msg}")
        return {"mesage": error_msg}, 404

#-------------------------------------------------------------------------

