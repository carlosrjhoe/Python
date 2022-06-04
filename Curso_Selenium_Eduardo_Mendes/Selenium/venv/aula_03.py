from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'
browser = Chrome()
browser.get(url)

a = browser.find_element(by=By.TAG_NAME, value='a')
p = browser.find_element(by=By.TAG_NAME, value='p')

