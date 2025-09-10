from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import sys

# Base ORM
Base = declarative_base()

class PedidoItem(Base):
    __tablename__ = 'pedido_item'

    pedido_id = Column(Integer, ForeignKey('pedidos.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('itens.id'), primary_key=True)
    quantidade = Column(Integer, nullable=False, default=1)

    pedido = relationship("Pedido", back_populates="pedido_itens")
    item = relationship("Item", back_populates="pedido_itens")

    def __repr__(self):
        return f"PedidoItem(pedido_id={self.pedido_id}, item_id={self.item_id}, quantidade={self.quantidade})"


class Pedido(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(255))

    pedido_itens = relationship("PedidoItem", back_populates="pedido")

    def __repr__(self):
        return f"Pedido(id={self.id}, descricao='{self.descricao}')"


class Item(Base):
    __tablename__ = 'itens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))

    pedido_itens = relationship("PedidoItem", back_populates="item")

    def __repr__(self):
        return f"Item(id={self.id}, nome='{self.nome}')"


def menu():
    print("\n===== MENU N:N =====")
    print("1 - Cadastrar Item")
    print("2 - Listar Itens")
    print("3 - Cadastrar Pedido")
    print("4 - Listar Pedidos")
    print("5 - Associar Item a Pedido")
    print("6 - Sair")
    return input("Escolha uma opção: ")


if __name__ == "__main__":
    # Conectar ao MySQL (ajuste usuario, senha, host e banco)
    engine = create_engine("mysql+pymysql://root:aluno123@localhost:3306/exercicio4", echo=True)

    # Criar tabelas
    Base.metadata.create_all(engine)

    # Criar sessão
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        opcao = menu()

        if opcao == "1":
            nome = input("Nome do item: ")
            item = Item(nome=nome)
            session.add(item)
            session.commit()
            print("Item cadastrado com sucesso!")

        elif opcao == "2":
            itens = session.query(Item).all()
            for i in itens:
                print(i)

        elif opcao == "3":
            desc = input("Descrição do pedido: ")
            pedido = Pedido(descricao=desc)
            session.add(pedido)
            session.commit()
            print("Pedido cadastrado com sucesso!")

        elif opcao == "4":
            pedidos = session.query(Pedido).all()
            for p in pedidos:
                print(p)
                for pi in p.pedido_itens:
                    print("   ", pi.item.nome, "Quantidade:", pi.quantidade)

        elif opcao == "5":
            pedido_id = int(input("ID do pedido: "))
            item_id = int(input("ID do item: "))
            quantidade = int(input("Quantidade: "))

            pedido = session.query(Pedido).get(pedido_id)
            item = session.query(Item).get(item_id)

            if pedido and item:
                pi = PedidoItem(pedido=pedido, item=item, quantidade=quantidade)
                session.add(pi)
                session.commit()
                print("Associação criada com sucesso!")
            else:
                print("Pedido ou Item não encontrado!")

        elif opcao == "6":
            print("Saindo...")
            sys.exit(0)

        else:
            print("Opção inválida!")
