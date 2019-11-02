import matplotlib.pyplot as plt

grafico1 = [1, 3, 5, 7, 9]
valores1 = [2, 3, 7, 1, 2]

grafico2 = [2, 4, 6, 8, 10]
valores2 = [5, 1, 3, 7, 4]

titulo = 'Gráfico de barras 2'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(grafico1, valores1, label = 'Grupo 1') #plot grafico de barras
plt.bar(grafico2, valores2, label = 'Grupo 2')
plt.legend()
plt.show()

