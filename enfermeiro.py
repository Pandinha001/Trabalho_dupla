class  Enfermeiro(Pessoa):
    def __init__(self, nome, telefone, email, data_nasc, cpf):
        super().__init__(nome, telefone, email, data_nasc, cpf)
        self.codigo = self.gerar_identificador()

    def GerarIdentinficador(self):
        pass

    def Administrar_medicamento(self):
        pass