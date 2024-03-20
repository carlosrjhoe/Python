class Veiculo:

    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self) -> str:
        return f'Marca: {self.marca} - {self.modelo} - {self._ligado}'


class Carro(Veiculo):
    
    def __init__(self, marca, modelo, portas) -> None:
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self) -> str:
        super().__str__()
        status = 'Ligado' if self._ligado else 'Desligado'
        return f'{self.marca} - {self.modelo} - Portas: {self.portas} - status: {status}'


class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo) -> None:
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self) -> str:
        super().__str__()
        status = 'Ligado' if self._ligado else 'Desligado'
        return f'{self.marca} - {self.modelo} - Tipo: {self.tipo} - status: {status}'
        

if __name__ == "__main__":
    veiculo_01 = Carro('Toyota', 'Corolla', 4)
    moto_01 = Moto('Honda', 'CB 500', 'Casual')
    print(veiculo_01)
    print(moto_01)