import os
import pandas as pd
from io import StringIO

pasta = 'C:/Anlise_dados/anlise/XLS/2'
pasta_salva = 'C:/Anlise_dados/anlise/XLS/3'


arquivos = os.listdir(pasta)


for arquivo in arquivos:
    nome, extensao = os.path.splitext(arquivo)

    #inicio
    if extensao == '.htm':

        with open(os.path.join(pasta, arquivo), 'r', encoding='utf-8') as f:
            conteudo_html = f.read()

        #
        dados = pd.read_html(StringIO(conteudo_html))

        if dados:
            # Salva os dados em um arquivo Excel
            #novo_nome = '_'.join(nome.split(' ')[2:]) + '.xlsx'
            novo_nome = '_'.join(nome.split(' ')) + '.xlsx'
            dados[0].to_excel(os.path.join(pasta_salva, novo_nome), index=False, header=False)
            print(f"Arquivo {arquivo} convertido para {novo_nome}.")
