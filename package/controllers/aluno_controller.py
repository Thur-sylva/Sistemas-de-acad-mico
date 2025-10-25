from package.models.aluno import Aluno
from .datarecord import DataRecord

class AlunoController:
    def __init__(self):
        self.data = DataRecord("alunos.json")
        self._alunos = []
        self.carregar()

    def adicionar_aluno(self, aluno: Aluno):
        self._alunos.append(aluno)
        self.data.add({
            "nome": aluno.get_nome(),
            "curso": aluno._curso,
            "matricula": aluno._matricula,
            "especial": aluno._especial
        })

    def listar_alunos(self):
        return self._alunos

    def buscar_aluno(self, matricula):
        for a in self._alunos:
            if a._matricula == matricula:
                return a
        return None

    def excluir_aluno(self, matricula):
        self._alunos = [a for a in self._alunos if a._matricula != matricula]
        self.data.remove(lambda d: d["matricula"] == matricula)

    def carregar(self):
        self._alunos = []
        for d in self.data.all():
            aluno = Aluno(d["nome"], d["curso"], d["matricula"], d["especial"])
            self._alunos.append(aluno)