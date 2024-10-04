from selenium.webdriver import Chrome

driver = Chrome()
url_saucedemo = 'https://www.saucedemo.com/'
driver.get(url_saucedemo)

titulo = driver.title
print(f'Titulo do site: {titulo}')

url = driver.current_url
print(f'URL do site: {url}')

codigo_fonte = driver.page_source
print(f'Codigo fonte do site: {codigo_fonte}')
