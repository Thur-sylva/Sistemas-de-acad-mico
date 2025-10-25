from ..models.disciplina import Disciplina

def menu_disciplina(disc_ctrl):
    while True:
        print("\nMENU DISCIPLINA ")
        print("1 - Cadastrar Disciplina")
        print("2 - Listar Disciplinas")
        print("3 - Excluir Disciplina")
        print("0 - Voltar")
        opc = input("Escolha: ").strip()

        if opc == "1":
            nome = input("Nome: ").strip()
            codigo = input("Código: ").strip()
            carga = int(input("Carga horária: "))
            
            disc_ctrl.adicionar_disciplina(nome, codigo, carga)
            print(f"Disciplina {nome} cadastrada!")

        elif opc == "2":
            disciplinas = disc_ctrl.listar_disciplinas()
            if disciplinas:
                for d in disciplinas:
                    print(f"- {d.nome} | Código: {d.codigo} | Carga: {d.carga_horaria}")
            else:
                print("Nenhuma disciplina cadastrada.")

        elif opc == "3":
            codigo = input("Código da disciplina para excluir: ").strip()
            disc = disc_ctrl.buscar_disciplina(codigo)
            if disc:
                disc_ctrl.excluir_disciplina(codigo)
                print(f"Disciplina {disc.nome} excluída!")
            else:
                print("Disciplina não encontrada.")

        elif opc == "0":
            break
        else:
            print("Opção inválida!")