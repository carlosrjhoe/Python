"""– Uma vez que temos uma lista contendo como elementos próprios uma série de tuplas compostas por uma categoria e por um tipo de exame de imagem, reconstrua essa base de dados em um dicionário, unificando as categorias de exames e agrupando seus subtipos.
"""

def transforma_tupla_em_dict(lista_de_tupla):
    data_dict = {}

    for especialidade, exame in data:
        data_dict.setdefault(especialidade, []).append(exame)

    return data_dict

if __name__ == '__main__':
    data = [
        ('Raios-X', 'Raios-X'),
        ('Magnetismo', 'Ressonância magnetica'),
        ('Ultrassom', 'Cintelografia'),
        ('Raios-X', 'Tomografia computadorizada'),
        ('Medicina nuclear', 'PET-CT'),
        ('Raios-X', 'Mamografia'),
        ('Raios-X', 'Densitometria Ossea'),
    ]

    print(transforma_tupla_em_dict(data))
