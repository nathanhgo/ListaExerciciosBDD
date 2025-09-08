from Cliente import Cliente
from ClienteDAO import ClienteDAO

def exibir_menu():
    print("\n--- MENU DE GERENCIAMENTO DE CLIENTES ---")
    print("1. Adicionar Novo Cliente")
    print("2. Listar Todos os Clientes")
    print("3. Buscar Cliente por ID")
    print("4. Atualizar Cliente")
    print("5. Remover Cliente")
    print("6. Sair")
    return input("Escolha uma opção: ")

def main(): # IMPORTANTE - Atualizar os dados cadastrais conforme as configs do seu MySql
    dao = ClienteDAO(
        host="localhost",
        user="root",
        password="root",
        database="exercicio1"
    )

    while True:
        opcao = exibir_menu()

        if opcao == '1': # Inserir
            nome = input("Digite o nome do cliente: ")
            endereco = input("Digite o endereço do cliente: ")
            novo_cliente = Cliente(nome=nome, endereco=endereco)
            dao.inserir(novo_cliente)

        elif opcao == '2': # Listar todos
            print("\n--- LISTA DE CLIENTES CADASTRADOS ---")
            clientes = dao.recuperar_todos()
            if clientes:
                for cliente in clientes:
                    print(cliente)
            else:
                print("Nenhum cliente encontrado.")

        elif opcao == '3': # Buscar por ID
            try:
                id_busca = int(input("Digite o ID do cliente a ser buscado: "))
                cliente = dao.recuperar_por_id(id_busca)
                if cliente:
                    print("\n--- CLIENTE ENCONTRADO ---")
                    print(cliente)
                else:
                    print("Cliente não encontrado com o ID fornecido.")
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif opcao == '4': # Atualizar
            try:
                id_atualizar = int(input("Digite o ID do cliente a ser atualizado: "))
                cliente_existente = dao.recuperar_por_id(id_atualizar)
                if cliente_existente:
                    print(f"Dados atuais: {cliente_existente}")
                    novo_nome = input(f"Novo nome (deixe em branco para manter '{cliente_existente.nome}'): ")
                    novo_endereco = input(f"Novo endereço (deixe em branco para manter '{cliente_existente.endereco}'): ")

                    nome_final = novo_nome if novo_nome else cliente_existente.nome
                    endereco_final = novo_endereco if novo_endereco else cliente_existente.endereco
                    
                    cliente_atualizado = Cliente(id=id_atualizar, nome=nome_final, endereco=endereco_final)
                    dao.atualizar(cliente_atualizado)
                else:
                    print("Cliente não encontrado com o ID fornecido.")
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif opcao == '5': # Remover
            try:
                id_remover = int(input("Digite o ID do cliente a ser removido: "))
                dao.remover(id_remover)
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif opcao == '6': # Sair
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()