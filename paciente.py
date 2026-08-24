from pessoa import Pessoa

pacientes = {}
class Paciente(Pessoa):

    contador = 0
    def __init__(self, nome, telefone, email, data_nasc, cpf, tipo_sanguineo):
        super().__init__(nome, telefone, email, data_nasc, cpf)
        self.codigo = self.codigo_identificacao()
        self.prontuario = None
        self._tipo_sanguineo = tipo_sanguineo
    def GerarIdentificador(self):
        dados_base = super().GerarIdentificador()
        return f"[Cód: {self.codigo}] {dados_base}"
        
    def codigo_identificacao(self):
        Paciente.contador += 1
        return Paciente.contador
        
    def agendar_consulta(self):
        print("OLA! VAMOS COMEÇAR SEU AGENDAMENTO")
        cod_consulta = int(input("informe seu código de identificação:"))
        especialista = input("informe o especialista: (cardiologista, pediatra, clinico geral, cirurgiao): ")
        data_consulta = input(" informe a data da consulta (dd/mm/yy): ") 
        print("Consulta agendada com sucesso! Suas informações: "
        f"codigo: {cod_consulta}, especialista: {especialista}, data: {data_consulta}")
