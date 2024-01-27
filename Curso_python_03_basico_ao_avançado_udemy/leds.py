leds = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6,}
num = int(input())
for _ in range(num):
    outro_num = input()
    cont = 0
    for caractere in outro_num:
        cont += leds[caractere]
    print(f'{cont} leds')