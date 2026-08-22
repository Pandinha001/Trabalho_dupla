
pacientes = {}
class Paciente(Pessoa):
    def __init__(self, nome, telefone, email, data_nasc, cpf, sintoma, historico_medico, tipo_sanguineo):
        super().__init__(nome, telefone, email, data_nasc, cpf)

        self.sintoma = sintoma
        self.historico_medico = historico_medico
        self.tipo_sanguineo = tipo_sanguineo

    def GerarIdentinficador(self):
        pass

    def Agendar_consulta(self):
        pass