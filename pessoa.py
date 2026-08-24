class Pessoa():
    def __init__(self, nome, telefone, email, data_nasc, cpf):
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._data_nasc = data_nasc
        self._cpf = cpf

    def GerarIdentificador(self):
        return f"Nome: {self._nome}, Tel: {self._telefone}, Email: {self._email}, CPF: {self._cpf}"
    def __str__(self):
        return self.GerarIdentificador()

    
