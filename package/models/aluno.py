from package.models.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, curso, matricula, especial=False):
        super().__init__(nome)
        self.set_matricula(matricula)
        self.set_curso(curso)
        self._disciplinas = []
        self._especial = especial
        self._nota = None
        self._frequencia = None

    def set_curso(self, curso):
        if isinstance(curso, str):
            self._curso = curso
        else: 
            print("Entre com um curso válido (string)")

    def set_matricula(self, matricula):
        if isinstance(matricula, int):
            self._matricula = matricula 
        else:
            print("Entre com uma matrícula válida (int)")
    
    def get_curso(self):
        return self._curso
    
    def get_matricula(self):
        return self._matricula
    
    def matricular_disciplina(self, disciplina):
        if self._especial and len(self._disciplinas) >= 2:
            print(f"{self._nome} é aluno especial e já atingiu o limite de disciplinas")
            return False
        if disciplina.adicionar_aluno(self):
            self._disciplinas.append(disciplina)
            return True
        return False

    def __str__(self):
        tipo = "especial" if self._especial else "normal"
        return f"{super().__str__()}, Curso: {self._curso}, Matrícula: {self._matricula}, Tipo: {tipo}"