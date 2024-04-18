import os

pasta = 'C:/Anlise_dados/anlise/XLS/1'
pasta_saida = 'C:/Anlise_dados/anlise/XLS/2'


if not os.path.isdir(pasta):
    print("O caminho especificado não é uma pasta válida.")
    exit()


arquivos = os.listdir(pasta)


for arquivo in arquivos:
    nome, extensao = os.path.splitext(arquivo)

    # Verifica se a extensão do arquivo é .xls
    if extensao == '.xls':
        novo_nome = nome + '.htm'
        os.rename(os.path.join(pasta, arquivo), os.path.join(pasta_saida, novo_nome))
        print(f"Arquivo {arquivo} renomeado para {novo_nome}.")
