from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time


class Buscar_mesas:
    def __init__(self):
        self.site_link = 'https://www.casasbahia.com.br/?utm_source=gp_branding&utm_medium=cpc&utm_campaign=gg_brd_inst_cb_exata&gclid=Cj0KCQiAveebBhD_ARIsAFaAvrGCBWxlAT-MOVtUCIaa6b3kMSWmes1zd1NtGLzIzp7d33f4heZCurYaAvI8EALw_wcB'
        self.site_map = {
            'botão': {
                'mesas': {
                    'xpath': '//*[@id="strBusca"]'
                }
            }
        }
        self.driver = Chrome(executable_path='chromedriver.exe')
        self.driver.maximize_window()

    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.site_link)
        time.sleep(10)
        

    def clicar_no_buscar(self):
        self.driver.find_element(By.XPATH, self.site_map['botão']['mesas']['xpath']).click()

    def name(self):
        pass

    def name(self):
        pass

if __name__ == '__main__':
    mesa = Buscar_mesas()
    mesa.abrir_site()
    mesa.clicar_no_buscar()