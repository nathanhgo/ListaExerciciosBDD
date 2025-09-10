from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, joinedload
from Cliente import Cliente, Base
from Pedido import Pedido

class ClienteDAO:
    def __init__(self, host, user, password, database):
        db_url = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    # === Clientes ===
    def inserir_cliente(self, cliente: Cliente):
        s = self.Session()
        try:
            s.add(cliente); s.commit()
            print(f"Cliente '{cliente.nome}' inserido com ID: {cliente.id}")
            return cliente.id
        except Exception as e:
            s.rollback(); print("Falha ao inserir cliente:", e); return None
        finally:
            s.close()

    def listar_clientes(self):
        s = self.Session()
        try:
            return s.execute(select(Cliente).options(joinedload(Cliente.pedidos))).scalars().all()
        finally:
            s.close()

    def recuperar_por_id_cliente(self, id: int):
        s = self.Session()
        try:
            return s.get(Cliente, id)
        finally:
            s.close()

    def atualizar_cliente(self, cliente: Cliente):
        s = self.Session()
        try:
            s.merge(cliente); s.commit(); print("Cliente atualizado."); return True
        except Exception as e:
            s.rollback(); print("Falha ao atualizar cliente:", e); return False
        finally:
            s.close()

    def remover_cliente(self, id: int):
        s = self.Session()
        try:
            c = s.get(Cliente, id)
            if not c: print("Cliente não encontrado."); return False
            s.delete(c); s.commit(); print("Cliente removido."); return True
        except Exception as e:
            s.rollback(); print("Falha ao remover cliente:", e); return False
        finally:
            s.close()

    # === Pedidos ===
    def inserir_pedido(self, cliente_id: int, pedido: Pedido):
        s = self.Session()
        try:
            c = s.get(Cliente, cliente_id)
            if not c: print("Cliente não encontrado."); return None
            c.pedidos.append(pedido); s.add(c); s.commit()
            print(f"Pedido inserido com ID: {pedido.id}")
            return pedido.id
        except Exception as e:
            s.rollback(); print("Falha ao inserir pedido:", e); return None
        finally:
            s.close()

    def listar_pedidos(self):
        s = self.Session()
        try:
            return s.execute(select(Pedido)).scalars().all()
        finally:
            s.close()

    def recuperar_por_id_pedido(self, id: int):
        s = self.Session()
        try:
            return s.get(Pedido, id)
        finally:
            s.close()

    def atualizar_pedido(self, pedido: Pedido):
        s = self.Session()
        try:
            s.merge(pedido); s.commit(); print("Pedido atualizado."); return True
        except Exception as e:
            s.rollback(); print("Falha ao atualizar pedido:", e); return False
        finally:
            s.close()

    def remover_pedido(self, id: int):
        s = self.Session()
        try:
            p = s.get(Pedido, id)
            if not p: print("Pedido não encontrado."); return False
            s.delete(p); s.commit(); print("Pedido removido."); return True
        except Exception as e:
            s.rollback(); print("Falha ao remover pedido:", e); return False
        finally:
            s.close()
