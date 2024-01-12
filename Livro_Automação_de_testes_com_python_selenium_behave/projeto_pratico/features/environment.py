from selenium.webdriver import Chrome
from behave import given, when, then
from po.Google import Google

def before_all(context):
    context.driver = Chrome()
    context.google = Google(context.driver)

def after_step(context, step):
    pass

def after_all(context):
    pass