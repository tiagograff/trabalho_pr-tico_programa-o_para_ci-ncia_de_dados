import matplotlib.pyplot as plt
import numpy as np
import dados as dado
# Obtenção dos dados
classe1 = dado.sobreviventesClasse1
classe2 = dado.sobreviventesClasse2
classe3 = dado.sobreviventesClasse3
# Contagem de sobreviventes por classe
sobreviventes1 = np.sum(classe1 == 0)
sobreviventes2 = np.sum(classe2 == 0)
sobreviventes3 = np.sum(classe3 == 0)
print(sobreviventes1, sobreviventes2, sobreviventes3)
# gráfico 09
label = ['classe 1', 'classe 2', 'classe 3']
valores = [sobreviventes1, sobreviventes2, sobreviventes3]
# adiconando valores na parte de cima das barras do gráfico
bars = plt.bar(label, valores)
# adicionando valores sobre as barras
plt.bar_label(bars)
plt.title('sobreviventes por classe')
# mostrando gráfico
plt.show()
