from package.models.pessoa import Pessoa
from package.models.turma import Turma

class Professor(Pessoa):
    def __init__(self, nome, titulacao):
        super().__init__(nome)
        self._titulacao = titulacao
        self._turmas = []

    def adicionar_turma(self, turma: Turma):
        self._turmas.append(turma)
    
    def lancar_nota(self, turma: Turma, aluno, nota):
        if turma in self._turmas:
            turma.lancar_notas(aluno, nota)
            print(f"Nota lançada para {aluno.get_nome()} na turma {turma.disciplina.nome}")
        else:
            print("Essa turma não pertence a este professor.")

    def lancar_frequencia(self, turma: Turma, aluno, freq):
        if turma in self._turmas:
            turma.lancar_frequencia(aluno, freq)
            print(f"Frequência lançada para {aluno.get_nome()} na turma {turma.disciplina.nome}")
        else:
            print("Essa turma não pertence a este professor.")

    def listar_turmas(self):
        for t in self._turmas:
            print(t)

    def __str__(self):
        return f"Nome: {self._nome}, Titulação: {self._titulacao}"
