# Generated by Selenium IDE
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestUntitled():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        # self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_untitled(self):
        self.driver.get("https://clientes.sensorweb.com.br/ache/login.htm")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "user-input").click()
        self.driver.find_element(By.ID, "user-input").send_keys("klebson.luiz")
        self.driver.find_element(By.ID, "password-input").click()
        self.driver.find_element(
            By.ID, "password-input").send_keys("Ache@2026")
        self.driver.find_element(By.NAME, "Submit").click()
        self.driver.find_element(By.ID, "icon-grafic").click()

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#\\35 26 input"))
        ).click()
        
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 28 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 30 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 32 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 34 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 36 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 38 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 40 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 42 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 44 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 46 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 48 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 50 input").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#\\35 52 > td:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 52 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 54 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 56 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 58 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 60 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 62 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 64 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 66 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 68 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 70 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 72 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 74 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 76 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 78 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 80 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 82 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 84 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 86 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 88 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 90 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 92 input").click()
        self.driver.find_element(By.CSS_SELECTOR, "#\\35 94 input").click()
        self.driver.find_element(By.ID, "imageChartImg").click()
        sleep(10)