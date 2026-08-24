from pessoa import Pessoa

class  Enfermeiro(Pessoa):
    contador = 0
    def __init__(self, nome, telefone, email, data_nasc, cpf):
        super().__init__(nome, telefone, email, data_nasc, cpf)
        self.codigo = self.codigo_identificacao()

    def GerarIdentinficador(self):
        print(self.nome)
        print(self.telefone)
        print(self.email)
        print(self.data_nasc)
        print(self.cpf)

    def codigo_identificacao(self):

        Enfermeiro.contador += 1
        return Enfermeiro.contador

    def administrar_medicamento(self):
        doenca = input("qual sua doença?")

        print("remedio administrado com sucesso")
