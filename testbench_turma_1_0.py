from package.models.aluno import Aluno
from package.models.professor import Professor
from package.models.disciplina import Disciplina
from package.models.turma import Turma


disc = Disciplina("Física", "FIS101", 60)
prof = Professor("Dra. Ana", "Mestre")
turma = Turma(disc, prof, presencial=True, sala="101", horario="08:00-10:00")

aluno1 = Aluno("Carlos", "Engenharia", 2001)
aluno2 = Aluno("Daniela", "Engenharia", 2002, especial=True)

print("Matriculando alunos...")
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)

turma.lancar_notas(aluno1, 7.5)
turma.lancar_notas(aluno2, 9.0)

turma.lancar_frequencia(aluno1, 85)
turma.lancar_frequencia(aluno2, 95)

print("\nAlunos da turma de Física ")
turma.listar_alunos()

print("\nInformações da turma:")
print(turma)