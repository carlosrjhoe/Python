a=[3,4,5]

# b = [i for i in a if i>4]
# print(b)

"""Compeensão com lambda"""
b = filter(lambda x: x > 4, a)

print(f"{b}")