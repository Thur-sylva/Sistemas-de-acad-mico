from package.models.aluno import Aluno
from package.controllers.datarecord import DataRecord

class AlunoController:
    def __init__(self):
        self.data = DataRecord("alunos.json")
        self._alunos = []

    def adicionar_aluno(self, aluno: Aluno):
        self._alunos.append(aluno)
        self.data.add({
            "nome": aluno.get_nome(),
            "curso": aluno.get_curso(),
            "matricula": aluno.get_matricula(),
            "especial": aluno._especial
        })

    def listar_alunos(self):
        return self._alunos

    def buscar_aluno_obj(self, matricula):
        for a in self._alunos:
            if a.get_matricula() == matricula:
                return a
        return None