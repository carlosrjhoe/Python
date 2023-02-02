import re

def procurarNumeroEmTexto(texto):
    """Pesquisa a string recebida em busca de qualquer correspondência com a regex."""
    numregex = re.compile(r"\d\d\d\d\d\d\d\d\d\d\d")
    mo = numregex.search(texto)
    print(f"Telefone encontrado: {mo.group()}")

if __name__ == "__main__":
    procurarNumeroEmTexto("Meu numero é 81995419951")
    procurarNumeroEmTexto("Meu numero é 81987949484")