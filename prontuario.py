from paciente import Paciente

class Prontuario(Paciente):
    def __init__(self,  nome, telefone, email, data_nasc, cpf, sintoma, tipo_sanguineo, exame, data_entrada):
        super().__init__(nome, telefone, email, data_nasc, cpf,sintoma, tipo_sanguineo )
        self.exame = exame
        self.data_entrada = data_entrada

    def Imprimir_prontuario(self):

        print("PRONTUÁRIO")
        print("Nome:", self.nome )
        print("cpf:", self.cpf)
        print("sintoma:", self.sintoma)
        print("exame:",self.exame)
        print("remedio:",self.remedio)
        print("tipo saguíneo:", self.tipo_sanguineo)
        print("data entrada", self.data_entrada)
