import os
import pandas as pd


def xlsx_para_csv(arquivo_xlsx, pasta_destino):
    # Carregar o arquivo XLSX
    dados = pd.read_excel(arquivo_xlsx)

    # Obter o nome do arquivo sem a extensão
    nome_arquivo = os.path.splitext(os.path.basename(arquivo_xlsx))[0]

    # Salvar os dados como arquivo CSV na pasta de destino
    arquivo_csv = os.path.join(pasta_destino, f'{nome_arquivo}.csv')
    dados.to_csv(arquivo_csv, index=False, encoding='utf-8-sig')


def converter_todos_xlsx_para_csv(pasta_origem, pasta_destino):
    # Verificar se a pasta de destino existe, senão criar
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Iterar sobre todos os arquivos na pasta de origem
    for arquivo in os.listdir(pasta_origem):
        if arquivo.endswith('.xlsx'):
            # Caminho completo do arquivo de origem
            caminho_arquivo = os.path.join(pasta_origem, arquivo)

            # Converter para CSV e salvar na pasta de destino
            xlsx_para_csv(caminho_arquivo, pasta_destino)


# Exemplo de uso:
pasta_origem = 'C:/Users/marce/OneDrive/Documents/Cidades/CsV/separados'
pasta_destino = 'C:/Users/marce/OneDrive/Documents/Cidades/CsV/separados/2'
converter_todos_xlsx_para_csv(pasta_origem, pasta_destino)
