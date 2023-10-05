from flask import Flask, Response,request, jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:865974@localhost/projeto'

db = SQLAlchemy(app)

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome_completo = db.Column(db.String(30))
    data_nascimento = db.Column(db.String(20))
    endereco = db.Column(db.String(100))
    cpf = db.Column(db.String(11))
    estado_civil = db.Column(db.String(50))

    def to_json(self):
        return {"id":self.id, "nome":self.nome_completo, "data_de_nascimento": self.data_de_nascimento,"endereco": self.endereco, "cpf": self.cpf, "civil":self.estado_civilcivil}

with app.app_context():
    db.create_all()

#Irá selecionar tudo
@app.route('/pessoas', methods=["GET"])
def seleciona_pessoas():
    try:
        pessoas_classe = Pessoa.query.all()
        pessoas_json = [pessoas.to_json() for pessoas in pessoas_classe]
        mensagem = 'Tarefa concluida'
        status = 200

    except Exception as e:
        mensagem = 'Erro ao concluir' + str(e)
        status = 500

    return jsonify({"status": status, "mensagem":mensagem, "pessoas":pessoas_json}), status

#selecionar individual
@app.route('/pessoas/<id>',methods=["GET"])
def seleciona_usuario(id):
    try:
            pessoa_classe = Pessoa.query.filter_by(id=id).first()
            pessoa_json = pessoa_classe.to_json()
            mensagem = 'Tarefa concluida'
            status = 200
    except Exception as e:
            mensagem = 'Erro ao concluir ' + str(e)
            status = 500

    return jsonify({"status": status, "mensagem": mensagem, "pessoa": pessoa_json}), status

#cadastrar
@app.route("/cadastro", methods=["POST"])
def cria_pessoa():
    try:
        body = request.get_json()
        pessoa = Pessoa(nome=body["nome"], data_de_nascimento=body["data_de_nascimento"], endereco=body["endereco"], cpf=body["cpf"],estado_civil=body["civil"])
        db.session.add(pessoa)
        db.session.commit()
        mensagem = 'Pessoa cadastrada'
        status = 201
    except Exception as e:
        mensagem = 'Erro ao cadastrar '
        status = 400
    return jsonify({"mensagem": mensagem}), status

#atualizar
@app.route("/atualizar/<id>", methods=["PUT"])
def atualiza_pessoa(id):
    try:
        pessoa_classe = Pessoa.query.filter_by(id=id).first()


        if pessoa_classe:
            body = request.get_json()
            if 'nome' in body:
                pessoa_classe.nome_completo = body['nome']

            if'data_de_nascimento' in body:
                pessoa_classe.data_de_nascimento = body['data_de_nascimento']
            if'endereco' in body:
                pessoa_classe.endereco = body['endereco']
            if'cpf' in body:
                pessoa_classe.cpf = body['cpf']
            if'civil' in body:
                 pessoa_classe.estado_civil = body['civil']

            db.session.commit()
            mensagem = 'Pessoa atualizada'
            status = 200

        else:
            mensagem = 'Pessoa não localizada'
            status = 404

    except Exception as e:
        mensagem = 'Erro ao atualizar'
        status = 400

    return jsonify({'mensagem': mensagem, 'pessoa': pessoa_classe.to_json()}), status

#deletar
@app.route('/deletar/<id>', methods=["DELETE"])
def deleta_pessoa(id):
    try:
        pessoa_classe = Pessoa.query.filter_by(id=id).first()
        if pessoa_classe:
            db.session.delete(pessoa_classe)
            db.session.commit()
            mensagem = 'Pessoa deletada'
            status = 200
        else:
            mensagem = 'Pessoa não encontrada'
            status = 404

    except Exception as e:
        mensagem = 'Erro ao deletar usuario'
        status = 500

    return jsonify({'mensagem': mensagem}), status
app.run()


