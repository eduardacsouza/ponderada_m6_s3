class Animal:
    def __init__(self, nome, especie, nivel_felicidade):
        self.nome = nome
        self.especie = especie
        self.nivel_felicidade = nivel_felicidade


class API:
    def __init__(self):
        self.animais = []

    def criar_animal(self, nome, especie, nivel_felicidade):
        animal = Animal(nome, especie, nivel_felicidade)
        self.animais.append(animal)
        return animal
