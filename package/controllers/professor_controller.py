from package.models.professor import Professor
from package.controllers.datarecord import DataRecord

class ProfessorController:
    def __init__(self):
        self.data = DataRecord("professores.json")
        self._professores = []

    def adicionar_professor(self, prof: Professor):
        self._professores.append(prof)
        self.data.add({
            "nome": prof.get_nome(),
            "titulacao": prof._titulacao
        })

    def listar_professores(self):
        return self._professores

    def buscar_professor_obj(self, nome):
        for p in self._professores:
            if p.get_nome() == nome:
                return p
        return None