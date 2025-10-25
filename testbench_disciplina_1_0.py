from package.models.disciplina import Disciplina

# Criando disciplinas
disc1 = Disciplina("Matemática", "MAT101", 60)
disc2 = Disciplina("Física", "FIS101", 80, pre_requisitos=["MAT101"])

print(disc1)
print(disc2)

print("\nPré-requisitos de Física:", disc2.pre_requisitos)

disc1.criar_turma("Turma A")
disc1.criar_turma("Turma B")

disc2.criar_turma("Turma 1")

print("\nTurmas de Matemática:", disc1.turmas)
print("Turmas de Física:", disc2.turmas)