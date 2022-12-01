from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, "pt_BR.utf-8")

data = datetime.now()
mes_atual = int(data.strftime('%m'))
print(f"{mes_atual} - {mdays[mes_atual]}")

formatacao = data.strftime('%A, %d de %B de %Y')
print(f'{data}')
print(f'{formatacao}')

