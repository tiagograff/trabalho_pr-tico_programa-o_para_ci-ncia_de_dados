import matplotlib.pyplot as plt
import numpy as np
import dados as dado
# buscando dados
familiares = dado.familiaresArray
sobreviventes = dado.arraySobreviventes
# inicializando variáveis
temFamiliares = []
naoTemFamiliares = []
sobreviventesSemFamiliares = 0
sobreviventesComFamiliares = 0
# percorrendo familiares (array) para saber quais tem e quais não tem familiares
for i in range(len(familiares)):
    familia = familiares[i]
    if familia == 0:
        naoTemFamiliares.append(familia)
        # caso sobreviveu e não tinha familiares
        if sobreviventes[i] == 0:
            sobreviventesSemFamiliares += 1
    else:
        temFamiliares.append(familia)
        # caso sobreiveu e tinha familiares
        if sobreviventes[i] == 0:
            sobreviventesComFamiliares += 1
# tamanho dos arrays com/sem familiares
nroNaoTemFamiliares = np.size(naoTemFamiliares)
nroTemFamiliares = np.size(temFamiliares)
# grafico 7
label1 = ['possui familiares', 'não possui familiares']
valores1 = [nroTemFamiliares, nroNaoTemFamiliares]
# grafico 8
label2 = ['sobreviventes com familiares', 'sobreviventes sem familiares']
valores2 = [sobreviventesComFamiliares, sobreviventesSemFamiliares]
# montando gráficos
fig, (gr1, gr2) = plt.subplots(1, 2, figsize=(10, 5))
# monstando gráfico 7
gr1.pie(valores1, labels=label1, autopct='%1.1f%%')
# montando gráfico 8
gr2.pie(valores2, labels=label2, autopct='%1.1f%%')
# mostrando gráficos
plt.show()
