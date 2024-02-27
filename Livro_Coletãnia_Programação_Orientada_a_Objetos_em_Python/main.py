# from basesedados import BaseDeDados
from usuario import Usuario, Identificador

usuario1 = Usuario('carlos')
identificador1 = Identificador('0001')

usuario1.logar = identificador1
usuario1.logar.logar()