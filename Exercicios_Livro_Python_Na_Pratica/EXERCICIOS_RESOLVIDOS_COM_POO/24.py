"""Crie duas variáveis com dois valores numéricos inteiros digitados pelo usuário, caso o valor do primeiro       número for maior que o do segundo, exiba em tela uma mensagem de acordo, caso contrário, exiba em tela uma mensagem dizendo que o primeiro valor digitado é menor que o segundo:
Feltrin, Fernando. Python na Prática: Aprenda Python Através de Exercícios Comentados (p. 34). Uniorg. Edição do Kindle. """


def perguntas():
    num1 = input('Digite o 1° número: ')
    num2 = input('Digite o 2° número: ')

    if num1 > num2:
        return 'O primeiro número digitado é maior'
    else:
        return'O segundo número digitado é maior'


if __name__ == '__main__':
    print(f'{perguntas()}')