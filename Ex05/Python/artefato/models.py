from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    DTYPE = Column(String)

    __mapper_args__ = {
        'polymorphic_identity':'cliente',
        'polymorphic_on': DTYPE
    }

class Fisico(Cliente):
    __tablename__ = None  # SINGLE_TABLE strategy
    cpf = Column(String)
    __mapper_args__ = {
        'polymorphic_identity':'Fisico',
    }

class Juridico(Cliente):
    __tablename__ = None  # SINGLE_TABLE strategy
    cnpj = Column(String)
    __mapper_args__ = {
        'polymorphic_identity':'Juridico',
    }
