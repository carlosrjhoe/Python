from abc import ABC, abstractmethod

class VeiculoBase(ABC):
    @abstractmethod
    def atender_solicitacao(self) -> None:
        pass

class Num001(VeiculoBase):
    def atender_solicitacao(self) -> None:
        print('Veículo n° 001 em deslocamento até o cliente')
        
class Num002(VeiculoBase):
    def atender_solicitacao(self) -> None:
        print('Veículo n° 002 em deslocamento até o cliente')

class Veiculo:
    def __init__(self, id):
        self.num = self.chama_veiculo(id)
        
    def chama_veiculo(num: str) -> VeiculoBase:
        if num == '001':
            return Num001()
        if num == '002':
            return Num002()
        assert 0, 'Veiculo indisponível'

    def atender_solicitacao(self):
        self.num.atender_solicitacao()

if __name__ == "__main__":
    frota_disponivel = ['001', '002']
    print(f'Veículos disponíveis: {frota_disponivel}')
    cliente_id_237 = str(input('Escolha um veículo: '))
    if cliente_id_237 == '001':
        op = Veiculo.chama_veiculo(cliente_id_237)
        op.atender_solicitacao()
    if cliente_id_237 == '002':
        op = Veiculo.chama_veiculo(cliente_id_237)
        op.atender_solicitacao()
    else:
        pass