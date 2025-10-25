
from package.models.disciplina import Disciplina
from .datarecord import DataRecord

class DisciplinaController:
    def __init__(self):
        self.data = DataRecord("disciplinas.json")
        self._disciplinas = []
        self.carregar()

    def adicionar_disciplina(self, nome, codigo, carga_horaria):
        disc = Disciplina(nome, codigo, carga_horaria)
        self._disciplinas.append(disc)
        self.data.add({"nome": nome, "codigo": codigo, "carga_horaria": carga_horaria})

    def listar_disciplinas(self):
        return self._disciplinas

    def buscar_disciplina(self, codigo):
        for d in self._disciplinas:
            if d.codigo == codigo:
                return d
        return None

    def excluir_disciplina(self, codigo):
        self._disciplinas = [d for d in self._disciplinas if d.codigo != codigo]
        self.data.remove(lambda d: d["codigo"] == codigo)

    def carregar(self):
        self._disciplinas = []
        for d in self.data.all():
            disc = Disciplina(d["nome"], d["codigo"], d["carga_horaria"])
            self._disciplinas.append(disc)