import json

# Carrega os dados em uma lista
file_name = 'population_data.json'
with open(file_name) as file:
    pop_data = json.load(file)

# Exibe a população de cada país em 2010
for dict_pop in pop_data:
    if dict_pop['Year'] == '2010':
        cidade = dict_pop['Country Name']
        populacao = int(float(dict_pop['Value']))
        print(f'Cidade: {cidade}, População: {populacao} pessoas.')