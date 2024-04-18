import pandas as pd
import os

# Caminho para o arquivo Excel de entrada e de saída
arquivo_entrada = 'CEP_07072.xlsx'
arquivo_saida = arquivo_entrada
nome_arquivo = os.path.basename(arquivo_entrada)
nome_sem_extensao = os.path.splitext(nome_arquivo)[0]

# Especificar as colunas que você deseja manter
colunas_desejadas = ['NOME:','TELEFONE:', 'CPF:','ENDEREÇO:','NÚMERO:','COMPLEMENTO:','CIDADE:','BAIRRO:', 'UF:','CEP:', 'IDENTIFICADOR:']

# Ler o arquivo Excel
df = pd.read_excel(arquivo_entrada)
# Obter o número de linhas do DataFrame
numero_de_linhas = df.shape[0]

print(nome_sem_extensao, ";", numero_de_linhas)


# Verificar se todas as colunas desejadas existem no DataFrame
for coluna in colunas_desejadas:
    if coluna not in df.columns:
        # Se a coluna não existir, cria ela com valores nulos
        df[coluna] = None

# Pegar apenas as colunas desejadas de todas as linhas
novo_df = df[colunas_desejadas]

# Converter a coluna 'NUN' para string antes de concatenar
novo_df.loc[:, 'NÚMERO:'] = novo_df['NÚMERO:'].astype(str)


# Concatenar as colunas 'END' e 'NUN' e armazenar em uma nova coluna 'END_NUN'
novo_df['END:'] = novo_df['ENDEREÇO:'] + ' , ' + novo_df['NÚMERO:']


# Remover as colunas 'END' e 'NUN'
novo_df.drop(['ENDEREÇO:', 'NÚMERO:'], axis=1, inplace=True)

# Reorganizar as colunas
novo_df = novo_df[['NOME:', 'TELEFONE:', 'CPF:', 'END:', 'COMPLEMENTO:', 'CIDADE:', 'BAIRRO:', 'UF:', 'CEP:', 'IDENTIFICADOR:']]

novo_df['IDENTIFICADOR:'] = nome_sem_extensao


# Salvar o DataFrame modificado em um novo arquivo Excel
novo_df.to_excel(arquivo_saida, index=False)
