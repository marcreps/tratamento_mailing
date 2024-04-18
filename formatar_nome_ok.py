import os

pasta = 'C:/Anlise_dados/anlise/XLS/3'

arquivos = os.listdir(pasta)


for arquivo in arquivos:

    if os.path.isfile(os.path.join(pasta, arquivo)):

        nome, extensao = os.path.splitext(arquivo)

       # novo_nome = nome.replace("CEP_de", "CEP").replace("_a", "").replace("_OK_GEISA", "") + extensao
        novo_nome = nome.replace("_Unico", "") + extensao

        if novo_nome != arquivo:
            os.rename(os.path.join(pasta, arquivo), os.path.join(pasta, novo_nome))
            print(f"Arquivo renomeado: {arquivo} -> {novo_nome}")
        else:
            print(f"Arquivo {arquivo} não precisa ser renomeado.")
