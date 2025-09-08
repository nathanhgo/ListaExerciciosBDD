from Endereco import Endereco
from Cliente import Cliente
from ClienteDAO import ClienteDAO

def exibir_menu():
    print("\n--- MENU DE GERENCIAMENTO DE CLIENTES ---")
    print("1. Adicionar Novo Cliente e Endereço")
    print("2. Listar Todos os Clientes e Endereços")
    print("3. Buscar Cliente por ID")
    print("4. Buscar Endereço por ID")
    print("5. Atualizar Cliente")
    print("6. Atualizar Endereço")
    print("7. Remover Cliente")
    print("8. Remover Endereço")
    print("9. Sair")
    return input("Escolha uma opção: ")

def main(): # IMPORTANTE - Atualizar os dados cadastrais conforme as configs do seu MySql
    dao = ClienteDAO(
        host="localhost",
        user="root",
        password="root",
        database="exercicio2"
    )

    while True:
        opcao = exibir_menu()

        if opcao == '1': # Inserir
            nome = input("Digite o nome do cliente: ")
            rua = input("Digite a rua do endereço: ")
            numero = int(input("Digite o número do endereço: "))
            novo_cliente = Cliente(nome=nome, endereco=Endereco(rua=rua, numero=numero))
            dao.inserir(novo_cliente)

        elif opcao == '2': # Listar todos
            print("\n--- LISTA DE CLIENTES E ENDEREÇOS CADASTRADOS ---")
            clientes = dao.recuperar_todos()
            if clientes:
                for cliente in clientes:
                    print(cliente)
            else:
                print("Nenhum cliente encontrado.")

        elif opcao == '3': # Buscar por Cliente ID
            try:
                id_busca = int(input("Digite o ID do cliente a ser buscado: "))
                cliente = dao.recuperar_por_id_cliente(id_busca)
                if cliente:
                    print("\n--- CLIENTE ENCONTRADO ---")
                    print(cliente)
                else:
                    print("Cliente não encontrado com o ID fornecido.")
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif opcao == '4': # Buscar por Endereço ID
            try:
                id_busca = int(input("Digite o ID do endereço a ser buscado: "))
                endereco = dao.recuperar_por_id_endereco(id_busca)
                if endereco:
                    print("\n--- ENDEREÇO ENCONTRADO ---")
                    print(endereco)
                else:
                    print("Endereço não encontrado com o ID fornecido.")
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif opcao == '5': # Atualizar Cliente
            try:
                id_atualizar = int(input("Digite o ID do cliente a ser atualizado: "))
                cliente_existente = dao.recuperar_por_id_cliente(id_atualizar)
                if cliente_existente:
                    print(f"Dados atuais: {cliente_existente}")
                    novo_nome = input(f"Novo nome (deixe em branco para manter '{cliente_existente.nome}'): ")

                    nome_final = novo_nome if novo_nome else cliente_existente.nome
                    
                    cliente_atualizado = Cliente(id=id_atualizar, nome=nome_final)
                    dao.atualizar_cliente(cliente_atualizado)
                else:
                    print("Cliente não encontrado com o ID fornecido.")
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif opcao == '6': # Atualizar Endereço
            try:
                id_atualizar = int(input("Digite o ID do endereço a ser atualizado: "))
                endereco_existente = dao.recuperar_por_id_endereco(id_atualizar)
                if endereco_existente:
                    print(f"Dados atuais: {endereco_existente}")
                    nova_rua = input(f"Novo nome (deixe em branco para manter '{endereco_existente.rua}'): ")
                    novo_numero = input(f"Novo endereço (deixe em branco para manter '{endereco_existente.numero}'): ")

                    rua_final = nova_rua if nova_rua else endereco_existente.rua
                    numero_final = novo_numero if novo_numero else endereco_existente.numero
                    
                    endereco_atualizado = Endereco(id=id_atualizar, rua=rua_final, numero=numero_final)
                    dao.atualizar_endereco(endereco_atualizado)
                else:
                    print("Endereço não encontrado com o ID fornecido.")
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif opcao == '7': # Remover Cliente
            try:
                id_remover = int(input("Digite o ID do cliente a ser removido: "))
                dao.remover_cliente(id_remover)
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif opcao == '8': # Remover Endereço
            try:
                id_remover = int(input("Digite o ID do endereço a ser removido: "))
                dao.remover_endereco(id_remover)
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif opcao == '9': # Sair
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()