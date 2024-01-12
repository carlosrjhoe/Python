class Google:

    def __init__(self, driver):
        self.driver = driver

    def homepage(self):
        self.driver.get('http://www.google.com.br')

    def valid_title(self, titulo):
        assert titulo in self.driver.title