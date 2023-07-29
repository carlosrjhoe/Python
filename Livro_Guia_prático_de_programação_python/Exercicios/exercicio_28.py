inteiros = []
def intervalo_numeros():
    for num in range(num_inicio, num_final+1):
        inteiros.append(num)
    return inteiros
    
if __name__ == "__main__":
    num_inicio = int(input('Qual é o primeiro número? '))
    num_final = int(input('Qual é o segundo número? '))
    print(intervalo_numeros())