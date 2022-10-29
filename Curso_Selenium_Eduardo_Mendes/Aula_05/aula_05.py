from selenium.webdriver import Chrome

url = 'http://selenium.dunossauro.live/aula_05_a.html'
driver = Chrome()
driver.get(url)
div_1 = driver.find_element_by_id()