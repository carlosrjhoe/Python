"""Vejamos um exemplo dos dois casos:"""
EMPRESA = "Unidos Venceremos Ltda"

def variavel_global():
    print(EMPRESA)
    print("-" * len(EMPRESA))
    
def variavel_local(nome):
    print(nome)
    print("-" * len(nome))

variavel_global()
variavel_local('Carlos Roberto Conceição Junior')