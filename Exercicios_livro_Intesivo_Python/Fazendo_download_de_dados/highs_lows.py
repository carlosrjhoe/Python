import csv

file_name = "sitka_weather_07-2014.csv"
with open(file_name) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    # print(header_row)

    temperatura_maxima = []
    for i in reader:
        temperatura_maxima.append(i[1])

    print(temperatura_maxima, end="")
