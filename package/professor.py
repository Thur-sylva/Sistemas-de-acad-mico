from package.pessoa import Pessoa
 
class Professor(Pessoa):
    def __init__(self, nome, titulacao):
        super().__init__(nome)
        self._titulacao = titulacao
        self._turmas = []

    def adicionar_turmas(self, turma):
        self._turmas.append(turma)
    
    def __str__(self):
        return f"{super().__str__()}, titulacao: {self._titulacao}"
