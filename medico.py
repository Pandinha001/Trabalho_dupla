
from pessoa import Pessoa

class Medico(Pessoa):
    contador = 0

    def __init__(self, nome, telefone, email, data_nasc, cpf, especialidade):
        super().__init__(nome, telefone, email, data_nasc, cpf)
        self.especialidade = especialidade
        self.codigo = self.codigo_identificacao() 

    def GerarIdentinficador(self):
        print(self.nome)
        print(self.telefone)
        print(self.email)
        print(self.data_nasc)
        print(self.cpf)
        print(self.especialidade)
        
    def codigo_identificacao(self):
        Medico.contador += 1
        return Medico.contador
        

    def prescrever_tratamento(self):
        print("informe o especialista: )")
        print("1- cardiologista")
        print("2- pediatra")
        print("3- clínic geral")
        print("4- cirurgião")
        escolha = int(input("Qual sua opção: "))

        if escolha == 1:
            print("NÃO BEBA ENERGÉTICO☕")
        elif escolha == 2:
            print("NÃO COMA DOCE🍭🍬")
        elif escolha == 3:
            print("FAÇA UM CHECK UP🩺🩻")
        elif escolha == 4:
            ("Marque uma cirurgia🏥")
        else:
            print("INVALIDO ")
