from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

url = 'https://curso-python-selenium.netlify.app/aula_03.html'
driver.get(url)

a = driver.find_element_by_tag_name('a')
p = driver.find_element_by_tag_name('p')