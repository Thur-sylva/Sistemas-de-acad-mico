class Disciplina:
    def __init__(self, nome, codigo, carga_horaria, pre_requisitos=None):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.pre_requisitos = pre_requisitos if pre_requisitos else []
        self.turmas = []  
    
    def criar_turma(self, turma):
        self.turmas.append(turma)
    
    def adicionar_aluno(self, aluno):
        return True
    
    def __str__(self):
        return f"{self.codigo} - {self.nome} ({self.carga_horaria}h)"