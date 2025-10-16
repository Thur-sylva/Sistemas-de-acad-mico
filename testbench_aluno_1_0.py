from package.pessoa import Pessoa
from package.aluno import Aluno

aluno1 = Aluno("João", "Engenharia de Software", 12345)
aluno2 = Aluno("Maria", "Engenharia Eletrônica", 54321, especial=True)  # aluno especial

print(aluno1)
print(aluno2)

print("Nome de João:", aluno1.get_nome())
print("Curso de Maria:", aluno2.get_curso())
print("Matrícula de João:", aluno1.get_matricula())

aluno1.set_nome("João Pedro")
aluno1.set_curso("Engenharia Eletrônica")
aluno1.set_matricula(98765)

print("\nApós alteração:")
print(aluno1)