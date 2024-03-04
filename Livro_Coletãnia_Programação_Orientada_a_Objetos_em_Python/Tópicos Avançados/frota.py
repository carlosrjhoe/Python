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

class Veiculo(ABC):
    @staticmethod
    @abstractmethod
    def chama_veiculo(num: str) -> VeiculoBase:
        pass

class Veiculo_2(Veiculo):
    @staticmethod
    def chama_veiculo(num: str) -> VeiculoBase:
        if num == '001':
            return Num001()
        if num == '002':
            return Num002()
        assert 0, 'Veiculo indisponível'

class Veiculo_3(Veiculo):
    @staticmethod
    def chama_veiculo(num: str) -> VeiculoBase:
        if num == '003':
            return Num001()
        if num == '004':
            return Num002()
        if num == '005':
            return Num002()
        assert 0, 'Veiculo indisponível'

if __name__ == "__main__":
    frota_disponivel = ['001', '002', '003', '004', '005']
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