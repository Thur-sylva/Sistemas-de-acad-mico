from package.controllers.aluno_controller import AlunoController
from package.controllers.professor_controller import ProfessorController
from package.controllers.disciplina_controller import DisciplinaController
from package.controllers.turma_controller import TurmaController
from package.models.aluno import Aluno
from package.models.professor import Professor
from package.models.disciplina import Disciplina
from package.models.turma import Turma

def menu_principal():
    aluno_ctrl = AlunoController()
    prof_ctrl = ProfessorController()
    disc_ctrl = DisciplinaController()
    turma_ctrl = TurmaController()

    while True:
        print("\n SISTEMA ACADÊMICO")
        print("1 - Cadastrar Aluno")
        print("2 - Cadastrar Professor")
        print("3 - Cadastrar Disciplina")
        print("4 - Criar Turma")
        print("5 - Matricular Aluno em Turma")
        print("6 - Professor lança Nota")
        print("7 - Professor lança Frequência")
        print("8 - Listar Alunos de Turma")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            curso = input("Curso: ")
            matricula = int(input("Matrícula: "))
            especial = input("Aluno especial? (s/n): ").lower() == "s"
            aluno = Aluno(nome, curso, matricula, especial)
            aluno_ctrl.adicionar_aluno(aluno)
            print("Aluno cadastrado!")

        elif opcao == "2":
            nome = input("Nome do professor: ")
            titulacao = input("Titulação: ")
            prof = Professor(nome, titulacao)
            prof_ctrl.adicionar_professor(prof)
            print("Professor cadastrado!")

        elif opcao == "3":
            nome = input("Nome da disciplina: ")
            codigo = input("Código: ")
            carga = int(input("Carga horária: "))
            disc = Disciplina(nome, codigo, carga)
            disc_ctrl.adicionar_disciplina(disc)
            print("Disciplina cadastrada!")

        elif opcao == "4":
            codigo_disc = input("Código da disciplina: ")
            disciplina = disc_ctrl.buscar_disciplina(codigo_disc)
            if not disciplina:
                print("Disciplina não encontrada")
                continue
            nome_prof = input("Nome do professor: ")
            professor = prof_ctrl.buscar_professor_obj(nome_prof)
            if not professor:
                print("Professor não encontrado")
                continue
            turma = Turma(disciplina, professor)
            professor.adicionar_turma(turma)
            turma_ctrl.adicionar_turma(turma)
            print("Turma criada!")

        elif opcao == "5":
            matricula = int(input("Matrícula do aluno: "))
            aluno = aluno_ctrl.buscar_aluno_obj(matricula)
            if not aluno:
                print("Aluno não encontrado")
                continue
            codigo_disc = input("Código da disciplina da turma: ")
            turma = turma_ctrl.buscar_turma_obj(codigo_disc)
            if not turma:
                print("Turma não encontrada")
                continue
            if turma.adicionar_aluno(aluno):
                print("Aluno matriculado!")

        elif opcao == "6": 
            nome_prof = input("Digite seu nome (Professor): ")
            prof = prof_ctrl.buscar_professor_obj(nome_prof)
            if not prof:
                print("Professor não encontrado")
                continue
            print("Suas turmas:")
            prof.listar_turmas()
            codigo_disc = input("Código da disciplina da turma: ")
            turma = next((t for t in prof._turmas if t.disciplina.codigo == codigo_disc), None)
            if not turma:
                print("Turma não encontrada")
                continue
            matricula = int(input("Matrícula do aluno: "))
            aluno = next((a for a in turma.alunos if a.get_matricula() == matricula), None)
            if not aluno:
                print("Aluno não encontrado na turma")
                continue
            nota = float(input("Nota do aluno: "))
            prof.lancar_nota(turma, aluno, nota)

        elif opcao == "7":  
            nome_prof = input("Digite seu nome (Professor): ")
            prof = prof_ctrl.buscar_professor_obj(nome_prof)
            if not prof:
                print("Professor não encontrado")
                continue
            print("Suas turmas:")
            prof.listar_turmas()
            codigo_disc = input("Código da disciplina da turma: ")
            turma = next((t for t in prof._turmas if t.disciplina.codigo == codigo_disc), None)
            if not turma:
                print("Turma não encontrada")
                continue
            matricula = int(input("Matrícula do aluno: "))
            aluno = next((a for a in turma.alunos if a.get_matricula() == matricula), None)
            if not aluno:
                print("Aluno não encontrado na turma")
                continue
            freq = float(input("Frequência do aluno (%): "))
            prof.lancar_frequencia(turma, aluno, freq)

        elif opcao == "8":  
            codigo_disc = input("Código da disciplina da turma: ")
            turma = turma_ctrl.buscar_turma_obj(codigo_disc)
            if not turma:
                print("Turma não encontrada")
                continue
            turma.listar_alunos()

        elif opcao == "0":
            print("Saindo...")
            break