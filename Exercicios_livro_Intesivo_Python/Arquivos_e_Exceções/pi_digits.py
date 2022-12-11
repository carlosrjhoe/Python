file_path = "Arquivos_e_Exceções\pi_digits.txt"
with open(file_path) as file:
    lines = file.readlines()

    pi_string = ""
    for line in lines:
        pi_string += line.strip()

    print(f'{pi_string}')
    print(len(pi_string))