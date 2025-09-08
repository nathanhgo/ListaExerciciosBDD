package pacote;

import jakarta.persistence.*;

@Entity
@DiscriminatorValue("Juridico")
public class Juridico extends Cliente {
    
    private String cnpj;

    public void setCnpj(String cnpj) {
        this.cnpj = cnpj;
    }
    public String getCnpj() {
        return cnpj;
    }
    
}
