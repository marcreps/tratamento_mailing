import pandas as pd
import os

pasta_entrada = 'C:/Anlise_dados/anlise/XLS/terminu'
pasta_saida = 'C:/Anlise_dados/anlise/XLS/analise'

relatorio = {'Nome do Arquivo': [], 'Número de Linhas': []}

colunas_desejadas = ['NOME:', 'TELEFONE:', 'CPF:', 'ENDEREÇO:', 'NÚMERO:', 'COMPLEMENTO:', 'CIDADE:', 'BAIRRO:', 'UF:',
                     'CEP:', 'IDENTIFICADOR:']

arquivos = os.listdir(pasta_entrada)

for arquivo_entrada in arquivos:

    if arquivo_entrada.endswith('.xlsx'):

        caminho_arquivo_entrada = os.path.join(pasta_entrada, arquivo_entrada)

        df = pd.read_excel(caminho_arquivo_entrada)

        numero_de_linhas = df.shape[0]

        relatorio['Nome do Arquivo'].append(arquivo_entrada)
        relatorio['Número de Linhas'].append(numero_de_linhas)


df_relatorio = pd.DataFrame(relatorio)

arquivo_relatorio_saida = os.path.join(pasta_saida, 'relatorio_11_04.xlsx')

df_relatorio.to_excel(arquivo_relatorio_saida, index=False)

print(f"Relatório gerado e salvo em {arquivo_relatorio_saida}")
