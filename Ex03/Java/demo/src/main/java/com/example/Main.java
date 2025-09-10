package com.example;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ClienteDAO dao = new ClienteDAO();
        Scanner sc = new Scanner(System.in);
        int opcao;

        do {
            System.out.println("\n=== MENU CLIENTES/PEDIDOS (Ex3 1:N) ===");
            System.out.println("1 - Inserir cliente");
            System.out.println("2 - Listar clientes (com pedidos)");
            System.out.println("3 - Atualizar cliente");
            System.out.println("4 - Remover cliente");
            System.out.println("5 - Adicionar pedido a cliente");
            System.out.println("6 - Listar pedidos");
            System.out.println("7 - Atualizar total de um pedido");
            System.out.println("8 - Remover pedido");
            System.out.println("0 - Sair");
            System.out.print("Opção: ");
            String in = sc.nextLine();
            if (in.isEmpty()) continue;
            opcao = Integer.parseInt(in);

            switch (opcao) {
                case 1 -> {
                    System.out.print("Nome: ");
                    String nome = sc.nextLine();
                    dao.inserir(new Cliente(nome));
                }
                case 2 -> {
                    List<Cliente> clientes = dao.listar();
                    for (Cliente c : clientes) {
                        System.out.println(c);
                        for (Pedido p : c.getPedidos()) {
                            System.out.println("  - " + p);
                        }
                    }
                }
                case 3 -> {
                    System.out.print("ID do cliente: ");
                    int cid = Integer.parseInt(sc.nextLine());
                    Cliente c = dao.buscarPorId(cid);
                    if (c == null) { System.out.println("Cliente não encontrado."); break; }
                    System.out.print("Novo nome: ");
                    c.setNome(sc.nextLine());
                    dao.atualizar(c);
                }
                case 4 -> {
                    System.out.print("ID do cliente: ");
                    int cid = Integer.parseInt(sc.nextLine());
                    dao.remover(cid);
                }
                case 5 -> {
                    System.out.print("ID do cliente: ");
                    int clienteId = Integer.parseInt(sc.nextLine());
                    System.out.print("Total do pedido (ex: 199.90): ");
                    BigDecimal total = new BigDecimal(sc.nextLine());
                    Pedido p = new Pedido(LocalDateTime.now(), total);
                    dao.inserirPedido(clienteId, p);
                }
                case 6 -> {
                    List<Pedido> pedidos = dao.listarPedidos();
                    pedidos.forEach(System.out::println);
                }
                case 7 -> {
                    System.out.print("ID do pedido: ");
                    int pid = Integer.parseInt(sc.nextLine());
                    Pedido p = dao.buscarPedidoPorId(pid);
                    if (p == null) {
                        System.out.println("Pedido não encontrado.");
                    } else {
                        System.out.print("Novo total: ");
                        p.setTotal(new BigDecimal(sc.nextLine()));
                        dao.atualizarPedido(p);
                    }
                }
                case 8 -> {
                    System.out.print("ID do pedido: ");
                    int pid = Integer.parseInt(sc.nextLine());
                    dao.removerPedido(pid);
                }
                case 0 -> System.out.println("Saindo...");
                default -> { }
            }
        } while (opcao != 0);

        sc.close();
        HibernateUtil.shutdown();
    }
}
