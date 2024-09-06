from datetime import datetime

data_formatada = '05-09-2024 20:31:00'
data_fmtd = '%d-%m-%Y %H:%M:%S'


def main():
    data = datetime.strptime(data_formatada, data_fmtd)
    # print(data_formatada)
    # print(data_fmtd)
    print(data)
    print(datetime.now())


if __name__ == '__main__':
    main()
