from collections import Counter

class Verificar_letras:
    
    def __init__(self) -> None:
        texto = 'Programa irá verificar a quantidade das vogais'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        
        self.texto_a_verificar = 'A radiologia e a ciencia que estuda a anatomia por meio de radiacoes'
        
    def exibir_informacoes(self):
        a1,a2,a3,a4,a5,a6 = Counter(self.texto_a_verificar).most_common(6)
        
        print(f'Texto:\n{self.texto_a_verificar}\n')
        print(f'O elemento mais comum é: {a2[0]}, se repetem {a2[1]} vezes')
        print(f'O elemento mais comum é: {a3[0]}, se repetem {a3[1]} vezes')
        print(f'O elemento mais comum é: {a4[0]}, se repetem {a4[1]} vezes')
        print(f'O elemento mais comum é: {a5[0]}, se repetem {a5[1]} vezes')
        print(f'O elemento mais comum é: {a6[0]}, se repetem {a6[1]} vezes\n')