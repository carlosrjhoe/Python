a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(type(a))

"""União de conjuntos: A união de dois conjuntos"""
print(a.union(b))

"""Interseção de conjuntos: Único elemento em comum aos dois conjuntos"""
print(a.intersection(b))

"""Verificando se um conjunto pertence ao outro"""
print(b <= a)