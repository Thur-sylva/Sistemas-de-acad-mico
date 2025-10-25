from package.models.professor import Professor
from .datarecord import DataRecord

class ProfessorController:
    def __init__(self):
        self.data = DataRecord("professores.json")
        self._professores = []
        self.carregar()

    def adicionar_professor(self, nome, titulacao):
        prof = Professor(nome, titulacao)
        self._professores.append(prof)
        self.data.add({"nome": nome, "titulacao": titulacao})

    def listar_professores(self):
        return self._professores

    def buscar_professor_obj(self, nome):
        for p in self._professores:
            if p.get_nome().lower() == nome.lower():
                return p
        return None

    def excluir_professor(self, nome):
        self._professores = [p for p in self._professores if p.get_nome() != nome]
        self.data.remove(lambda d: d["nome"] == nome)

    def carregar(self):
        self._professores = []
        for d in self.data.all():
            prof = Professor(d["nome"], d["titulacao"])
            self._professores.append(prof)