class Medico(Pessoa):
    def __init__(self, nome, telefone, email, data_nasc, cpf, especialidade, cod_medico):
        super().__init__(nome, telefone, email, data_nasc, cpf)

    def GerarIdentinficador(self):
        pass

    def Criar_laudo(self):
        pass

    def prescrever_tratamento(self):
        pass