import os
import shutil

caminho_original = '/Users/carlo/Desktop/Neto_1'
caminho_novo = "/Users/carlo/Desktop/Neto_2"

try:
    os.mkdir(caminho_novo)
except FileExistsError as erro:
    print(f'Pasta {caminho_novo} já existe!')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if '.pdf' in file:
            shutil.move(old_file_path, new_file_path)
            print(f'Arquivo {file} copiado com sucesso.')