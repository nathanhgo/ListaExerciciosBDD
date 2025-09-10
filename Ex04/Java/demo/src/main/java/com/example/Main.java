package com.example;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import java.util.List;
import java.util.Scanner;

public class Main {
    private static final SessionFactory sessionFactory =
            new Configuration().configure().buildSessionFactory();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opcao;

        do {
            System.out.println("\n=== MENU N:N ===");
            System.out.println("1 - Criar Item");
            System.out.println("2 - Criar Pedido");
            System.out.println("3 - Listar Pedidos");
            System.out.println("0 - Sair");
            System.out.print("Escolha: ");
            opcao = sc.nextInt();
            sc.nextLine();

            switch (opcao) {
                case 1 -> criarItem(sc);
                case 2 -> criarPedido(sc);
                case 3 -> listarPedidos();
            }
        } while (opcao != 0);

        sessionFactory.close();
        sc.close();
    }

    private static void criarItem(Scanner sc) {
        System.out.print("Nome do item: ");
        String nome = sc.nextLine();
        System.out.print("Preço: ");
        Double preco = sc.nextDouble();
        sc.nextLine();

        Item item = new Item(nome, preco);

        try (Session session = sessionFactory.openSession()) {
            session.beginTransaction();
            session.persist(item);
            session.getTransaction().commit();
            System.out.println("Item salvo com sucesso!");
        }
    }

    private static void criarPedido(Scanner sc) {
        System.out.print("Descrição do pedido: ");
        String desc = sc.nextLine();

        Pedido pedido = new Pedido(desc);

        try (Session session = sessionFactory.openSession()) {
            List<Item> itens = session.createQuery("from Item", Item.class).list();

            if (itens.isEmpty()) {
                System.out.println("Nenhum item disponível. Cadastre itens primeiro.");
                return;
            }

            System.out.println("Itens disponíveis:");
            for (Item i : itens) {
                System.out.println(i.getId() + " - " + i.getNome() + " (R$ " + i.getPreco() + ")");
            }

            System.out.print("Digite os IDs dos itens (separados por vírgula): ");
            String[] ids = sc.nextLine().split(",");

            session.beginTransaction();
            for (String idStr : ids) {
                Long id = Long.parseLong(idStr.trim());
                Item item = session.get(Item.class, id);
                if (item != null) {
                    pedido.addItem(item);
                }
            }
            session.persist(pedido);
            session.getTransaction().commit();

            System.out.println("Pedido criado com sucesso!");
        }
    }

private static void listarPedidos() {
    try (Session session = sessionFactory.openSession()) {
        List<Pedido> pedidos = session.createQuery("from Pedido", Pedido.class).list();

        if (pedidos.isEmpty()) {
            System.out.println("Nenhum pedido encontrado.");
            return;
        }

        System.out.println("\n=== LISTA DE PEDIDOS ===");
        for (Pedido pedido : pedidos) {
            System.out.println("\n-------------------------------");
            System.out.println("Pedido ID: " + pedido.getId());
            System.out.println("Descrição: " + pedido.getDescricao());
            System.out.println("Itens do Pedido:");

            if (pedido.getItens().isEmpty()) {
                System.out.println("   (Nenhum item associado)");
            } else {
                for (Item item : pedido.getItens()) {
                    System.out.printf("   - %s | Preço: R$ %.2f%n", item.getNome(), item.getPreco());
                }
            }
        }
        System.out.println("-------------------------------\n");
    }
}

}
