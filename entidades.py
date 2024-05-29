from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey;

engine = create_engine("sqlite:///livraria.db", echo=True)

meta = MetaData()

autores = Table('autores', meta,
    Column('id',Integer, primary_key=True, autoincrement=True),
    Column('nome',String,nullable=False),
    Column('anoNascimento',Integer,nullable=False),
    Column('anoFalecimento',Integer,nullable=True),
)

editoras = Table('editoras', meta,
    Column('id',Integer, primary_key=True, autoincrement=True),
    Column('nome',String,nullable=False),
    Column('cepEndereco',Integer,nullable=False),
)

livros = Table('livros', meta,
    Column('id',Integer, primary_key=True, autoincrement=True),
    Column('titulo',String, nullable=False),
    Column('anoPublicacao', Integer, nullable=False),
    Column('editoraId', Integer, ForeignKey('editoras.id'), nullable=False),
    Column('autorId', Integer, ForeignKey('autores.id'), nullable=False),
)

meta.create_all(engine)

conn = engine.connect()

print(engine)