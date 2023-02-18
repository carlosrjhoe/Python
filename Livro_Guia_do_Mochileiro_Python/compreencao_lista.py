# A compreensão de lista é mais clara
a = [1,2,3,4,5,6,7,8,9,10]
b = [i for i in a if i <= 5]
c = [i for i in a if i > 5]
# Ou:
d = filter(lambda x: x > 4, a)

print(f'{a}')
print(f'{b}')
print(f'{c}')
