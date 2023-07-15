def msg(nome, *args):
    print(f'{nome} = {args}')

if __name__ == '__main__':
    ex_1 = msg('Carlos')
    ex_2 = msg('Carlos', 'idade = 37', 'profissão = Encarregado')
    