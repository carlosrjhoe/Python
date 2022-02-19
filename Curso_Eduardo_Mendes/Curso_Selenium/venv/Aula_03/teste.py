from selenium.webdriver import Chrome

driver = Chrome()
driver.get('https://www.youtube.com/channel/UCia6ZLWymatyJH325kGkaCA')
driver.fullscreen_window() # Abrir em tela cheia