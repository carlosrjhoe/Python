import pytest


class TestePhoneBook:

    @pytest.mark.parametrize(
        "test_data", ["car#los", "@carlos", "car!los", "cart%r", "car$los"]
    )
    def test_add_phonebook_com_caractere_invalido(self, setUp, test_data):
        """teste add com caractere inválido"""
        phonebook = setUp
        resultado = phonebook.add(test_data, "123456789")
        experado = "Nome invalido"
        assert resultado == experado

    def test_lookup_phonebook_com_caractere_invalido(self, setUp):
        """teste lookup com caractere inválido"""
        phonebook = setUp
        phonebook.add('Carlos', '333')
        resultado = phonebook.lookup('Carlos')
        experado = '333'
        assert resultado == experado
