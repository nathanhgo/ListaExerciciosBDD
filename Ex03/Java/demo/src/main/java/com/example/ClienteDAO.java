package com.example;

import org.hibernate.Session;
import org.hibernate.Transaction;
import java.util.List;

public class ClienteDAO {

    // === CLIENTE ===
    public void inserir(Cliente cliente) {
        Transaction tx = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            tx = session.beginTransaction();
            session.persist(cliente);
            tx.commit();
            System.out.println("Cliente inserido com sucesso!");
        } catch (Exception e) {
            if (tx != null) tx.rollback();
            System.out.println("Erro ao inserir cliente: " + e.getMessage());
        }
    }

    public Cliente buscarPorId(int id) {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            return session.get(Cliente.class, id);
        }
    }

    public List<Cliente> listar() {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            return session.createQuery("from Cliente", Cliente.class).list();
        }
    }

    public void atualizar(Cliente cliente) {
        Transaction tx = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            tx = session.beginTransaction();
            session.merge(cliente);
            tx.commit();
            System.out.println("Cliente atualizado com sucesso!");
        } catch (Exception e) {
            if (tx != null) tx.rollback();
            System.out.println("Erro ao atualizar cliente: " + e.getMessage());
        }
    }

    public void remover(int id) {
        Transaction tx = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            tx = session.beginTransaction();
            Cliente c = session.get(Cliente.class, id);
            if (c != null) session.remove(c);
            tx.commit();
            System.out.println("Cliente removido com sucesso!");
        } catch (Exception e) {
            if (tx != null) tx.rollback();
            System.out.println("Erro ao remover cliente: " + e.getMessage());
        }
    }

    // === PEDIDO ===
    public void inserirPedido(int clienteId, Pedido pedido) {
        Transaction tx = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            tx = session.beginTransaction();
            Cliente c = session.get(Cliente.class, clienteId);
            if (c == null) {
                System.out.println("Cliente não encontrado.");
                return;
            }
            c.addPedido(pedido);
            session.merge(c);
            tx.commit();
            System.out.println("Pedido adicionado com sucesso!");
        } catch (Exception e) {
            if (tx != null) tx.rollback();
            System.out.println("Erro ao adicionar pedido: " + e.getMessage());
        }
    }

    public List<Pedido> listarPedidos() {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            return session.createQuery("from Pedido", Pedido.class).list();
        }
    }

    public Pedido buscarPedidoPorId(int id) {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            return session.get(Pedido.class, id);
        }
    }

    public void atualizarPedido(Pedido pedido) {
        Transaction tx = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            tx = session.beginTransaction();
            session.merge(pedido);
            tx.commit();
            System.out.println("Pedido atualizado com sucesso!");
        } catch (Exception e) {
            if (tx != null) tx.rollback();
            System.out.println("Erro ao atualizar pedido: " + e.getMessage());
        }
    }

    public void removerPedido(int pedidoId) {
        Transaction tx = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            tx = session.beginTransaction();
            Pedido p = session.get(Pedido.class, pedidoId);
            if (p != null) session.remove(p);
            tx.commit();
            System.out.println("Pedido removido com sucesso!");
        } catch (Exception e) {
            if (tx != null) tx.rollback();
            System.out.println("Erro ao remover pedido: " + e.getMessage());
        }
    }
}
