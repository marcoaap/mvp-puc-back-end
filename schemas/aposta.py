from pydantic import BaseModel
from typing import Optional, List
from model.aposta import Aposta

class ApostaSchema(BaseModel):
    """ Define como uma nova aposta a ser inserido deve ser representado
    """
    #id_aposta: int = 1
    id_jogo: str = "Time1 x Time2" 
    id_player: str = "jogador99"
    placar1: Optional[int] = 0
    placar2: Optional[int] = 0
        

class ApostaBuscaSchema(BaseModel):
    """ Para buscar uma aposta deve ser informado será necessario
        informar o id_jogo>

    """
    id_jogo: str = "Time1 x Time2"
    


class ListagemApostasSchema(BaseModel):
    """ Define como uma listagem de apostas será retornada.
    """
    apostas:List[ApostaSchema]


def apresenta_apostas(apostas: List[Aposta]):
    """ Retorna uma representação da aposta seguindo o schema definido em
        ApostaViewSchema.
    """
    result = []
    for aposta in apostas:
        result.append({

            #"id_aposta": aposta.id_aposta,
            "id_jogo": aposta.id_jogo,
            "id_player": aposta.id_player,
            "placar1": aposta.placar1,
            "placar2": aposta.placar2,
        })

    return {"apostas": result}


class ApostaViewSchema(BaseModel):
    """ Define como uma aposta será retornada: aposta.

    """
    id_aposta: int = 1
    id_jogo: str = "Time1 x Time2" 
    id_player: str = "jogador99"
    placar1: Optional[int] = 0
    placar2: Optional[int] = 0
    
class ApostaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id_jogo: str

def apresenta_aposta(aposta: Aposta):
    """ Retorna uma representação da aposta seguindo o schema definido em
        ApostaViewSchema.
    """
    return {
        "id_aposta": aposta.id_aposta,
        "id_jogo": aposta.id_jogo,
        "id_player": aposta.id_player, 
        "placar1": aposta.placar1,
        "placar2": aposta.placar2
       }


