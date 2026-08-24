from paciente import Paciente

class Prontuario(Paciente):
    def __init__(self,  nome, telefone, email, data_nasc, cpf, sintoma, tipo_sanguineo, exame, data_entrada):
        super().__init__(nome, telefone, email, data_nasc, cpf, tipo_sanguineo)
        self._exame = exame
        self._data_entrada = data_entrada
        self._sintoma = sintoma
        

    def Imprimir_prontuario(self):

        print("PRONTUÁRIO MÉDICO")
        print("Nome:", self._nome )
        print("cpf:", self._cpf)
        print("sintoma:", self._sintoma)
        print("exame:",self._exame)
        print("tipo saguíneo:", self._tipo_sanguineo)
        print("data entrada", self._data_entrada)
