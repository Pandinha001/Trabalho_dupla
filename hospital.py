from pessoa import Pessoa
from paciente import Paciente
from medico import Medico
from enfermeiro import Enfermeiro

class Hospital:

    def __init__(self):
        self.pessoas = []

    def adicionar(self, pessoa):
        self.pessoas.append(pessoa)
    def buscar_pessoa(self, codigo):
        for pessoa in self.pessoas:

            if pessoa.codigo == codigo:
                return pessoa
        return None
    def listar(self, tipo):
        if tipo == "pacientes":
            for pessoa in self.pessoas:
                if isinstance(pessoa, Paciente):
                    print(pessoa)

        elif tipo == "medicos":

            for pessoa in self.pessoas:

                if isinstance(pessoa, Medico):
                    print(pessoa)

        elif tipo == "enfermeiros":
            for pessoa in self.pessoas:
                if isinstance(pessoa, Enfermeiro):
                    print(pessoa)

        else:
            print("Isso não existe no hospital")