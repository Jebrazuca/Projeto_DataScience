import matplotlib.pyplot as plt

eixox = [1, 5, 8]
eixoy = [2, 4, 9]

#Titulo do grafico
plt.title('Meu primeiro gráfico com Python')

#Eixos
plt.xlabel("Eixo X")
plt.ylabel('Eixo Y')

plt.plot(eixox, eixoy) #plot grafico de linha
plt.show()
