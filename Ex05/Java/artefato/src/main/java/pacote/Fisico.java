package pacote;

import jakarta.persistence.*;

@Entity
@DiscriminatorValue("Fisico")
public class Fisico extends Cliente {
    
    private String cpf;

    public String getCpf() {
        return cpf;
    }
    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

}
