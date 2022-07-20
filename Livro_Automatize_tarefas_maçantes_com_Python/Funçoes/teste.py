""" A primeira linha contém uma instrução def u que define uma função
chamada hello(). O código no bloco após a instrução def v é o corpo da
função. Esse código é executado quando a função é chamada, e não quando
ela é inicialmente definida """

# def hello(name):
#   print(f'Olá, {name}')

# hello('Carlos')
# hello('Mayara')
# hello('Neto')
# hello('Luna')

""" Valores de retorno e instruções return """

# print('Hello!', end=" ")
# print('World')

# print('gatos', 'cachorro', 'ratos', sep=",")
# print('gatos', 'cachorro', 'ratos')

""" Escopo local e global """

# def span():
#   eggs = 3241

# span()

def spam():
  global eggs
eggs = 'spam' # essa é a variável global

def bacon():
  eggs = 'bacon' # essa é uma variável local
  
def ham():
  print(eggs) # essa é a variável global
  
eggs = 42 # essa é a variável global
spam()
print(eggs)