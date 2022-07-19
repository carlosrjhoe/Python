def spam(numero):
    return 42 / numero
  
try:
  print(spam(2))
  print(spam(12))
  print(spam(0))
  print(spam(1))
except ZeroDivisionError:
  print('Error: Invalid argument.')
