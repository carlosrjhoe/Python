MESES = {1:'january',2: 'february',3:'march', 4:'april',5:'may',6:'june',7:'july',8:'august',9:'september',10:'october',11:'november',12:'december'}
num = int(input())
for i, j in MESES.items():
    if num == i:
        print(f'{j.title()}')