

class Prontuario():
    def __init__(self,  sintomas, tipo_sanguineo, exame, data_entrada, paciente):
        
        self._exame = exame
        self._data_entrada = data_entrada
        self._sintoma = sintomas
        self.p =  paciente
        self._tipo_sanguineo = tipo_sanguineo
    def Imprimir_prontuario(self):
        print("PRONTUÁRIO MÉDICO")
        print("Nome:", self.p._nome )
        print("cpf:", self.p._cpf)
        print("sintoma:", self._sintoma)
        print("exame:",self._exame)
        print("tipo saguíneo:", self._tipo_sanguineo)
        print("data entrada", self._data_entrada)
