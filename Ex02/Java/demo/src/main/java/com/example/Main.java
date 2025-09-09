package com.example;

import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ClienteDAO dao = new ClienteDAO();
        Scanner sc = new Scanner(System.in);
        int opcao;

        do {
            System.out.println("\n=== MENU CLIENTES ===");
            System.out.println("1 - Inserir cliente");
            System.out.println("2 - Listar clientes");
            System.out.println("3 - Atualizar cliente");
            System.out.println("4 - Remover cliente");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");
            opcao = sc.nextInt();
            sc.nextLine(); // limpar buffer

            switch (opcao) {
                case 1:
                    System.out.print("Nome do cliente: ");
                    String nome = sc.nextLine();
                    
                    System.out.print("Rua do endereço: ");
                    String rua = sc.nextLine();
                    
                    System.out.print("Número do endereço: ");
                    int numero = sc.nextInt();
                    sc.nextLine(); // limpar buffer

                    // 1. Criar o objeto Endereco
                    Endereco novoEndereco = new Endereco(rua, numero);
                    
                    // 2. Criar o objeto Cliente
                    Cliente novoCliente = new Cliente(nome, novoEndereco);
                    
                    // 3. Estabelecer a relação bidirecional
                    novoEndereco.setCliente(novoCliente);
                    
                    dao.inserir(novoCliente);
                    break;

                case 2:
                    List<Cliente> clientes = dao.listar();
                    System.out.println("\n=== Lista de Clientes ===");
                    for (Cliente c : clientes) {
                        System.out.println(c);
                    }
                    break;

                case 3:
                    System.out.print("Digite o ID do cliente a atualizar: ");
                    int idAtualizar = sc.nextInt();
                    sc.nextLine();
                    
                    Cliente clienteExistente = dao.buscarPorId(idAtualizar);
                    if (clienteExistente != null) {
                        System.out.print("Novo nome (" + clienteExistente.getNome() + "): ");
                        String novoNome = sc.nextLine();
                        
                        // Pegamos o endereço já existente para atualizar
                        Endereco enderecoExistente = clienteExistente.getEndereco();
                        System.out.print("Nova rua (" + enderecoExistente.getRua() + "): ");
                        String novaRua = sc.nextLine();
                        
                        System.out.print("Novo número (" + enderecoExistente.getNumero() + "): ");
                        String novoNumeroStr = sc.nextLine();

                        // Atualiza o nome do cliente se não for vazio
                        if (!novoNome.isEmpty()) {
                            clienteExistente.setNome(novoNome);
                        }
                        
                        // Atualiza o endereço se os campos não forem vazios
                        if (!novaRua.isEmpty()) {
                            enderecoExistente.setRua(novaRua);
                        }
                        if (!novoNumeroStr.isEmpty()) {
                            enderecoExistente.setNumero(Integer.parseInt(novoNumeroStr));
                        }
                        
                        dao.atualizar(clienteExistente);
                    } else {
                        System.out.println("Cliente não encontrado.");
                    }
                    break;

                case 4:
                    System.out.print("Digite o ID do cliente a remover: ");
                    int idRemover = sc.nextInt();
                    sc.nextLine();
                    dao.remover(idRemover);
                    break;

                case 0:
                    System.out.println("Saindo...");
                    break;

                default:
                    System.out.println("Opção inválida!");
            }

        } while (opcao != 0);

        sc.close();
        HibernateUtil.shutdown();
    }
}