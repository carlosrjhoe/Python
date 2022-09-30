from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('carlos')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

print(escritor.get_nome)
print(caneta.get_marca)
maquina.escrever()

escritor._ferramenta = maquina
escritor._ferramenta.escrever()
