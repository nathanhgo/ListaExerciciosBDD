from crud import listar_clientes, adicionar_fisico, adicionar_juridico, remover_cliente, editar_cliente

def menu():
    while True:
        print("\n1 - Listar clientes")
        print("2 - Adicionar cliente fisico")
        print("3 - Adicionar cliente juridico")
        print("4 - Remover cliente")
        print("5 - Editar cliente")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            listar_clientes()
        elif opcao == "2":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            adicionar_fisico(nome, cpf)
        elif opcao == "3":
            nome = input("Nome: ")
            cnpj = input("CNPJ: ")
            adicionar_juridico(nome, cnpj)
        elif opcao == "4":
            cid = int(input("ID do cliente: "))
            remover_cliente(cid)
        elif opcao == "5":
            cid = int(input("ID do cliente: "))
            editar_cliente(cid)
        elif opcao == "0":
            break

if __name__ == "__main__":  
    from database import Base, engine
    Base.metadata.create_all(engine)  # cria as tabelas
    menu()
