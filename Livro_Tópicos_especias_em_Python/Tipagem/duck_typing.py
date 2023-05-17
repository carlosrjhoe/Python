# lista = [1,2,3,4,5,6,7,8,9,10]
# nome = 'Carlos Roberto'
# nascimento = 1985

# print(len(nome))
# print(len(lista))
# print(len(nascimento))

class Pessoa:
    def __len__(self):
        return 1985

pessoa1 = Pessoa()
print(len(pessoa1))