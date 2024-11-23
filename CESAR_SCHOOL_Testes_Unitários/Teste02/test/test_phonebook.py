import pytest


class TestePhoneBook:

    @pytest.mark.parametrize(
        "test_data", ["car#los", "@carlos", "car!los", "cart%r", "car$los"]
    )
    def test_add_phonebook_com_caractere_invalido(self, setUp, test_data):
        """teste add com caractere inválido"""
        resultado = setUp.add(test_data, "123456789")
        experado = "Nome invalido"
        assert resultado == experado
