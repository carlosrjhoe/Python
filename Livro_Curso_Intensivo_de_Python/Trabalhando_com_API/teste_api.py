import requests

# Faz uma chamada de API e armazena a resposta
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
resp = requests.get(url)
print(f'Status code: {resp.status_code}')

# Armazena a resposta da API em uma variável
response_dict = resp.json()
repositorios = response_dict['items']
repo = repositorios[0]

# Processa o resultado
# print(f'{response_dict.keys()}')
print(f'Total repositorios: {response_dict["total_count"]}')
# print(f'Keys: {len(repo)}')
# for key in sorted(repo.keys()):
#     print(f'{key}')


print("Selected information about first repository:")
for i in repositorios:
    print(f'Nome: {i["name"]}')
    print(f'Owner: {i["owner"]["login"]}')
    print(f'Stars: {i["stargazers_count"]}')
    print(f'Repository: {i["html_url"]}')
    print(f'Created: {i["created_at"]}')
    print(f'Updated: {i["updated_at"]}')
    print(f'Description: {i["description"]}')
    print(f'########################################################################################')