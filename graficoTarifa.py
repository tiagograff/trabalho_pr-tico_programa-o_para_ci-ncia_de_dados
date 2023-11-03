import matplotlib.pyplot as plt
import dados as dado
# obtendo dados
tarifa = dado.tarifaArray
tarifa_max = tarifa.max()
tarifa_min = tarifa.min()
tarifa_media = tarifa.mean()
# gráfico 4
categorias = ['Tarifa Máxima', 'Tarifa Miníma', 'Tarifa Média']
valores = [tarifa_max, tarifa_min, tarifa_media]
# gráfico em barras verticais
plt.bar(categorias, valores)
plt.xlabel('Tarifas')
plt.ylabel('Valores')
plt.title('Tarifas Máxima, Mínima e Média (em libras)')
# mostrar
plt.show()
