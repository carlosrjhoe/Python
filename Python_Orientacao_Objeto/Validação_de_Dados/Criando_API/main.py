import requests
from acesso_cep import BuscaEndereco

cep = 54515110
objeto_cep = BuscaEndereco(cep)
r = requests.get('https://viacep.com.br/ws/54515110/json/')

'''Para acessarmos essas informações'''
uf, localidade, cep, bairro, logradouro, complemento = objeto_cep.acessa_via_cep()
print(f'\nEstado: {localidade} \nCidade: {uf} \nBairro: {bairro} \nAv/Rua: {logradouro} \nNúmero: {complemento}')

'''
    Nesta aula, vimos:

    O que são requisições HTTP;
    Para que serve e como acessar uma API;
    Como utilizar a biblioteca requests do Python;
    Acessar a API do ViaCEP e retornar informações do endereço a partir do CEP.
    
'''
