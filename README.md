# Projeto Flask CRUD

Este é um projeto simples em Flask para realizar operações CRUD (Create, Read, Update, Delete) em um banco de dados MySQL usando o SQLAlchemy ORM. O projeto permite criar, visualizar, atualizar e excluir registros de pessoas.

## Pré-requisitos

- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/)
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)

## Configuração do Banco de Dados

1. Crie um banco de dados MySQL chamado `projeto`.
2. No arquivo `app.py`, altere a configuração do banco de dados no trecho:

   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:senha@localhost/projeto'

# Instalação das Dependenncias
pip install flask flask-sqlalchemy mysql-connector-python

Para iniciar o aplicativo Flask, execute o seguinte comando no terminal dentro do diretório do projeto:

    python app.py 

O aplicativo será executado em http://localhost:5000/.

Endpoints da API
GET /pessoas: Obtém a lista de todas as pessoas no banco de dados.

GET /pessoas/<id>: Obtém detalhes de uma pessoa específica com base no ID fornecido.

POST /cadastro: Cria um novo registro de pessoa. Envie os dados da pessoa no corpo da solicitação como JSON.

PUT /atualizar/<id>: Atualiza os detalhes de uma pessoa existente com base no ID fornecido. Envie os dados atualizados no corpo da solicitação como JSON.

DELETE /deletar/<id>: Exclui uma pessoa específica com base no ID fornecido.
