import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()

    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
        
else:
    print(f'HTTP error: {response.status_code}')

print(len(dados_restaurante['Pizza Hut']))