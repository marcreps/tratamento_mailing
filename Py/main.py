import os
import pandas as pd

# Caminho para o arquivo Excel de entrada e de saída
arquivo_entrada = 'Cancelados 0602.xlsx'
arquivo_saida = 'Formatado.xlsx'

# Especificar as colunas que você deseja manter
colunas_desejadas = ['Nome', 'CPF', 'Telefone', 'Tel_2', 'Endereco', 'Complemento', 'Bairro', 'CEP', 'Cidade', 'UF', 'identificador']

# Ler o arquivo Excel
df = pd.read_excel(arquivo_entrada)

# Pegar apenas as colunas desejadas de todas as linhas
novo_df = df[colunas_desejadas]

# Criar um novo DataFrame para armazenar os resultados
novo_df_final = pd.DataFrame(columns=novo_df.columns)

# Iterar sobre as linhas do DataFrame original
for index, row in novo_df.iterrows():
    # Copiar a linha atual
    nova_linha = row.copy()
    # Criar uma nova linha com Tel_2 na linha de baixo
    nova_linha['Telefone'] = row['Tel_2']
    nova_linha['Tel_2'] = ''
    # Adicionar as novas linhas ao novo DataFrame final
    novo_df_final = pd.concat([novo_df_final, pd.DataFrame([row, nova_linha]).dropna(axis=1)], ignore_index=True)

# Apagar a coluna 'Tel_2'
novo_df_final.drop(columns=['Tel_2'], inplace=True)

# Verificar se Tel_1 é diferente de zero e não é vazio e apagar as linhas correspondentes
novo_df_final = novo_df_final.dropna(subset=['Telefone']).loc[novo_df_final['Telefone'] != 0]

# Verificar e remover linhas duplicadas na coluna 'Telefone', mantendo apenas a primeira ocorrência
novo_df_final.drop_duplicates(subset=['Telefone'], keep='first', inplace=True)

# Salvar o DataFrame modificado em um novo arquivo Excel
novo_df_final.to_excel(arquivo_saida, index=False)

# Deletar o arquivo de entrada
#os.remove(arquivo_entrada)
