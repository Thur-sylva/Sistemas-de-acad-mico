from package.aluno import Aluno
from package.professor import Professor
from package.disciplina import Disciplina
from package.turma import Turma


prof = Professor("Dr. Carlos", "Doutor")

disc = Disciplina("Matemática", "MAT101", 60)

aluno1 = Aluno("João", "Engenharia de Software", 12345)
aluno2 = Aluno("Maria", "Engenharia Eletrônica", 54321)

turma = Turma(disciplina=disc, professor=prof, semestre="2025/2", capacidade=2, presencial=True, sala="101", horario="08:00-10:00")

print(turma)

print("\nMatriculando alunos:")
print("João:", turma.adicionar_aluno(aluno1))
print("Maria:", turma.adicionar_aluno(aluno2))

aluno3 = Aluno("Pedro", "Engenharia de Software", 67890)
print("Pedro:", turma.adicionar_aluno(aluno3))  

print("\nAlunos matriculados na turma:")
for aluno in turma.alunos:
    print(aluno)