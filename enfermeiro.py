from pessoa import Pessoa

class  Enfermeiro(Pessoa):
    contador = 0
    def __init__(self, nome, telefone, email, data_nasc, cpf):
        super().__init__(nome, telefone, email, data_nasc, cpf)
        self.codigo = self.codigo_identificacao()

    def GerarIdentificador(self):
        dados_base = super().GerarIdentificador()
        return f"[Cód: {self.codigo}] {dados_base}"
    
    def codigo_identificacao(self):
        Enfermeiro.contador += 1
        return Enfermeiro.contador

    def administrar_medicamento(self):
        doenca = input("qual sua doença?")
        print(f"Para que o paciente melhore da {doenca}, seu remedio foi administrado com sucesso")
