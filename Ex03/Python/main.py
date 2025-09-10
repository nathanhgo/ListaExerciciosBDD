from Cliente import Cliente
from Pedido import Pedido
from ClienteDAO import ClienteDAO
from decimal import Decimal
from datetime import datetime

def menu():
    print("\n=== MENU CLIENTES/PEDIDOS (Ex3 1:N) ===")
    print("1 - Inserir cliente")
    print("2 - Listar clientes (com pedidos)")
    print("3 - Atualizar cliente")
    print("4 - Remover cliente")
    print("5 - Adicionar pedido a cliente")
    print("6 - Listar pedidos")
    print("7 - Atualizar pedido")
    print("8 - Remover pedido")
    print("0 - Sair")
    return input("Opção: ").strip()

def main():
    dao = ClienteDAO(host="localhost", user="root", password="root", database="exercicio3")

    while True:
        op = menu()
        if op == "1":
            nome = input("Nome do cliente: ")
            dao.inserir_cliente(Cliente(nome=nome))
        elif op == "2":
            for c in dao.listar_clientes() or []:
                print(c)
                for p in c.pedidos:
                    print("  -", p)
        elif op == "3":
            cid = int(input("ID do cliente: "))
            c = dao.recuperar_por_id_cliente(cid)
            if not c: print("Cliente não encontrado."); continue
            c.nome = input("Novo nome: ")
            dao.atualizar_cliente(c)
        elif op == "4":
            cid = int(input("ID do cliente: "))
            dao.remover_cliente(cid)
        elif op == "5":
            cid = int(input("ID do cliente: "))
            total = Decimal(input("Total (ex: 199.90): "))
            dao.inserir_pedido(cid, Pedido(total=total))
        elif op == "6":
            for p in dao.listar_pedidos() or []:
                print(p)
        elif op == "7":
            pid = int(input("ID do pedido: "))
            p = dao.recuperar_por_id_pedido(pid)
            if not p: print("Pedido não encontrado."); continue
            p.total = Decimal(input("Novo total: "))
            dao.atualizar_pedido(p)
        elif op == "8":
            pid = int(input("ID do pedido: "))
            dao.remover_pedido(pid)
        elif op == "0":
            print("Saindo..."); break

if __name__ == "__main__":
    main()
