dentro = fora = 0 

num = int(input())
for _ in range(1, num + 1):
    outro_num = int(input())
    if 10 <= outro_num <= 20:
        dentro += 1
    else:
        fora += 1
print(f'Dentro: {dentro}')
print(f'Fora: {fora}')