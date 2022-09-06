import datetime

agora = datetime.datetime.now()

print('Data e hora atualizada')
print(f'{agora.strftime("%d-%m-%Y - %H:%M:%S")}')