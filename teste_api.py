import unittest
from api import API

class Teste(unittest.TestCase):

    def setUp(self):
        self.zoo = API()

    def teste_criar_animal(self):
        animal = self.zoo.criar_animal('Cobra', 'Réptil', 4)
        self.assertIn(animal, self.zoo.animais)

    def teste_criar_recinto(self):
        recinto = self.zoo.criar_recinto([], True)
        self.assertIn(recinto, self.zoo.recintos)

    def teste_alimentar_animais(self):
        animal = self.zoo.criar_animal('Puma', 'Felino', 5)
        recinto = self.zoo.criar_recinto([animal], True)
        recinto.alimentar_animais()
        self.assertEqual(animal.nivel_felicidade, 6)

    def teste_receber_visitantes(self):
        animal = self.zoo.criar_animal('Elefante', 'Indiano', 3)
        recinto = self.zoo.criar_recinto([animal], True)
        dinheiro_ganho = self.zoo.receber_visitantes()
        self.assertEqual(dinheiro_ganho, 4)

if __name__ == '__main__':
    unittest.main()
