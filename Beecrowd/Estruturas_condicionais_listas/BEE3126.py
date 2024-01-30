candidatos = int(input())
pos = neg = 0
for confirmacao in range(candidatos):
    confirmacao = input().split()
    break
for i in confirmacao:
    if i == '1':
        pos += 1
print(pos)