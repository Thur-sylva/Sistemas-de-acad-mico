class Turma:
    def __init__(self, disciplina, professor, presencial=True, sala=None, horario=None):
        self.disciplina = disciplina
        self.professor = professor
        self.presencial = presencial
        self.sala = sala if presencial else None
        self.horario = horario
        self.alunos = []

    def adicionar_aluno(self, aluno):
        for pre in self.disciplina.pre_requisitos:
            if pre not in [d.codigo for d in aluno._disciplinas]:
                print(f"{aluno.get_nome()} não cumpriu pré-requisitos!")
                return False
        self.alunos.append(aluno)
        return True

    def lancar_notas(self, aluno, nota):
        if aluno in self.alunos:
            aluno._nota = nota

    def lancar_frequencia(self, aluno, freq):
        if aluno in self.alunos:
            aluno._frequencia = freq

    def listar_alunos(self):
        for a in self.alunos:
            nota = getattr(a, "_nota", "N/A")
            freq = getattr(a, "_frequencia", "N/A")
            print(f"{a.get_nome()} - Nota: {nota} - Frequência: {freq}")

    def __str__(self):
        tipo = "Presencial" if self.presencial else "Remoto"
        return f"Turma de {self.disciplina.nome} - {tipo} - Prof: {self.professor.get_nome()}"