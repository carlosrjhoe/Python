class Blibioteca:
    
    def __init__(self, livro1, **kwargs):
        self.livro1 = livro1
        
        
pratileira1 = Blibioteca('LIVRO TESTE')
pratileira1.livro2 = 'duna - frank herbert'
pratileira1.livro3 = '1985 - gorge orwell'
pratileira1.livro4 = '1990 pawer rapratileira'

print(pratileira1.livro1)
print(pratileira1.livro2)
print(pratileira1.livro3)