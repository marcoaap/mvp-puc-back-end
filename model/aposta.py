from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base


class Aposta(Base):
    __tablename__ = 'aposta'

    id_aposta = Column("pk_id_aposta", Integer, primary_key=True)
    id_jogo = Column(String(15), unique=True)
    id_player = Column(String(15))
    placar1 = Column(Integer)
    placar2 = Column(Integer)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, id_jogo:str, id_player:str, placar1:int, placar2:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Aposta

        Arguments:
            id_jogo: Jogo a ser disputado na rodada
            id_player: Login do Apostador na aplicação
            placar1: Placar do mandante do jogo
            placar2: Placar do visitante do jogo
            data_insercao: Data que aposta foi inserida no banco de dados
        """
        self.id_jogo = id_jogo
        self.id_player = id_player
        self.placar1 = placar1
        self.placar2 = placar2

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao