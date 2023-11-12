import matplotlib.pyplot as plt
import dados as dado
# obtendo dados
tarifa = dado.tarifaArray
tarifaMax = tarifa.max()
tarifaMin = tarifa.min()
tarifaMedia = tarifa.mean()
# gráfico 4
categorias = ['Tarifa Máxima', 'Tarifa Miníma', 'Tarifa Média']
valores = [tarifaMax, tarifaMin, tarifaMedia]
bars = plt.bar(categorias, valores)
# adcionando valores em cima dos gráficos
plt.bar_label(bars)
# gráfico em barras verticais
plt.xlabel('Tarifas')
plt.ylabel('Valores')
plt.title('Tarifas Máxima, Mínima e Média (em libras)')
# mostrar
plt.show()
