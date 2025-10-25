from .datarecord import DataRecord

class NotaController:
    def __init__(self):
        self.data = DataRecord("notas.json")

    def registrar_nota(self, matricula, codigo_disc, nota, frequencia):
        registros = self.data.all()
        for r in registros:
            if r["matricula"] == matricula and r["disciplina"] == codigo_disc:
                r["nota"] = nota
                r["frequencia"] = frequencia
                self.data.save()
                return f"✅ Nota e frequência atualizadas"
        # Novo registro
        self.data.add({
            "matricula": matricula,
            "disciplina": codigo_disc,
            "nota": nota,
            "frequencia": frequencia
        })
        return f"✅ Nota e frequência registradas"

    def buscar_notas_aluno(self, matricula):
        return [r for r in self.data.all() if r["matricula"] == matricula]

    def buscar_notas_disciplina(self, codigo_disc):
        return [r for r in self.data.all() if r["disciplina"] == codigo_disc]