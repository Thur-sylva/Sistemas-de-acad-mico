from ..controllers.aluno_controller import AlunoController
from ..controllers.professor_controller import ProfessorController
from ..controllers.disciplina_controller import DisciplinaController
from ..controllers.turma_controller import TurmaController

def menu_turma(turma_ctrl: TurmaController, aluno_ctrl: AlunoController,
               disc_ctrl: DisciplinaController, prof_ctrl: ProfessorController):

    while True:
        print("\nMENU TURMA ")
        print("1 - Cadastrar Turma")
        print("2 - Listar Turmas")
        print("3 - Excluir Turma")
        print("4 - Matricular aluno em turma")
        print("0 - Voltar")
        opc = input("Escolha: ").strip()

        if opc == "1":
            codigo_disc = input("Código da disciplina: ").strip()
            disciplina = disc_ctrl.buscar_disciplina(codigo_disc)
            if not disciplina:
                print("Disciplina não encontrada!")
                continue

            nome_prof = input("Nome do professor: ").strip()
            professor = prof_ctrl.buscar_professor_obj(nome_prof)
            if not professor:
                print("Professor não encontrado!")
                continue

            presencial = input("Presencial (s/n): ").strip().lower() == "s"
            sala = input("Sala: ").strip()
            horario = input("Horário: ").strip()

            turma = turma_ctrl.criar_turma(disciplina, professor, presencial, sala, horario)
            print(f"Turma de {disciplina.nome} criada com sucesso!")

        elif opc == "2":
            turmas = turma_ctrl.listar_turmas()
            if turmas:
                for t in turmas:
                    print(f"- {t.disciplina.nome} | Professor: {t.professor.get_nome()} | "
                          f"Sala: {t.sala} | Horário: {t.horario} | "
                          f"Alunos: {len(t.alunos)}")
            else:
                print("Nenhuma turma cadastrada.")

        elif opc == "3":
            codigo_disc = input("Código da disciplina para excluir: ").strip()
            if turma_ctrl.excluir_turma(codigo_disc):
                print("Turma excluída com sucesso!")
            else:
                print("Turma não encontrada!")

        elif opc == "4":
            matricula_input = input("Matrícula do aluno: ").strip()
            try:
                matricula = int(matricula_input)
            except ValueError:
                print("Matrícula inválida!")
                continue

            aluno = aluno_ctrl.buscar_aluno(matricula)
            if not aluno:
                print("Aluno não encontrado!")
                continue

            codigo_disc = input("Código da disciplina: ").strip()
            turma = turma_ctrl.buscar_turma(codigo_disc)
            if not turma:
                print("Turma não encontrada!")
                continue

            turma.adicionar_aluno(aluno)
            turma_ctrl.salvar()
            print(f"Aluno {aluno.get_nome()} matriculado na turma {turma.disciplina.nome}!")

        elif opc == "0":
            break

        else:
            print("Opção inválida!")