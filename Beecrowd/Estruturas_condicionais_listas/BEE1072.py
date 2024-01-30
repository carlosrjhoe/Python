num = int(input())
inn = out = 0
for _ in range(num):
    outro_num = int(input())
    if 10 <= outro_num <= 20:
        inn += 1
    else:
        out += 1
print(f'{inn} in')
print(f'{out} out')