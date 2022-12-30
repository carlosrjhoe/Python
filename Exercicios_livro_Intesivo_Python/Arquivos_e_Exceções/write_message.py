# Se o qrquivo não exixter, esse comando irá criar no dirétorio
file_name = "Arquivos_e_Exceções\programming.txt"

with open(file_name, 'a') as file:
    file.write("\nthis is very interesting history")
