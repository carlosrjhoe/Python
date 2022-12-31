import matplotlib.pyplot as plt

squares = [1, 2, 4, 5, 7, 8, 12, 30, 45]
plt.plot(squares, linewidth=5)

# Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=20)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square of values", fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis="both", labelsize=14)

plt.show()