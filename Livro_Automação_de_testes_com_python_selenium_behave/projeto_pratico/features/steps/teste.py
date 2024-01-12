from behave import given, when, then
from selenium.webdriver import Chrome

driver = Chrome()
titulo = 'Google'

@given(u'que acesso a página enicial do google')
def step_impl(context):
    driver.get('https://google.com.br')


@when(u'estou na página')
def step_impl(context):
    assert titulo in driver.title


@then(u'a página deve ser fechada')
def step_impl(context):
    driver.quit()