class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return self.name

def ordem_alfabetica(pessoa):
    return pessoa.name

def ordem_idade(age):
    return age.age

if __name__ == "__main__":
    pessoa_01 = Pessoa('carlos', 38)
    pessoa_02 = Pessoa('mayara', 39)
    pessoa_03 = Pessoa('neto', 8)

pessoas = [pessoa_01, pessoa_02, pessoa_03]
print(sorted(pessoas, key = ordem_alfabetica))
print(sorted(pessoas, key = ordem_idade))
print(sorted(pessoas, key = ordem_idade, reverse=True))