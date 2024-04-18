import pandas as pd
import os


pasta_entrada = 'C:/Anlise_dados/anlise/XLS/3'
pasta_saida = 'C:/Anlise_dados/anlise/XLS/terminu'
colunas_desejadas = ['NOME:', 'TELEFONE:', 'CPF:', 'ENDEREÇO:', 'NÚMERO:', 'COMPLEMENTO:', 'CIDADE:', 'BAIRRO:', 'UF:',
                     'CEP:', 'IDENTIFICADOR:']
arquivos = os.listdir(pasta_entrada)

for arquivo_entrada in arquivos:
    if arquivo_entrada.endswith('.xlsx'):

        caminho_arquivo_entrada = os.path.join(pasta_entrada, arquivo_entrada)

        nome_arquivo_saida = arquivo_entrada

        caminho_arquivo_saida = os.path.join(pasta_saida, nome_arquivo_saida)

        df = pd.read_excel(caminho_arquivo_entrada)
        nome_sem_extensao = os.path.splitext(arquivo_entrada)[0]
        numero_de_linhas = df.shape[0]

        for coluna in colunas_desejadas:
            if coluna not in df.columns:
                df[coluna] = None

        novo_df = df[colunas_desejadas]

        #novo_df.loc[:, 'NÚMERO:'] = novo_df['NÚMERO:'].astype(str)

        #novo_df['END:'] = novo_df['ENDEREÇO:'] + ' , ' + novo_df['NÚMERO:']

        #novo_df.drop(['ENDEREÇO:', 'NÚMERO:'], axis=1, inplace=True)

        novo_df = novo_df[['NOME:', 'TELEFONE:', 'CPF:', 'ENDEREÇO:','NÚMERO:', 'COMPLEMENTO:', 'CIDADE:', 'BAIRRO:', 'UF:', 'CEP:',
                           'IDENTIFICADOR:']]

        novo_df['IDENTIFICADOR:'] = nome_sem_extensao
        #novo_df['IDENTIFICADOR:'] = arquivo_entrada.split('_')[-1].split('.')[0]

        novo_df.to_excel(caminho_arquivo_saida, index=False)

        print(f"Arquivo {arquivo_entrada} processado e salvo em {caminho_arquivo_saida}")
