from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    endereco = Column(String(255), nullable=False)

    def __repr__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Endereço: {self.endereco}"