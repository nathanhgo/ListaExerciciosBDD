from models import Cliente, Fisico, Juridico
from database import Session

def listar_clientes():
    with Session() as session:
        clientes = session.query(Cliente).all()
        for c in clientes:
            if isinstance(c, Fisico):
                print(f"[Fisico] {c.id} - {c.nome} - CPF: {c.cpf}")
            elif isinstance(c, Juridico):
                print(f"[Juridico] {c.id} - {c.nome} - CNPJ: {c.cnpj}")
            else:
                print(f"[Cliente] {c.id} - {c.nome}")

def adicionar_fisico(nome, cpf):
    with Session() as session:
        f = Fisico(nome=nome, cpf=cpf)
        session.add(f)
        session.commit()

def adicionar_juridico(nome, cnpj):
    with Session() as session:
        j = Juridico(nome=nome, cnpj=cnpj)
        session.add(j)
        session.commit()

def remover_cliente(cliente_id):
    with Session() as session:
        c = session.get(Cliente, cliente_id)
        if c:
            session.delete(c)
            session.commit()
            
def editar_cliente(cliente_id):
    with Session() as session:
        c = session.get(Cliente, cliente_id)
        if c:
            nome = input("Digite o novo nome [enter para manter]: ")
            if nome:
                c.nome = nome
            if isinstance(c, Fisico):
                cpf = input("Digite o novo cpf [enter para manter]: ")
                if cpf:
                    c.cpf = cpf
            if isinstance(c, Juridico):
                cnpj = input("Digite o novo cnpj [enter para manter]: ")
                if cnpj:
                    c.cnpj = cnpj
            
            session.commit()
