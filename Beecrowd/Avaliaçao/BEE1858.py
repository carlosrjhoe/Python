num = int(input())
vezes = input().split()
for i in range(num):
    vezes[i] = int(vezes[i])
num_minimo = min(vezes)
print(vezes.index(num_minimo)+1)