file_path = "Arquivos_e_Exceções\learning_python.txt"

with open(file_path) as file:
    linhas = file.readlines()
    linha_str = ""
    for line in linhas:
        linha_str += line.replace("Python", "Java")

    print(f"{linha_str}")