from django.test import TestCase, RequestFactory
from animais.models import Animal

class AnimalModelTestCase(TestCase):

    def setUp(self) -> None:
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não',
        )

    def test_animal_cadastrado_com_caracteristicas(self):
        '''teste que verifica se o animal está cadastrodo com suas respectivas caracteristicas'''
        self.assertEqual(self.animal.nome_animal, 'Leão')