import csv

file_name = "sitka_weather_07-2014.csv"
with open(file_name) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    # print(header_row)

    for index, column_header in enumerate(header_row):
        print(f"{index} - {column_header}")