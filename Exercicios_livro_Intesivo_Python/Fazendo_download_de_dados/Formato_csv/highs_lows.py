import csv
from matplotlib import pyplot as plt
from date_time import datetime

file_name = "death_valley_2014.csv"
with open(file_name) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    temperatura_maxima_em_celsius, temperatura_minima_em_celsius, datas = [], [], []
    
    for i in reader:
        try:
            # Obtém as datas e as temperaturas máximas do arquivo
            data_atual = datetime.strptime(i[0], '%Y-%m-%d')
            
            temperatura_alta = int(i[1])
            temperatura_baixa = int(i[3])
        except ValueError:
            print(data_atual, "falta de dados")
        else:
            datas.append(data_atual)
            # Transforma temperatura fahrenheit em celsius e pegando temperatura alta e baixa
            temperatura_maxima_em_celsius.append((temperatura_alta-32)*5/9)
            temperatura_minima_em_celsius.append((temperatura_baixa-32)*5/9)


    # Faz a plotagem dos dados
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(datas, temperatura_maxima_em_celsius, c="red", alpha=0.5)
    plt.plot(datas, temperatura_minima_em_celsius, c="blue", alpha=0.5)
    plt.fill_between(datas, temperatura_maxima_em_celsius, temperatura_minima_em_celsius, facecolor="blue", alpha=0.1)

    # Formatar o grafico
    plt.title("Temperaturas máximas e mínimas diárias - 2014\nDeath Valley, CA", fontsize=20)
    plt.ylabel("Temperatura (°C)", fontsize=16)
    fig.autofmt_xdate()
    plt.tick_params(axis="both", which="major", labelsize=16)
    plt.show()
    