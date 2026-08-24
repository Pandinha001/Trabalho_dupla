
from pessoa import Pessoa
from hospital import Hospital
from paciente import Paciente
from medico import Medico
from enfermeiro import Enfermeiro
from prontuario import Prontuario
from datetime import date

hospital = Hospital()

while True:

    print("BEM VINDO AO HOSPITAL ...")

    print("Possui cadastro?")
    print("1 - Sim")
    print("2 - Não")
    print("3 - sair")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
            print("Antes de darmos continuidade, precisamos saber quem é você. ")
            print("1 - Sim")
            print("2 - Não, sou um intruso")
            print("3 - Não, sou o zelador")
            escolha = int(input("Possui um código? "))
            if escolha == 1:
                
                codigo_identificacao = int(input("Digite seu código de identificação: "))
                pessoa = hospital.buscar_pessoa(codigo_identificacao)

                if pessoa is None:
                    print("haha! esse cadastro não existe.")
                    continue

                if isinstance(pessoa, Paciente):

                    while True:

                        print("\n PACIENTE ")
                        print("1 - Agendar consulta")
                        print("2 - Acessar prontuário")
                        print("3 - Ver meus dados")
                        print("4 - Sair")

                        escolha = input("Escolha: ")

                        if escolha == "1":
                            pessoa.agendar_consulta()

                        elif escolha == "2":
                            pessoa.prontuario.Imprimir_prontuario()

                        elif escolha == "3":
                            pessoa.GerarIdentificador()

                        elif escolha == "4":
                            break
                        
                elif isinstance(pessoa, Medico):

                    while True:

                        print("\n MÉDICO ")
                        print("1 - Prescrever tratamento")
                        print("2 - Ver pacientes")
                        print("3 - Ver meus dados")
                        print("4 - sair")

                        escolha = input("Escolha: ")

                        if escolha == "1":
                            pessoa.prescrever_tratamento()
                        elif escolha == "2":
                            hospital.listar("pacientes")
                        elif escolha == "3":
                            pessoa.GerarIdentificador()
                        elif escolha == "4":
                            break
                elif isinstance(pessoa, Enfermeiro):

                    while True:

                        print("\n ENFERMEIRO ")
                        print("1 - Administrar medicamento")
                        print("2 - Ver pacientes")
                        print("3 - Ver meus dados")
                        print("4 - sair")

                        escolha = input("Escolha: ")

                        if escolha == "1":
                            pessoa.administrar_medicamento()
                        elif escolha == "2":
                            hospital.listar("pacientes")
                        elif escolha == "3":
                            pessoa.GerarIdentificador()
                        elif escolha == "4":
                            break 
            elif escolha == 2:
                print("GUARDAS, PRENDAM-NO!")
            elif escolha == 3:
                print("Hospital limpo com sucesso!")

    elif escolha == 2:
        print("\n NOVO CADASTRO ")
        print("1 - Paciente")
        print("2 - Médico")
        print("3 - Enfermeiro")

        tipo = input("Sua escolha: ")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        data_nasc = input("Data de nascimento: ")
        cpf = input("CPF: ")

        if tipo == "1":
            sintomas = input("Sintomas: ")
            tipo_sanguineo = input("Tipo sanguíneo: ")
            exame = input("qual o exame deseja fazer: ")
            data_entrada = date.today().strftime("%d/%m/%Y")

            paciente = Paciente(
                nome,
                telefone,
                email,
                data_nasc,
                cpf,
                tipo_sanguineo
            )
            paciente.prontuario = Prontuario(nome, telefone, email, data_nasc, cpf, sintomas, tipo_sanguineo, exame, data_entrada)
            hospital.adicionar(paciente)    

            print("\n Agradecemos a prefêrencia!")
            print("Seu código é:", paciente.codigo)
        elif tipo == "2":
            especialidade = input("Especialidade (cardiologista, pediatra, clinico geral, cirurgiao):  ")
            medico = Medico(
                nome,
                telefone,
                email,
                data_nasc,
                cpf,
                especialidade,
            )
            hospital.adicionar(medico)
            print("\nCadastro realizado!")
            print("Seu código é:", medico.codigo)
        elif tipo == "3":
            enfermeiro = Enfermeiro(
                nome,
                telefone,
                email,
                data_nasc,
                cpf,
            )
            hospital.adicionar(enfermeiro)
            print("\nCadastro realizado!")
            print("Seu código é:", enfermeiro.codigo)

        else:
            print("Opção inválida.")
    elif escolha == 3:
        break
