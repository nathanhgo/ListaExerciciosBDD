package com.example;

import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ClienteDAO dao = new ClienteDAO();
        Scanner sc = new Scanner(System.in);
        int opcao;
        System.setProperty("file.encoding", "UTF-8");

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
                    System.out.print("Nome: ");
                    String nome = sc.nextLine();
                    System.out.print("Endereço: ");
                    String endereco = sc.nextLine();
                    dao.inserir(new Cliente(nome, endereco));
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
                        System.out.print("Novo endereço (" + clienteExistente.getEndereco() + "): ");
                        String novoEndereco = sc.nextLine();

                        clienteExistente.setNome(novoNome.isEmpty() ? clienteExistente.getNome() : novoNome);
                        clienteExistente.setEndereco(novoEndereco.isEmpty() ? clienteExistente.getEndereco() : novoEndereco);
                        
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