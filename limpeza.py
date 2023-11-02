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
