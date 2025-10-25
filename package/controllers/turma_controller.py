from package.models.turma import Turma
from package.controllers.datarecord import DataRecord

class TurmaController:
    def __init__(self):
        self.data = DataRecord("turmas.json")
        self._turmas = []

    def adicionar_turma(self, turma: Turma):
        self._turmas.append(turma)
        self.data.add({
            "disciplina": turma.disciplina.codigo,
            "professor": turma.professor.get_nome(),
            "presencial": turma.presencial,
            "sala": turma.sala,
            "horario": turma.horario
        })

    def listar_turmas(self):
        return self._turmas

    def buscar_turma_obj(self, codigo_disciplina):
        for t in self._turmas:
            if t.disciplina.codigo == codigo_disciplina:
                return t
        return None