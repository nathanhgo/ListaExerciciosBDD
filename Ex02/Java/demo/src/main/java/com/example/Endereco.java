package com.example;

import jakarta.persistence.*;

@Entity
@Table(name = "endereco")
public class Endereco {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    
    @Column(name = "rua")
    private String rua;
    
    @Column(name = "numero")
    private int numero;

    @OneToOne(mappedBy = "endereco")
    private Cliente cliente;

    public Endereco() {}

    public Endereco(String rua, int numero) {
        this.rua = rua;
        this.numero = numero;
    }

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getRua() { return rua; }
    public void setRua(String rua) { this.rua = rua; }

    public int getNumero() { return numero; }
    public void setNumero(int numero) { this.numero = numero; }

    public Cliente getCliente() { return cliente; }
    public void setCliente(Cliente cliente) { this.cliente = cliente; }

    @Override
    public String toString() {
        return "Endereco{id=" + id + ", rua='" + rua + "', numero=" + numero + "}";
    }
}