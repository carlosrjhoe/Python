# conftest.py
from pytest import fixture
from selenium.webdriver import Chrome


@fixture
def setUp():
    # Inicializa o WebDriver (neste caso, o Chrome)
    driver = Chrome()
    # Opcional: Maximiza a janela do navegador
    driver.maximize_window()
    # `yield` passa o driver para o teste e, após o teste, executa o código de limpeza
    yield driver
    # Fecha o navegador ao final do teste
    driver.quit()
