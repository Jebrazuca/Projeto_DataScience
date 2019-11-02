# Crescimento da população Brasileira 1980-2016
# DataSus

import matplotlib.pyplot as plt
dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linhas = dados[i].split(';')
        x.append(int(linhas[0]))
        y.append(int(linhas[1]))

plt.plot(x, y, color='#006400', linestyle='-.')
plt.bar(x, y, color='#FAFAD2')

plt.title("Crescimento da população Brasileira 1980-2016")
plt.xlabel('Ano')
plt.ylabel('População x100.000.000')

plt.show()
#plt.savefig('dados_populacao.png', dpi=300)
