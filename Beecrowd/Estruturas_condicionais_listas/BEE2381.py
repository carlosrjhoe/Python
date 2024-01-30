x, y = [int(x) for x in input().split()]
turma = []
for _ in range(x):
    turma.append(input())
turma.sort()
print(turma[y - 1])