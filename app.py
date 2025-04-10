from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from sqlalchemy.exc import IntegrityError
from model import Session, OrdemServico, Solucao
from schemas import *
from flask_cors import CORS

info = Info(title="API de Ordens de Serviço", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Tags para agrupar rotas no Swagger
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
ordem_tag = Tag(name="Ordem de Serviço", description="Cadastro e consulta de ordens de serviço")
solucao_tag = Tag(name="Solução", description="Registro de soluções para ordens de serviço")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para a documentação da API"""
    return redirect('/openapi')

@app.post('/ordem_servico', tags=[ordem_tag],
          responses={"200": OrdemServicoViewSchema, "400": ErrorSchema})
def criar_ordem(form: OrdemServicoSchema):
    """Cria uma nova ordem de serviço na base de dados"""
    ordem = OrdemServico(**form.dict())
    try:
        session = Session()
        session.add(ordem)
        session.commit()
        return apresenta_ordem(ordem), 201
    except Exception:
        return {"mensagem": "Erro ao criar ordem de serviço"}, 400

@app.delete('/ordem_servico', tags=[ordem_tag],
            responses={"200": OrdemServicoViewSchema, "404": ErrorSchema})
def deletar_ordem(query: OrdemServicoBuscaSchema):
    """
    Remove uma ordem de serviço pelo ID fornecido.
    """
    session = Session()
    ordem = session.query(OrdemServico).filter_by(id=query.id).first()

    if not ordem:
        return {"mensagem": "Ordem não encontrada"}, 404

    if ordem.solucao:
        session.delete(ordem.solucao)

    session.delete(ordem)
    session.commit()
    return apresenta_ordem(ordem), 200

@app.post('/solucao', tags=[solucao_tag],
          responses={"200": SolucaoViewSchema, "404": ErrorSchema})
def registrar_solucao(form: SolucaoSchema):
    """Registra a solução de uma ordem de serviço"""
    session = Session()
    ordem = session.query(OrdemServico).filter(OrdemServico.id == form.ordem_servico_id).first()

    if not ordem:
        return {"mensagem": "Ordem de serviço não encontrada"}, 404

    solucao = Solucao(descricao=form.descricao, data_hora_fechamento=form.data_hora_fechamento, ordem_servico=ordem)
    session.add(solucao)
    session.commit()
    return apresenta_solucao(solucao), 200

@app.put('/solucao', tags=[solucao_tag],
         responses={"200": SolucaoViewSchema, "404": ErrorSchema})
def atualizar_solucao(form: SolucaoSchema):
    """
    Atualiza a solução já registrada de uma ordem de serviço.
    """
    session = Session()
    ordem = session.query(OrdemServico).filter_by(id=form.ordem_servico_id).first()

    if not ordem or not ordem.solucao:
        return {"mensagem": "Solução não encontrada para esta ordem"}, 404

    ordem.solucao.descricao = form.descricao
    ordem.solucao.data_hora_fechamento = form.data_hora_fechamento
    session.commit()

    return apresenta_solucao(ordem.solucao), 200

@app.get('/ordens_pendentes', tags=[ordem_tag],
         responses={"200": ListagemOrdensSchema})
def listar_pendentes():
    """
    Lista apenas ordens de serviço que ainda não têm solução registrada.
    """
    session = Session()
    ordens = session.query(OrdemServico).filter(OrdemServico.solucao == None).all()
    return apresenta_ordens(ordens), 200

@app.get('/solucoes', tags=[solucao_tag],
         responses={"200": ListagemSolucoesSchema})
def listar_solucoes():
    """
    Lista todas as soluções já registradas no sistema.
    """
    session = Session()
    solucoes = session.query(Solucao).all()

    if not solucoes:
        return {"solucoes": []}, 200

    return {"solucoes": [apresenta_solucao(s) for s in solucoes]}, 200

if __name__ == "__main__":
    app.run(debug=True)
