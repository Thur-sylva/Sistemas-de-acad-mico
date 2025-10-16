from package.pessoa import Pessoa
from package.professor import Professor

p1 = Professor("Dr. Carlos", "Doutor")
p2 = Professor("Profa. Ana", "Mestre")

print(p1)
print(p2)

print("Nome do prof1:", p1.get_nome())
print("Titulação do prof2:", p2._titulacao)  

p1.set_nome("Dr. Carlos Silva")
p2.set_nome("Profa. Ana Souza")

print("\nApós alteração dos nomes:")
print(p1)
print(p2)