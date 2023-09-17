# Projeto Back-end - Apostas Online Bolão de Futebol

Esta API é o MVP, Minimum Viable Product (projeto final), do curso de aperfeiçoamento **Desenvolvimento Full Stack Básico** oferecido pela PUC-RIO.

É solicitado que seja apresentado uma aplicação de uma única página (Single Page Application), que implemente pelo menos 3 rotas de acesso, utilizando os métodos GET, DELETE, POST.


# Idéia do projeto

O desenvolvimento dessa API partiu da oportunidade de oferecer uma forma online para realização dos Bolões de final de semana, que são muitos, ainda feitos em papel.

Muitos desafios são enfrentados com o uso do papel:

- Dificuldade na logística para distribuição e coleta das cartelas para marcação do jogos;
- Demora na apuração dos resultados;
- Possibilidade de erro na contabilização da pontuação de cada aposta;
- Custo na confecção das cartelas;
- Impossibilidade de ajuste no resultado enviado.

A API irá facilitar a vida do apostador e da banca que promove o bolão.

Os principais benefícios gerados com o uso da API são:

- Confiabilidade;
- Rapidez na apuração das apostas ganhadoras;
- Proporcionar a expansão na base de apostas já que as apostas serão feitas online;
- Fim dos problemas de logísitica.


# Preparação do ambiente

Após clonar o repositório, é necessário abrir um terminal a partir do diretório raiz e executar os comandos descritos abaixo.

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.


```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.


## Execução 
Para execução da API, é necessário que o Flask esteja ativo. Execute o comando abaixo para iniciar o Flask.

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

## Acessar a API de documentação (Swagger)
Abra um navegador de sua preferência

Acesse a URL [http://localhost:5000/](http://localhost:5000/) 

## Rotas da API

- [POST] `/incluir_aposta`

  Adiciona uma nova aposta à base de dados.

  - **Entrada**: Um objeto JSON com os dados da aposta.
  - **Saída**: Uma representação dos apostas cadastradas.

- [GET] `/lista_apostas`

  Retorna uma listagem de todos as apostas já existentes.

- [DELETE] `/excluir_aposta`

  Deleta a aposta da base de dados, onde o id é a partida = "Time1 x Time2"


## Sobre o Autor

Desenvolvedor: Marco Antonio, Analista de Suporte