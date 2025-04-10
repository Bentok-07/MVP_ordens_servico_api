from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from model.base import Base
from model.solucao import Solucao
from model.ordem_servico import OrdemServico

db_path = "database/"
# Verifica se o diretorio não existe
if not os.path.exists(db_path):
    os.makedirs(db_path)

# url de acesso ao banco 
db_url = 'sqlite:///%s/db.sqlite3' % db_path

engine = create_engine(db_url, echo=False)

Session = sessionmaker(bind=engine)

if not database_exists(engine.url):
    create_database(engine.url) 

Base.metadata.create_all(engine)

