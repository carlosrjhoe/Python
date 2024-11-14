senhoras = ['Branca', 'Rosa', 'Violeta']
cores = ['branca', 'rosa', 'violeta']

for senhora in senhoras:
    for cor in cores:
        if senhora != cor:
            if senhora == 'Rosa' and cor != 'rosa':
                print(f'{senhora} está vestindo {cor}.')
            if senhora == 'Branca' and cor != 'branca':
                print(f'{senhora} está vestindo {cor}.')
            if senhora == 'Violeta' and cor != 'violeta':
                print(f'{senhora} está vestindo {cor}.')
