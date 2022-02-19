from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('www.xvideos.com.br')

driver.quit() # FECHA A PAGINA