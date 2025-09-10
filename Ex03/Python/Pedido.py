from sqlalchemy import Column, Integer, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from Cliente import Base

class Pedido(Base):
    __tablename__ = 'pedido'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DateTime, nullable=False, default=datetime.utcnow)
    total = Column(Numeric(12, 2), nullable=False)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)

    cliente = relationship("Cliente", back_populates="pedidos")

    def __repr__(self):
        return f"ID: {self.id} | Data: {self.data} | Total: {self.total} | Cliente: {self.cliente_id}"
