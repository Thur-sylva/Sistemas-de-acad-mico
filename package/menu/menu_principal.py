from ..controllers.aluno_controller import AlunoController
from ..controllers.professor_controller import ProfessorController
from ..controllers.disciplina_controller import DisciplinaController
from ..controllers.turma_controller import TurmaController

from .menu_aluno import menu_aluno
from .menu_professor import menu_professor
from .menu_disciplina import menu_disciplina
from .menu_turma import menu_turma

def menu_principal():
    aluno_ctrl = AlunoController()
    prof_ctrl = ProfessorController()
    disc_ctrl = DisciplinaController()
    turma_ctrl = TurmaController(disc_ctrl)  

    while True:
        print("\n=== SISTEMA ACADÊMICO ===")
        print("1 - Aluno")
        print("2 - Professor")
        print("3 - Disciplina")
        print("4 - Turma")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            menu_aluno(aluno_ctrl)
        elif opcao == "2":
            menu_professor(prof_ctrl) 
        elif opcao == "3":
            menu_disciplina(disc_ctrl)
        elif opcao == "4":
            menu_turma(turma_ctrl, aluno_ctrl, disc_ctrl, prof_ctrl)
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")