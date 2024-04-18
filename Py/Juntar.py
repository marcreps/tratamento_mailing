import os
import pandas as pd

# Caminho para o arquivo Excel de entrada e de saída
arquivo_entrada = 'BASE VIVO ATIVOS PARTE H_F.xlsx'
arquivo_saida = 'BASE VIVO ATIVOS PARTE H_Final.xlsx'

# Ler o arquivo Excel
df = pd.read_excel(arquivo_entrada)

# Criar um DataFrame para armazenar os resultados
novo_df = pd.DataFrame(columns=df.columns)

# Iterar sobre as linhas do DataFrame original
for index, row in df.iterrows():
    # Copiar a linha atual
    nova_linha = row.copy()
    # Criar uma nova linha com Tel_2 na linha de baixo
    nova_linha['Tel_1'] = row['Tel_2']
    nova_linha['Tel_2'] = ''
    # Adicionar as novas linhas ao novo DataFrame
    novo_df = pd.concat([novo_df, pd.DataFrame([row, nova_linha]).dropna(axis=1)], ignore_index=True)

# Apagar a coluna 'Tel_2'
novo_df.drop(columns=['Tel_2'], inplace=True)

# Verificar se Tel_1 não está vazio e não é zero e apagar as linhas correspondentes
novo_df = novo_df.dropna(subset=['Tel_1']).loc[novo_df['Tel_1'] != '']

# Salvar o DataFrame modificado em um novo arquivo Excel
novo_df.to_excel(arquivo_saida, index=False)

# Deletar o arquivo de entrada
#os.remove(arquivo_entrada)
