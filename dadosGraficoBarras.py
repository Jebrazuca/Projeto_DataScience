import matplotlib.pyplot as plt

grafico = [1, 5, 8, 10, 12]
valores = [2, 4, 9, 4, 6]
titulo = 'Gráfico de barras'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(grafico, valores) #plot grafico de barras
plt.show()
