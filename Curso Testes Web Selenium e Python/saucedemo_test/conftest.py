from pytest import fixture
from selenium.webdriver import Chrome


# Decorador faz com o que a função seja realizada antes e depois dos testes.
@fixture
def webdriver():
    """Iniciar o driver do Chrome"""
    driver = Chrome()
    driver.maximize_window()
    # retorna o driver para o teste e, após o término do teste, fecha o navegador.
    yield driver
    # para fechar o navegador.
    driver.quit()
