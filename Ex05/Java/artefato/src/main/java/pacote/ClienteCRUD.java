package pacote;

import jakarta.persistence.*;
import java.util.List;
import java.util.Scanner;

public class ClienteCRUD {

    private static final EntityManagerFactory emf = Persistence.createEntityManagerFactory("default");
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        while (true) {
            System.out.println("\n=== Menu Clientes ===");
            System.out.println("1. Listar todos os clientes");
            System.out.println("2. Adicionar cliente Físico");
            System.out.println("3. Adicionar cliente Jurídico");
            System.out.println("4. Editar cliente");
            System.out.println("5. Remover cliente");
            System.out.println("0. Sair");
            System.out.print("Escolha: ");

            int opcao = Integer.parseInt(scanner.nextLine());

            switch (opcao) {
                case 1 -> listarClientes();
                case 2 -> adicionarFisico();
                case 3 -> adicionarJuridico();
                case 4 -> editarCliente();
                case 5 -> removerCliente();
                case 0 -> {
                    emf.close();
                    System.out.println("Saindo...");
                    return;
                }
                default -> System.out.println("Opção inválida!");
            }
        }
    }

    private static void listarClientes() {
        EntityManager em = emf.createEntityManager();
        List<Cliente> clientes = em.createQuery("FROM Cliente", Cliente.class).getResultList();

        System.out.println("\n--- Clientes ---");
        for (Cliente c : clientes) {
            System.out.print("ID: " + c.getId() + ", Nome: " + c.getNome() + ", Tipo: ");
            if (c instanceof Fisico f) {
                System.out.println("FÍSICO, CPF: " + f.getCpf());
            } else if (c instanceof Juridico j) {
                System.out.println("JURÍDICO, CNPJ: " + j.getCnpj());
            }
        }
        em.close();
    }

    private static void adicionarFisico() {
        System.out.print("Nome: ");
        String nome = scanner.nextLine();
        System.out.print("CPF: ");
        String cpf = scanner.nextLine();

        EntityManager em = emf.createEntityManager();
        em.getTransaction().begin();

        Fisico f = new Fisico();
        f.setNome(nome);
        f.setCpf(cpf);

        em.persist(f);
        em.getTransaction().commit();
        em.close();

        System.out.println("Cliente Físico adicionado!");
    }

    private static void adicionarJuridico() {
        System.out.print("Nome: ");
        String nome = scanner.nextLine();
        System.out.print("CNPJ: ");
        String cnpj = scanner.nextLine();

        EntityManager em = emf.createEntityManager();
        em.getTransaction().begin();

        Juridico j = new Juridico();
        j.setNome(nome);
        j.setCnpj(cnpj);

        em.persist(j);
        em.getTransaction().commit();
        em.close();

        System.out.println("Cliente Jurídico adicionado!");
    }

    private static void editarCliente() {
        System.out.print("ID do cliente a editar: ");
        Long id = Long.parseLong(scanner.nextLine());

        EntityManager em = emf.createEntityManager();
        Cliente c = em.find(Cliente.class, id);

        if (c == null) {
            System.out.println("Cliente não encontrado!");
            em.close();
            return;
        }

        em.getTransaction().begin();
        System.out.print("Novo nome (enter para manter): ");
        String nome = scanner.nextLine();
        if (!nome.isBlank()) c.setNome(nome);

        if (c instanceof Fisico f) {
            System.out.print("Novo CPF (enter para manter): ");
            String cpf = scanner.nextLine();
            if (!cpf.isBlank()) f.setCpf(cpf);
        } else if (c instanceof Juridico j) {
            System.out.print("Novo CNPJ (enter para manter): ");
            String cnpj = scanner.nextLine();
            if (!cnpj.isBlank()) j.setCnpj(cnpj);
        }

        em.getTransaction().commit();
        em.close();
        System.out.println("Cliente atualizado!");
    }

    private static void removerCliente() {
        System.out.print("ID do cliente a remover: ");
        Long id = Long.parseLong(scanner.nextLine());

        EntityManager em = emf.createEntityManager();
        Cliente c = em.find(Cliente.class, id);

        if (c == null) {
            System.out.println("Cliente não encontrado!");
            em.close();
            return;
        }

        em.getTransaction().begin();
        em.remove(c);
        em.getTransaction().commit();
        em.close();

        System.out.println("Cliente removido!");
    }
}
