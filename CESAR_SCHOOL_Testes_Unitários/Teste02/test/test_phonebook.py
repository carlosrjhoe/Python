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

    def test_add_numero_invalido(self, setUp):
        phonebook = setUp
        resultado = phonebook.add("Carlos", " ")
        esperado = "Numero invalido"
        assert resultado == esperado

    def test_add_phonebook_name_nao_existe_adicionado(self, setUp):
        phonebook = setUp
        phonebook.add("Carlos", "123456789")
        resultado = "Carlos" in phonebook.entries
        esperado = True
        assert resultado == esperado

    @pytest.mark.parametrize(
        "test_data", ["car#los", "@carlos", "car!los", "cart%r", "car$los"]
    )
    def test_lookup_phonebook_com_caractere_invalido(self, setUp, test_data):
        """teste lookup com caractere inválido"""
        phonebook = setUp
        phonebook.add(test_data, "333")
        resultado = phonebook.lookup(test_data)
        experado = "Nome invalido"
        assert resultado == experado

    def test_lookup_phonebook_com_nome_valido(self, setUp):
        """teste lookup com caractere inválido"""
        phonebook = setUp
        phonebook.add("Carlos", "333")
        resultado = phonebook.lookup("Carlos")
        experado = "333"
        assert resultado == experado
