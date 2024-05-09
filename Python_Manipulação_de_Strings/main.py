from extrator_argumentos_url import ExtratorArgumentoUrl

url = 'moedaorigem=real&moedadestino=dolar'
# url = None

# ExtratorArgumentoUrl.url_eh_valida((url))
# print(ExtratorArgumentoUrl.url_eh_valida(url))
argumento = ExtratorArgumentoUrl(url)
moeda_origem, moeda_destino = argumento.extrair_argumento()
print(moeda_origem)
print(moeda_destino)