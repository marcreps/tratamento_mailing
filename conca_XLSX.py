import os
import pandas as pd


def ler_xlsx_pasta_recursivamente(pasta):
    # Lista para armazenar todos os DataFrames
    dfs = []

    # Iterar sobre todos os diretórios e arquivos na pasta
    for raiz, _, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if arquivo.endswith('.xlsx'):
                caminho_arquivo = os.path.join(raiz, arquivo)
                # Ler o arquivo Excel e adicionar ao DataFrame
                df = pd.read_excel(caminho_arquivo)
                dfs.append(df)

    # Concatenar todos os DataFrames
    df_final = pd.concat(dfs, ignore_index=True)

    return df_final


def salvar_xlsx(df, pasta_destino, nome_arquivo):
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)
    df.to_excel(caminho_arquivo, index=False)


# Pasta de origem contendo arquivos .xlsx e subpastas
pasta_origem = 'C:/Anlise_dados/anlise/XLS/terminu'

# Pasta de destino para salvar o arquivo .xlsx
pasta_destino = 'C:/Anlise_dados/anlise/XLS/final'

# Ler todos os arquivos .xlsx recursivamente da pasta de origem e concatená-los
df_concatenado = ler_xlsx_pasta_recursivamente(pasta_origem)

# Nome do arquivo .xlsx a ser salvo
nome_arquivo_xlsx = 'CEPs_12_04.xlsx'

# Salvar o DataFrame concatenado como arquivo .xlsx na pasta de destino
salvar_xlsx(df_concatenado, pasta_destino, nome_arquivo_xlsx)
