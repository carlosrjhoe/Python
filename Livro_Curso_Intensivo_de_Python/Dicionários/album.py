"""8.7 – Álbum: Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
artista e o título de um álbum e deve devolver um dicionário contendo essas duas
informações. Use a função para criar três dicionários que representem álbuns
diferentes. Apresente cada valor devolvido para mostrar que os dicionários estão
armazenando as informações do álbum corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar o
número de faixas em um álbum. Se a linha que fizer a chamada incluir um valor
para o número de faixas, acrescente esse valor ao dicionário do álbum. Faça pelo
menos uma nova chamada da função incluindo o número de faixas em um álbum."""

def album_musical(artista, album):
    album_do_artista = {'Artista': artista, 'Álbum': album}
    return album_do_artista

print(album_musical('carlos', 'Novo mundo'))