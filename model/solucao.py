from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model.base import Base

class Solucao(Base):
    __tablename__ = "solucao"
    id = Column("pk_solucao", Integer, primary_key=True)
    descricao = Column(String)
    data_hora_fechamento = Column(DateTime, default=datetime.now)
    
    ordem_servico_id = Column(Integer, ForeignKey("ordem_servico.pk_ordem"), nullable=False)

    ordem_servico = relationship("OrdemServico", back_populates="solucao")

    def __init__(self, descricao: str, ordem_servico, data_hora_fechamento: Union[datetime, None] = None):
        """
        Cria uma solução para uma ordem de serviço

        Arguments:
            descricao: descrição da solução realizada.
            ordem_servico: instância da OrdemServico relacionada.
            data_hora_fechamento: data e hora de fechamento da ordem (opcional).
        """
        self.descricao = descricao
        self.ordem_servico = ordem_servico
        if data_hora_fechamento:
            self.data_hora_fechamento = data_hora_fechamento