import pandas as pd
import psycopg2

# Função para conectar ao banco de dados PostgreSQL
def connect_to_db():
    conn = psycopg2.connect(
        dbname="nome_do_banco", 
        user="usuario", 
        password="senha", 
        host="localhost"
    )
    return conn

# Função para inserir dados no banco de dados PostgreSQL
def insert_data(conn, data):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO tabela (coluna1, coluna2, coluna3) VALUES (%s, %s, %s)", data)
        conn.commit()
        print("Dados inseridos com sucesso!")
    except psycopg2.Error as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        cursor.close()

# Ler o arquivo Excel
excel_file = "caminho/do/arquivo.xlsx"
df = pd.read_excel(excel_file)

# Conectar ao banco de dados
conn = connect_to_db()

# Iterar sobre as linhas do DataFrame e inserir no banco de dados
for index, row in df.iterrows():
    data = (row['coluna1'], row['coluna2'], row['coluna3'])  # Substitua 'coluna1', 'coluna2', 'coluna3' pelos nomes reais das colunas
    insert_data(conn, data)

# Fechar a conexão com o banco de dados
conn.close()
