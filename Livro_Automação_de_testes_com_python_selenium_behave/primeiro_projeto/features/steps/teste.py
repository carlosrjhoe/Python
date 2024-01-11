from behave import given, when, then
from selenium.webdriver import Chrome

driver = Chrome()
url = 'https://www.google.com/'
titulo_site = 'Chrome'

@given(u'que acesso a página inicial do google')
def acessar_pagina(context):
    driver.get(url)

@when(u'estou na página')
def verificar_titulo(context):
    assert titulo_site in driver.title

@then(u'pagina deve ser fechada')
def fechar_pagina(context):
    driver.quit()