package com.example;

import jakarta.persistence.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Entity
@Table(name = "pedido")
public class Pedido {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "cliente_id", nullable = false)
    private Cliente cliente;

    @Column(name = "data", nullable = false)
    private LocalDateTime data;

    @Column(name = "total", nullable = false, precision = 12, scale = 2)
    private BigDecimal total;

    public Pedido() {}
    public Pedido(LocalDateTime data, BigDecimal total) {
        this.data = data;
        this.total = total;
    }

    public int getId() { return id; }
    public Cliente getCliente() { return cliente; }
    public void setCliente(Cliente cliente) { this.cliente = cliente; }
    public LocalDateTime getData() { return data; }
    public void setData(LocalDateTime data) { this.data = data; }
    public BigDecimal getTotal() { return total; }
    public void setTotal(BigDecimal total) { this.total = total; }

    @Override
    public String toString() {
        return "Pedido{id=" + id + ", data=" + data + ", total=" + total + "}";
    }
}
