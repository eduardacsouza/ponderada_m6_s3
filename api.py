class Animal:
    def __init__(self, nome, especie, nivel_felicidade):
        self.nome = nome
        self.especie = especie
        self.nivel_felicidade = nivel_felicidade

class Recinto:
    def __init__(self, animais, bem_cuidado):
        self.animais = animais
        self.bem_cuidado = bem_cuidado

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def remover_animal(self, animal):
        self.animais.remove(animal)

    def alimentar_animais(self):
        for animal in self.animais:
            animal.nivel_felicidade += 1

class API:
    def __init__(self):
        self.animais = []
        self.recintos = []

    def criar_animal(self, nome, especie, nivel_felicidade):
        animal = Animal(nome, especie, nivel_felicidade)
        self.animais.append(animal)
        return animal

    def criar_recinto(self, animais, bem_cuidado):
        recinto = Recinto(animais, bem_cuidado)
        self.recintos.append(recinto)
        return recinto

    def receber_visitantes(self):
        visitantes = sum([len(recinto.animais) for recinto in self.recintos])
        dinheiro_ganho = visitantes * 4  
        return dinheiro_ganho
