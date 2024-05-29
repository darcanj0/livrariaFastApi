##Alunos:
##Gabriel Vinícius Lemes de Carvalho
## Danie Thomas Arcanjo

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livraria.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    dtNascimento = db.Column(db.Date)
    dtFalecimento = db.Column(db.Date)


class Editora(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cepEnderecoSede = db.Column(db.String(10))


class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100))
    anoPublicacao = db.Column(db.Integer)
    editoraId = db.Column(db.Integer, db.ForeignKey('editora.id'))
    autorId = db.Column(db.Integer, db.ForeignKey('autor.id'))

    autor = db.relationship('Autor', backref=db.backref('livros', lazy=True))
    editora = db.relationship('Editora', backref=db.backref('livros', lazy=True))


def create_livro(titulo, ano_publicacao, autor_id, editora_id):
    novo_livro = Livro(titulo=titulo, anoPublicacao=ano_publicacao, autorId=autor_id, editoraId=editora_id)
    db.session.add(novo_livro)
    db.session.commit()
    return novo_livro


def read_livros():
    return Livro.query.all()


def update_livro(livro_id, titulo=None, ano_publicacao=None, autor_id=None, editora_id=None):
    livro = Livro.query.get(livro_id)
    if livro:
        if titulo:
            livro.titulo = titulo
        if ano_publicacao:
            livro.anoPublicacao = ano_publicacao
        if autor_id:
            livro.autorId = autor_id
        if editora_id:
            livro.editoraId = editora_id
        db.session.commit()
    return livro


def delete_livro(livro_id):
    livro = Livro.query.get(livro_id)
    if livro:
        db.session.delete(livro)
        db.session.commit()
    return livro



if __name__ == '__main__':
    with app.app_context():

        create_livro('O Alquimista', 1988, 1, 1)


        livros = read_livros()
        for livro in livros:
            print(f'Título: {livro.titulo}, Ano: {livro.anoPublicacao}')

        update_livro(1, titulo='O Alquimista (Edição Revisada)', ano_publicacao=1993)

        delete_livro(1)
