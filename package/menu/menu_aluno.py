from ..models.aluno import Aluno

def menu_aluno(aluno_ctrl):
    while True:
        print("\n MENU ALUNO ")
        print("1 - Cadastrar Aluno")
        print("2 - Listar Alunos")
        print("3 - Excluir Aluno")
        print("0 - Voltar")
        opc = input("Escolha: ").strip()

        if opc == "1":
            nome = input("Nome: ").strip()
            curso = input("Curso: ").strip()
            matricula = int(input("Matrícula: "))
            especial = input("Especial (s/n): ").strip().lower() == "s"
            aluno = Aluno(nome, curso, matricula, especial)
            aluno_ctrl.adicionar_aluno(aluno)
            print(f"Aluno {nome} cadastrado!")

        elif opc == "2":
            alunos = aluno_ctrl.listar_alunos()
            if alunos:
                print("\nLista de Alunos:")
                for a in alunos:
                    print(f"- {a.get_nome()} | Matrícula: {a.get_matricula()} | Curso: {a._curso}")
            else:
                print("Nenhum aluno cadastrado.")

        elif opc == "3":
            matricula = int(input("Matrícula do aluno para excluir: "))
            aluno = aluno_ctrl.buscar_aluno(matricula)
            if aluno:
                aluno_ctrl._alunos.remove(aluno)
                aluno_ctrl.data.clear()  
                for a in aluno_ctrl._alunos:
                    aluno_ctrl.data.add({
                        "nome": a.get_nome(),
                        "curso": a._curso,
                        "matricula": a._matricula,
                        "especial": a._especial
                    })
                print(f"Aluno {aluno.get_nome()} excluído!")
            else:
                print("Aluno não encontrado.")

        elif opc == "0":
            break
        else:
            print("Opção inválida!")