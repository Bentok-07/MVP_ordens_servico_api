# API - Cadastro de Ordens de Serviço

Esta é uma API desenvolvida em Python com Flask para registrar ordens de serviço e suas respectivas soluções.  
Ela utiliza SQLite como banco de dados, segue o padrão REST e possui documentação automática gerada com Swagger.

---

## Instalação e execução do projeto

### 1. Clone este repositório:
```bash
git clone https://github.com/Bentok-07/ordens_servico_api.git
cd ordens_servico_api
```

### 2. Crie e ative o ambiente virtual:
```bash
# Windows:
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac:
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação:
```bash
python app.py
```

A API será iniciada em:  
 http://localhost:5000/openapi

---

##  Funcionalidades da API

-  Criar nova ordem de serviço (`POST /ordem_servico`)
-  Listar todas as ordens de serviço (`GET /ordens_servico`)
-  Buscar ordem por ID (`GET /ordem_servico`)
-  Deletar ordem de serviço (`DELETE /ordem_servico`)
-  Registrar solução para uma ordem (`POST /solucao`)
-  Editar uma solução existente (`PUT /solucao`)
-  Buscar solução por ordem (`GET /solucao`)
-  Listar todas as soluções (`GET /solucoes`)
-  Interface interativa com Swagger (`GET /openapi`)

---

## Tecnologias utilizadas

- Python 3.11
- Flask + flask-openapi3
- SQLAlchemy (ORM)
- SQLite
- Pydantic (validação de dados)
- Swagger UI (documentação automática)

---

