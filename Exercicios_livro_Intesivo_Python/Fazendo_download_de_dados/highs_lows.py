import csv
from matplotlib import pyplot as plt

file_name = "sitka_weather_07-2014.csv"
with open(file_name) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    temperatura_maxima_em_celsius = []
    for i in reader:
        temp_highs = int(i[1])

        # Transforma temperatura fahrenheit em celsius
        temperatura_maxima_em_celsius.append((temp_highs-32)*5/9)

    # Faz a plotagem dos dados
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(temperatura_maxima_em_celsius, c="red")

    # Formatar o grafico
    plt.title("Altas temperaturas diárias, julho de 2014", fontsize=24)
    plt.xlabel("", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)
    plt.show()
    