from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model.base import Base
from model.solucao import Solucao

class OrdemServico(Base):
    __tablename__ = "ordem_servico"

    id = Column("pk_ordem", Integer, primary_key=True)
    numero_equipamento = Column(Integer)
    data_hora_defeito = Column(DateTime, default=datetime.now)
    descricao_problema = Column(String)

    # relacionamento com a tabela Solucao
    solucao = relationship("Solucao", back_populates="ordem_servico", uselist=False)

    def __init__(self, numero_equipamento: int, descricao_problema: str, data_hora_defeito: Union[datetime, None] = None):
             
        """
        Cria uma Ordem de Serviço  

        Arguments:
            numero_equipameto: numero do equipamento.
            data_hora_defeito: data e hora da abertura da ordem de serviço
            descricao: descricao da falha que o equipamento apresentou 
        """  

        self.numero_equipamento = numero_equipamento
        self.data_hora_defeito = data_hora_defeito
        self.descricao_problema = descricao_problema

        if data_hora_defeito:
            self.data_hora_defeito = data_hora_defeito
    
    def adiciona_solucao(self, solucao: Solucao):
        self.solucao.append(solucao)