file_path = "Arquivos_e_Exceções\pi_digits.txt"
with open(file_path) as file:
    lines = file.readlines()

    pi_string = ""
    for line in lines:
        pi_string += line.strip()

    print(f'{pi_string[:52]}...')
    # print(len(pi_string)) # Retorna a quantidade de caracteres

    birthday = input("Enter yout birthday, in form mmddyy: ")
    if birthday in pi_string:
        print("Your birthday appears in the first milion digits os pi!")
    else:
        print("Your birthday does not appear in the first million digits of pi.")