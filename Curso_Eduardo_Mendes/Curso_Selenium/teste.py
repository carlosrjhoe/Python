from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.devaprender.com')

driver.quit() # FECHA A PAGINA