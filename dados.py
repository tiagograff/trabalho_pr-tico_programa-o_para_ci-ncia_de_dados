import pandas as pd

dataFrame = pd.read_csv(
    'faculdade/trabalho_pratico_programa-o_para_ciencia_de_dados/titanic.csv')
# removendo coluna 'Name' porque não será utilizada
dataFrame.drop(columns=['Name'], inplace=True)
# criando uma nova coluna chamada Family Aboard que é a soma das colunas Siblings/Spouses Aboard e Parents/Children Aboard
dataFrame['FamilyAboard'] = dataFrame['Siblings/Spouses Aboard'] + \
    dataFrame['Parents/Children Aboard']
# removendo as colunas antigas que foram somadas
dataFrame.drop(columns=['Siblings/Spouses Aboard',
               'Parents/Children Aboard'], inplace=True)
# salvando em outro arquivo csv. limpo = tratado e removendo o index criado pelo próprio pandas
dataFrame.to_csv(
    'faculdade/trabalho_pratico_programa-o_para_ciencia_de_dados/limpo.csv', index=False)
# dados primários
# total de passageitos
totalPassageiros = dataFrame.shape[0]
print(totalPassageiros)
# quantos sobreviventes tiveram
sobreviventes = dataFrame['Survived'].value_counts()[0]
# array sobreviventes
arraySobreviventes = dataFrame['Survived'].to_numpy()
# quantos morreram
mortos = dataFrame['Survived'].value_counts()[1]
# quantos homens
homens = dataFrame['Sex'].value_counts()['male']
# quantas mulheres
mulheres = dataFrame['Sex'].value_counts()['female']
# primeira classe
primeiraClasse = dataFrame['Pclass'].value_counts()[1]
# segunda classe
segundaClasse = dataFrame['Pclass'].value_counts()[2]
# terceira classe
terceiraClasse = dataFrame['Pclass'].value_counts()[3]
# array com as tarifas
tarifaArray = dataFrame['Fare'].to_numpy()
# array com as idades
idadeArray = dataFrame['Age'].to_numpy()
# arrar com quantidade de familiares
familiaresArray = dataFrame['FamilyAboard'].to_numpy()
