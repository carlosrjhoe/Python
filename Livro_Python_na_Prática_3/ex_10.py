"""10 – Crie um decorador que imprima a frase "Antes da função" antes de executar a função decorada e "Depois da função" após executá-la. Aplique o decorador a uma função simples a testando em seguida:"""

def msg_decorator(funcao):
    def msg():
        print('[1]-Antes da função.')
        funcao()
        print('[3]-Depois da função.')
    return msg

@msg_decorator
def minha_funcao():
    print('[2]-Execuntando minha função.') 

if __name__ == '__main__':
    minha_funcao()