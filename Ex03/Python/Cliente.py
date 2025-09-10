from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)

    pedidos = relationship("Pedido", back_populates="cliente", cascade="all, delete-orphan")

    def __repr__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Pedidos: {len(self.pedidos) if self.pedidos is not None else 0}"
