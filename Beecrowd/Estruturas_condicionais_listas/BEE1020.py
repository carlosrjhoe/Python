idade_dias = int(input())
anos = int(idade_dias / 365)
meses = int((idade_dias % 365) / 30)
dias = int((idade_dias % 365) % 30)
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')