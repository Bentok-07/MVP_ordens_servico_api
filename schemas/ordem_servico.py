from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class OrdemServicoSchema(BaseModel):
    """ 
    Define os dados necessários para criar uma nova ordem de serviço.

    Campos:
    - numero_equipamento: número identificador do equipamento com defeito.
    - descricao_problema: descrição detalhada do problema apresentado.
    - data_hora_defeito: data e hora em que o defeito foi identificado.
    """
    numero_equipamento: int
    descricao_problema: str
    data_hora_defeito: Optional[datetime] = None


class OrdemServicoBuscaSchema(BaseModel):
    """ 
    Define os dados esperados para buscar uma ordem de serviço.

    Campos:
    - id: identificador único da ordem de serviço.
    """
    id: int


class OrdemServicoViewSchema(BaseModel):
    """ 
    Define como os dados de uma ordem de serviço serão retornados pela API.

    Campos:
    - id: identificador único da ordem.
    - numero_equipamento: número do equipamento.
    - descricao_problema: texto com a descrição do problema.
    - data_hora_defeito: data e hora do registro do defeito.
    """
    id: int
    numero_equipamento: int
    descricao_problema: str
    data_hora_defeito: datetime


class ListagemOrdensSchema(BaseModel):
    """ 
    Define como uma listagem de ordens de serviço será representada.

    Campos:
    - ordens: lista contendo múltiplas ordens de serviço.
    """
    ordens: List[OrdemServicoViewSchema]


def apresenta_ordem(ordem):
    """
    Retorna uma representação da ordem de serviço no formato definido em OrdemServicoViewSchema.
    """
    return {
        "id": ordem.id,
        "numero_equipamento": ordem.numero_equipamento,
        "descricao_problema": ordem.descricao_problema,
        "data_hora_defeito": ordem.data_hora_defeito
    }


def apresenta_ordens(ordens):
    """
    Retorna uma representação da lista de ordens de serviço no formato definido em ListagemOrdensSchema.
    """
    return {
        "ordens": [apresenta_ordem(ordem) for ordem in ordens]
    }
