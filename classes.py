class Pessoa():
    def __init__(self, nome, telefone, email, data_nasc, cpf):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.data_nasc = data_nasc
        self.cpf = cpf
    def GerarIdentinficador():
        pass

    

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




class  Enfermeiro(Pessoa):
    def __init__(self, nome, telefone, email, data_nasc, cpf, cod_infermeiro):
        super().__init__(nome, telefone, email, data_nasc, cpf)

    def GerarIdentinficador(self):
        pass

    def Administrar_medicamento(self):
        pass



class Medico(Pessoa):
    def __init__(self, nome, telefone, email, data_nasc, cpf, especialidade, cod_medico):
        super().__init__(nome, telefone, email, data_nasc, cpf)

    def GerarIdentinficador(self):
        pass

    def Criar_laudo(self):
        pass

    def prescrever_tratamento(self):
        pass


class Prontuario():
    def __init__(self, remedio, exame, data_entrada):
        self.