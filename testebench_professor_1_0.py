from package.models.professor import Professor
from package.models.aluno import Aluno
from package.models.disciplina import Disciplina
from package.models.turma import Turma

disc = Disciplina("Matemática", "MAT101", 60)

prof = Professor("Dr. Silva", "Doutor")

aluno1 = Aluno("Alice", "Engenharia", 1001)
aluno2 = Aluno("Bob", "Engenharia", 1002, especial=True)

turma = Turma(disc, prof)
prof.adicionar_turma(turma)  


turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)

prof.lancar_nota(turma, aluno1, 8.5)
prof.lancar_nota(turma, aluno2, 9.0)

prof.lancar_frequencia(turma, aluno1, 90)
prof.lancar_frequencia(turma, aluno2, 95)
print("                                                 ")
print(" Alunos da turma de Matemática ")
turma.listar_alunos()