from paciente import Paciente
from medico import Medico
from enfermeiro import Enfermeiro

class Hospital:
    def __init__(self):
        self.pessoas = []
    def adicionar(self, pessoa):
        self.pessoas.append(pessoa)
    def buscar_pessoa(self,codigo,tipo):
        if tipo == 1:
            for pessoa in self.pessoas:
                if pessoa.codigo == codigo and isinstance(pessoa,Paciente):
                    return pessoa
        elif tipo == 2:
            for pessoa in self.pessoas:
                if pessoa.codigo == codigo and isinstance(pessoa,Medico):
                    return pessoa
        else:
            for pessoa in self.pessoas:
                if pessoa.codigo == codigo and isinstance(pessoa,Enfermeiro):
                    return pessoa

    def listar(self, tipo):
        encontrou = False
        if tipo == "pacientes":
            for pessoa in self.pessoas:
                if isinstance(pessoa, Paciente):
                    print(pessoa)
                    encontrou = True
        elif tipo == "medicos":
            for pessoa in self.pessoas:
                if isinstance(pessoa, Medico):
                    print(pessoa)
                    encontrou = True
        elif tipo == "enfermeiros":
            for pessoa in self.pessoas:
                if isinstance(pessoa, Enfermeiro):
                    print(pessoa)
                    encontrou = True
        if not encontrou:
            print("Essa categoria não existe nesse hospital")