import re

class Telefones:
    
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Numero incorreto.")
    
    def valida_telefone(self, telefone):
        padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
        respota = re.findall(padrao, telefone)
        if respota:
            return True
        else:
            return False
