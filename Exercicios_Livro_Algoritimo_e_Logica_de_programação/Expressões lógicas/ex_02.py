''' Exercício 3.6 Escreva uma expressão que será utilizada para decidir se um aluno foi
ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores
que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma
está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3. '''

materia1 = float(input('Digite a 1° nota: '))
materia2 = float(input('Digite a 2° nota: '))
materia3 = float(input('Digite a 3° nota: '))

if(materia1 >= 7 and materia2 >= 7 and materia3 >= 7):
  print("Aprovado")
else:
  print("Reprobado")
