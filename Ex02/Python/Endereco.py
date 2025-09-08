from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Cliente import Base

class Endereco(Base):
    __tablename__ = 'endereco'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    rua = Column(String(255), nullable=False)
    numero = Column(Integer, nullable=False)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), unique=True)

    cliente = relationship("Cliente", back_populates="endereco")

    def __repr__(self):
        return f"ID: {self.id} | Rua: {self.rua} | Número: {self.numero} | Cliente: {self.cliente_id}"