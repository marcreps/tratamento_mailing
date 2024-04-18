import os
import pandas as pd

# Carregar o arquivo XLSX
dados = pd.read_excel('C:/Users/marce/OneDrive/Documents/Cidades/CsV/Mogi_Cruzes.xlsx')

# Criar uma pasta para salvar os arquivos separados
pasta_destino = 'C:/Users/marce/OneDrive/Documents/Cidades/CsV/separados'
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Iterar sobre os bairros únicos
for bairro in dados['bairro'].unique():
    # Filtrar os dados para o bairro atual
    bairro_dados = dados[dados['bairro'] == bairro]

    # Salvar os dados do bairro atual em um novo arquivo XLSX na pasta de destino
    nome_arquivo = os.path.join(pasta_destino, f'{bairro}.xlsx')
    bairro_dados.to_excel(nome_arquivo, index=False, engine='openpyxl')
