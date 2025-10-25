from package.models.disciplina import Disciplina
from package.controllers.datarecord import DataRecord

class DisciplinaController:
    def __init__(self):
        self.data = DataRecord("disciplinas.json")
        self._disciplinas = []

    def adicionar_disciplina(self, disc: Disciplina):
        self._disciplinas.append(disc)
        self.data.add({
            "nome": disc.nome,
            "codigo": disc.codigo,
            "carga_horaria": disc.carga_horaria,
            "pre_requisitos": disc.pre_requisitos
        })

    def listar_disciplinas(self):
        return self._disciplinas

    def buscar_disciplina(self, codigo):
        for d in self._disciplinas:
            if d.codigo == codigo:
                return d
        return None
