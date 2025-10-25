import json

class DataRecord:
    def __init__(self, filename):
        self.__filename = f"package/data/{filename}"
        self.__models = []
        self.read()

    def read(self):
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                self.__models = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.__models = []

    def save(self):
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(self.__models, f, indent=4, ensure_ascii=False)

    def add(self, item):
        self.__models.append(item)
        self.save()

    def all(self):
        return self.__models

    def clear(self):
        self.__models = []
        self.save()

    def remove(self, predicate):
        
        self.__models = [m for m in self.__models if not predicate(m)]
        self.save()

    def update(self, predicate, new_item):
        """Atualiza item existente"""
        for i, m in enumerate(self.__models):
            if predicate(m):
                self.__models[i] = new_item
                break
        self.save()