package com.example;

import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "cliente")
public class Cliente {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "nome", nullable = false)
    private String nome;

    @OneToMany(mappedBy = "cliente", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    private List<Pedido> pedidos = new ArrayList<>();

    public Cliente() {}
    public Cliente(String nome) { this.nome = nome; }

    public void addPedido(Pedido p) {
        pedidos.add(p);
        p.setCliente(this);
    }

    public void removePedido(Pedido p) {
        pedidos.remove(p);
        p.setCliente(null);
    }

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public List<Pedido> getPedidos() { return pedidos; }

    @Override
    public String toString() {
        return "Cliente{id=" + id + ", nome='" + nome + "', pedidos=" + pedidos.size() + "}";
    }
}
