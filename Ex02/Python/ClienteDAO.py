from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Cliente import Cliente, Base
from Endereco import Endereco

class ClienteDAO:
    def __init__(self, host, user, password, database):
        try:
            # Conexão com o banco de dados via SQLAlchemy
            db_url = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
            self.engine = create_engine(db_url)
            
            # Garante que a tabela 'cliente' existe no banco de dados
            Base.metadata.create_all(self.engine)
            
            # Criação da sessão
            self.Session = sessionmaker(bind=self.engine)
            print("Conexão com o banco de dados estabelecida com sucesso.")
        except Exception as e:
            print(f"Erro ao conectar ou criar tabelas: {e}")
            exit(1)

    def inserir(self, cliente):
        session = self.Session()
        try:
            session.add(cliente)
            session.commit()
            print(f"Cliente '{cliente.nome}' inserido com sucesso com o ID: {cliente.id}")
            return cliente.id
        except Exception as err:
            session.rollback()
            print(f"Falha ao inserir cliente: {err}")
            return None
        finally:
            session.close()

    def recuperar_por_id_cliente(self, id):
        session = self.Session()
        try:
            cliente = session.query(Cliente).get(id)
            return cliente
        except Exception as err:
            print(f"Erro ao buscar cliente: {err}")
            return None
        finally:
            session.close()

    def recuperar_por_id_endereco(self, id):
        session = self.Session()
        try:
            endereco = session.query(Endereco).get(id)
            return endereco
        except Exception as err:
            print(f"Erro ao buscar endereço: {err}")
            return None
        finally:
            session.close()

    def recuperar_todos(self):
        session = self.Session()
        try:
            clientes = session.query(Cliente).all()
            enderecos = session.query(Endereco).all()
            return clientes, enderecos
        except Exception as err:
            print(f"Erro ao listar clientes: {err}")
            return []
        finally:
            session.close()

    def atualizar_cliente(self, cliente_atualizado):
        session = self.Session()
        try:
            cliente_existente = session.query(Cliente).get(cliente_atualizado.id)
            if cliente_existente:
                cliente_existente.nome = cliente_atualizado.nome
                session.commit()
                print(f"Cliente com ID {cliente_atualizado.id} atualizado com sucesso.")
                return True
            else:
                print(f"Nenhum cliente encontrado com o ID {cliente_atualizado.id} para atualizar.")
                return False
        except Exception as err:
            session.rollback()
            print(f"Falha ao atualizar cliente: {err}")
            return False
        finally:
            session.close()
        
    def atualizar_endereco(self, endereco_atualizado):
        session = self.Session()
        try:
            endereco_existente = session.query(Endereco).get(endereco_atualizado.id)
            if endereco_existente:
                endereco_existente.rua = endereco_atualizado.rua
                endereco_existente.numero = endereco_atualizado.numero
                session.commit()
                print(f"Endereço com ID {endereco_atualizado.id} atualizado com sucesso.")
                return True
            else:
                print(f"Nenhum endereço encontrado com o ID {endereco_atualizado.id} para atualizar.")
                return False
        except Exception as err:
            session.rollback()
            print(f"Falha ao atualizar endereço: {err}")
            return False
        finally:
            session.close()

    def remover_cliente(self, id):
        session = self.Session()
        try:
            cliente = session.query(Cliente).get(id)
            if cliente:
                session.delete(cliente)
                session.commit()
                print(f"Cliente com ID {id} removido com sucesso.")
                return True
            else:
                print(f"Nenhum cliente encontrado com o ID {id} para remover.")
                return False
        except Exception as err:
            session.rollback()
            print(f"Falha ao remover cliente: {err}")
            return False
        finally:
            session.close()

    def remover_endereco(self, id):
        session = self.Session()
        try:
            endereco = session.query(Endereco).get(id)
            if endereco:
                session.delete(endereco)
                session.commit()
                print(f"Endereço com ID {id} removido com sucesso.")
                return True
            else:
                print(f"Nenhum endereço encontrado com o ID {id} para remover.")
                return False
        except Exception as err:
            session.rollback()
            print(f"Falha ao remover endereço: {err}")
            return False
        finally:
            session.close()