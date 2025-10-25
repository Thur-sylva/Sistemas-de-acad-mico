class Pessoa:
    def __init__(self, nome):
        self.set_nome(nome)
    
    def set_nome(self, nome):
        if isinstance(nome, str):
            self._nome = nome
        else:
            print("Entre com um nome válido (string)!")

    def get_nome(self):
        return self._nome

    def __str__(self):
        return f"Nome: {self._nome}"