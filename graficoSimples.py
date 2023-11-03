import matplotlib.pyplot as plt
import dados as dado
# dados para o gráfico
labelsGenero = ['Homens', 'Mulheres']
sizesGenero = [dado.homens, dado.mulheres]
colorsGenero = ['blue', 'pink']
explodeGenero = (0, 0)
#
labelsSobreviventes = ['Sobreviventes', 'Mortos']
sizesSobreviventes = [dado.sobreviventes, dado.mortos]
colorsSobreviventes = ['blue', 'pink']
explodeSobreviventes = (0, 0)
# criando mais de um gráfico
fig, (gr1, gr2, gr3) = plt.subplots(1, 3, figsize=(10, 10))
# colocando os dados no gráfico 'pizza'
gr1.pie(sizesGenero, colors=colorsGenero, explode=explodeGenero,
        labels=labelsGenero, autopct='%1.1f%%')
gr1.set_title('Homens x Mulheres')
# arredondar o gráfico
gr1.axis('equal')
# gráfico2
gr2.pie(sizesSobreviventes, colors=colorsSobreviventes, explode=explodeSobreviventes,
        labels=labelsSobreviventes, autopct='%1.1f%%')
gr2.set_title('Sobreviventes')
# arredondar o gráfico
gr2.axis('equal')
# gráfico 3
categarias = ['Classe 1', 'Classe 2', 'Classe 3']
valores = [dado.primeiraClasse, dado.segundaClasse, dado.terceiraClasse]
# gráfico em barras verticais
gr3.bar(categarias, valores)
gr3.set_xlabel('Categorias')
gr3.set_ylabel('Valores')
gr3.set_title('Tripulantes por Classe')
# mostrar os gráficos
plt.show()
