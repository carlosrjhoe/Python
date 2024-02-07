class MeuError(Exception):
    pass

def levantar():
    raise MeuError('A mensagem do meu erro')