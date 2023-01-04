import csv
from matplotlib import pyplot as plt
from date_time import datetime

file_name = "sitka_weather_07-2014.csv"
with open(file_name) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    temperatura_maxima_em_celsius, datas = [], []
    
    for i in reader:
        temperatura_alta = int(i[1])

        # Transforma temperatura fahrenheit em celsius
        temperatura_maxima_em_celsius.append((temperatura_alta-32)*5/9)

        # Obtém as datas e as temperaturas máximas do arquivo
        data_atual = datetime.strptime(i[0], '%Y-%m-%d')
        datas.append(data_atual)

    # Faz a plotagem dos dados
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(datas, temperatura_maxima_em_celsius, c="red")

    # Formatar o grafico
    plt.title("Altas temperaturas diárias, julho de 2014", fontsize=24)
    plt.ylabel("Temperatura (°C)", fontsize=16)
    fig.autofmt_xdate()
    plt.tick_params(axis="both", which="major", labelsize=16)
    plt.show()
    