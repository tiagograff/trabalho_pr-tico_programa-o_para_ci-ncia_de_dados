import matplotlib.pyplot as plt
import numpy as np
import dados as dado
# obtendo dados
idades = dado.idadeArray
# inicializando variáveis
maiorDeIdade = 0
menorDeIdade = 0
maioresDeIdade = []
# verificar se é maior de idade
for idade in idades:
    if idade >= 18:
        maiorDeIdade += 1
    else:
        menorDeIdade += 1
# dados gráfico 5
label = ['maior de idade', 'menor de idade']
valores = [maiorDeIdade, menorDeIdade]
# juntando dados de mesmo valor e fazendo a imcrementação dos valores que se repetem
idadesUnicas, repeticoes = np.unique(idades, return_counts=True)
# criando gráficos
fig, (gr1, gr2) = plt.subplots(1, 2, figsize=(10, 5))
# inserindo dados nos gráficos
# gráfico 5
gr1.pie(valores, labels=label, shadow=True, autopct='%1.1f%%')
# gráfico 6
gr2.plot(idadesUnicas, repeticoes)
gr2.set_xlabel('idade')
gr2.set_ylabel('vezes que aparece nos dados')

plt.show()
