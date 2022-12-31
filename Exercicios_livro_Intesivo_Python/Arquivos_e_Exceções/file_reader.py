file_path = "pi_digits.txt"
with open(file_path) as file:
    # contents = file.read() # Para ler todo contúdo do arquivo TXT
    # for line in file: # Para ler linha por linha do arquivo TXT
    lines = file.readlines() # Para transformar a linha por lista do arquivo TXT
    for line in lines:
        print(f"{line.strip()}")
