class Cpf:
    def __init__(self, cpf):
        self.cpf = cpf
        # self.__cpf_ = [int(n) for n in self.cpf]
    
    def validar_cpf(self) -> bool:
        if len(self.cpf) != 11:
            return False
        if self.__valida_digito(9):
            pass
        if self.__valida_digito(10):
            pass
        return True

    def __valida_digito(self, index):
        somatorio = 0
        for digito, multiplicador in zip(self.cpf[:index+1], range(index+1, 1, -1)):
            somatorio += digito * multiplicador
        dv = 11 - (somatorio % 11)
        if dv >= 10:
            dv = 0
        return dv == self.cpf[index]
            
if __name__ == "__main__":
    cpf_carlos = '06019931420'
    cpf = Cpf(cpf_carlos)
    print(cpf.validar_cpf())