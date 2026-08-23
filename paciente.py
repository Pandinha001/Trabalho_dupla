from pessoa import Pessoa

pacientes = {}
class Paciente(Pessoa):

    contador = 0
    def __init__(self, nome, telefone, email, data_nasc, cpf, sintoma, tipo_sanguineo):
        super().__init__(nome, telefone, email, data_nasc, cpf)
        self.sintoma = sintoma
        self.tipo_sanguineo = tipo_sanguineo
        
        self.codigo_identificacao = self.codigo_identificacao()
        
    def GerarIdentinficador(self):
        print(self.nome)
        print(self.telefone)
        print(self.email)
        print(self.data_nasc)
        print(self.cpf)
        print(self.tipo_sanguineo)
        
    def codigo_identificacao(self):

        Paciente.contador += 1
        return Paciente.contador
        
    def Agendar_consulta(self):
        print("OLA! VAMOS COMEÇAR SEU AGENDAMENTO")
        cod_consulta = int(input("informe seu código de identificação:"))
        especialista = input("informe o especialista: (cardiologista, pediatra, clinico geral, cirurgiao) ")
        data_consulta = input(" informe a data da consulta (dd/mm/yy)") 
