class Pessoa():
    def __init__(self, nome, telefone, email, data_nasc, cpf):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.data_nasc = data_nasc
        self.cpf = cpf
    def GerarIdentinficador(self):
        print(self.nome)
        print(self.telefone)
        print(self.email)
        print(self.data_nasc)
        print(self.cpf)
                

    
