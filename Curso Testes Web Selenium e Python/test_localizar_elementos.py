# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By

# driver = Chrome()
# URL_SAUCEDEMO = 'https://www.saucedemo.com/'
# driver.get(URL_SAUCEDEMO)

# user_name = driver.find_element(By.ID, 'user-name')
# password = driver.find_element(By.ID, 'password')
# botao = driver.find_element(By.ID, 'login-button')

# # print(user_name.is_displayed())

# user_name.send_keys('standard_user')
# password.send_keys('secret_sauce')
# botao.click()

# elem_products = driver.find_element(By.XPATH, "//span[@class='title']")
# assert elem_products.text == 'Products'

# img_backpack = driver.find_element(
#     By.XPATH, "(//img[@class='inventory_item_img'])[1]")
# print(img_backpack.get_attribute('alt'))
# assert img_backpack.get_attribute('alt') == 'Sauce Labs Backpack'
