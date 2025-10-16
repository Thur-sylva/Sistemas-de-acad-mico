from package.disciplina import Disciplina
from package.professor import Professor
from package.aluno import Aluno

class Turma:
    def __init__(self, disciplina, professor, semestre, capacidade, presencial=True, sala=None, horario=None, forma_avaliacao="Final Média"):
        self.disciplina = disciplina  
        self.professor = professor    
        self.capacidade = capacidade
        self.presencial = presencial
        self.sala = sala if presencial else None
        self.horario = horario
        self.alunos = []  
        self.forma_avaliacao = forma_avaliacao
        self.notas = {}   
        self.frequencia = {}  
    
    def adicionar_aluno(self, aluno):
        if len(self.alunos) >= self.capacidade:
            print(f"Turma cheia!")
            return False
        # Verificar pré-requisitos
        for pre in self.disciplina.pre_requisitos:
            if pre not in [d.codigo for d in aluno._disciplinas]:
                print(f"{aluno.get_nome()} não cumpriu pré-requisitos!")
                return False
        self.alunos.append(aluno)
        return True
    
    def lancar_notas(self, aluno, notas):
        if aluno in self.alunos:
            self.notas[aluno] = notas
    
    def lancar_frequencia(self, aluno, percentual):
        if aluno in self.alunos:
            self.frequencia[aluno] = percentual
    
    def __str__(self):
        tipo = "Presencial" if self.presencial else "Remoto"
        return f"Turma de {self.disciplina.nome} - {tipo} - Prof: {self.professor.get_nome()}"