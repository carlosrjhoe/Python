n, k = input().split()
n, k = int(n), int(k)

turma = []
for _ in range(n):
    turma.append(input())
turma.sort()

print(turma[k - 1])