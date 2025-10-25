from package.models.turma import Turma
from package.models.aluno import Aluno
from package.models.professor import Professor
from package.models.disciplina import Disciplina
from .datarecord import DataRecord
from .disciplina_controller import DisciplinaController

class TurmaController:
    def __init__(self, disc_ctrl: DisciplinaController):
        self.disc_ctrl = disc_ctrl
        self.data = DataRecord("turmas.json")
        self._turmas = []
        self.carregar()

    def criar_turma(self, disciplina: Disciplina, professor: Professor, presencial: bool, sala: str, horario: str):
        turma = Turma(disciplina, professor, presencial, sala, horario)
        self._turmas.append(turma)
        self.salvar()
        return turma

    def listar_turmas(self):
        return self._turmas

    def buscar_turma(self, codigo_disc):
        for t in self._turmas:
            if t.disciplina.codigo == codigo_disc:
                return t
        return None

    def excluir_turma(self, codigo_disc):
        turma = self.buscar_turma(codigo_disc)
        if turma:
            self._turmas.remove(turma)
            self.salvar()
            return True
        return False

    def salvar(self):
        dados = []
        for t in self._turmas:
            dados.append({
                "disciplina": t.disciplina.codigo,
                "professor": t.professor.get_nome(),
                "presencial": t.presencial,
                "sala": t.sala,
                "horario": t.horario,
                "alunos": [
                    {
                        "matricula": a.get_matricula(),
                        "nome": a.get_nome(),
                        "nota": getattr(a, "_nota", None),
                        "frequencia": getattr(a, "_frequencia", None)
                    } for a in t.alunos
                ]
            })
        self.data._DataRecord__models = dados
        self.data.save()

    def carregar(self):
        self._turmas = []
        for t_data in self.data.all():
            disciplina = Disciplina(t_data["disciplina"], t_data["disciplina"], 0)
            professor = Professor(t_data["professor"], "Titulação")
            turma = Turma(disciplina, professor, t_data["presencial"], t_data["sala"], t_data["horario"])
            for a_data in t_data.get("alunos", []):
                aluno = Aluno(a_data["nome"], "Curso", a_data["matricula"])
                if a_data.get("nota") is not None:
                    aluno._nota = a_data["nota"]
                if a_data.get("frequencia") is not None:
                    aluno._frequencia = a_data["frequencia"]
                turma.adicionar_aluno(aluno)
            self._turmas.append(turma)