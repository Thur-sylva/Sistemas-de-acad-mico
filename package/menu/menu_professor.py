from ..controllers.professor_controller import ProfessorController
from ..controllers.nota_controller import NotaController

def menu_professor(prof_ctrl: ProfessorController):
    nota_ctrl = NotaController()  

    while True:
        print("\nMENU PROFESSOR ")
        print("1 - Cadastrar Professor")
        print("2 - Listar Professores")
        print("3 - Excluir Professor")
        print("4 - Lançar nota e frequência")
        print("5 - Consultar notas de um aluno")
        print("6 - Consultar notas por disciplina")
        print("0 - Voltar ao menu principal")

        opc = input("Escolha: ").strip()

        if opc == "1":
            nome = input("Nome do professor: ").strip()
            titulacao = input("Titulação: ").strip()
            prof_ctrl.adicionar_professor(nome, titulacao)
            print(f" Professor {nome} cadastrado com sucesso!")

        elif opc == "2":
            professores = prof_ctrl.listar_professores()
            if professores:
                print("\nProfessores cadastrados:")
                for p in professores:
                    print(f"- {p.get_nome()} | Titulação: {p._titulacao}")
            else:
                print("Nenhum professor cadastrado.")

        elif opc == "3":
            nome = input("Nome do professor para excluir: ").strip()
            prof = prof_ctrl.buscar_professor_obj(nome)
            if prof:
                prof_ctrl._professores.remove(prof)
                prof_ctrl.data.clear()
                for p in prof_ctrl._professores:
                    prof_ctrl.data.add({"nome": p.get_nome(), "titulacao": p._titulacao})
                print(f"Professor {nome} excluído com sucesso!")
            else:
                print("Professor não encontrado.")

        elif opc == "4":
            nome_prof = input("Nome do professor: ").strip()
            prof = prof_ctrl.buscar_professor_obj(nome_prof)
            if not prof:
                print("Professor não encontrado!")
                continue

            matricula = input("Matrícula do aluno: ").strip()
            codigo_disc = input("Código da disciplina: ").strip()
            try:
                nota = float(input("Nota do aluno: "))
                freq = float(input("Frequência (%): "))
            except ValueError:
                print("Valor inválido para nota ou frequência!")
                continue

            msg = nota_ctrl.registrar_nota(matricula, codigo_disc, nota, freq)
            print(msg)

        elif opc == "5":
            matricula = input("Matrícula do aluno: ").strip()
            notas = nota_ctrl.buscar_notas_aluno(matricula)
            if notas:
                print(f"\nNotas do aluno {matricula}:")
                for n in notas:
                    print(f"- {n['disciplina']}: Nota={n['nota']}, Freq={n['frequencia']}%")
            else:
                print("Nenhuma nota encontrada para esse aluno.")

        elif opc == "6":
            codigo_disc = input("Código da disciplina: ").strip()
            notas = nota_ctrl.buscar_notas_disciplina(codigo_disc)
            if notas:
                print(f"\nNotas da disciplina {codigo_disc}:")
                for n in notas:
                    print(f"- Matrícula {n['matricula']}: Nota={n['nota']}, Freq={n['frequencia']}%")
            else:
                print("Nenhum lançamento encontrado para essa disciplina.")

        elif opc == "0":
            print("Retornando ao menu principal...")
            break

        else:
            print("Opção inválida!")