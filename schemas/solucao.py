from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from typing import List
from model.solucao import Solucao


class SolucaoSchema(BaseModel):
    """
    Define os dados necessários para registrar uma nova solução para uma ordem de serviço.

    Campos:
    - ordem_servico_id: ID da ordem de serviço a que a solução está vinculada.
    - descricao: descrição detalhada da solução aplicada.
    - data_hora_fechamento: data e hora em que a ordem foi encerrada.
    """
    ordem_servico_id: int
    descricao: str
    data_hora_fechamento: Optional[datetime] = None


class SolucaoViewSchema(BaseModel):
    """
    Define como os dados de uma solução serão exibidos pela API.

    Campos:
    - id: identificador único da solução.
    - descricao: descrição da solução aplicada.
    - data_hora_fechamento: quando a ordem foi finalizada.
    - ordem_servico_id: ID da ordem de serviço vinculada.
    """
    id: int
    descricao: str
    data_hora_fechamento: datetime
    ordem_servico_id: int

class ListagemSolucoesSchema(BaseModel):
    """
    Define como uma listagem de soluções será retornada.
    """
    solucoes: List[SolucaoViewSchema]


def apresenta_solucao(solucao: Solucao):
    """
    Retorna os dados de uma solução com detalhes da ordem de serviço associada.
    """
    return {
        "id": solucao.id,
        "descricao": solucao.descricao,
        "data_hora_fechamento": solucao.data_hora_fechamento,
        "ordem_servico_id": solucao.ordem_servico.id,
        "ordem_servico": {
            "numero_equipamento": solucao.ordem_servico.numero_equipamento,
            "descricao_problema": solucao.ordem_servico.descricao_problema,
            "data_hora_defeito": solucao.ordem_servico.data_hora_defeito 
        }
    }
