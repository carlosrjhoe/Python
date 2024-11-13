class TestServiceUser:

    def test_add_user_success(self, service_user_page):
        """Teste para adicionar usuário."""
        result = service_user_page.add_user('Carlos', 'Encarregado')
        expected = 'Usuário adicionado com sucesso!'
        assert result == expected

    def test_add_user_failure(self, service_user_page):
        """Teste para verificar que o usuário adicionado já existe."""
        service_user_page.add_user('Carlos', 'Encarregado')
        result = service_user_page.add_user('Carlos', 'Encarregado')
        expected = "Erro: Usário já existe no sistema."
        assert result == expected

    def test_del_user(self, service_user_page):
        """Teste para verificar que o usuário existe para deletar."""
        service_user_page.add_user('Carlos', 'Encarregado')
        result = service_user_page.del_user('Carlos')
        expected = 'Usuário deletado com sucesso.'
        assert result == expected

    def test_update_user_success(self, service_user_page):
        """Testes para verificar se usuário exite e se foi editado."""
        service_user_page.add_user('Carlos', 'Encarregado')
        result = service_user_page.update_user('Carlos', 'Conceição')
        expected = 'Nome do usuário atualizado com sucesso.'
        assert result == expected

    def test_get_user_by_name_success(self, service_user_page):
        """Testes para verificar se existe para recuperar."""
        service_user_page.add_user('Carlos', 'Encarregado')
        result = service_user_page.get_user_by_name('Carlos')
        assert result.name == 'Carlos'
