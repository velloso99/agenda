from imports import*
import sqlite3

# Criando conexão 
try:
    con = sqlite3.connect('database.db')
    print("Conexão com Banco de Dados efetuado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conectar com Banco de Dados!")
    
# Criando tabela do banco de dados
# Tabela Agenda
try:
    with con:
        cur= con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS agenda(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                ddd TEXT,
                contato TEXT,
                email TEXT,
                nascimento TEXT,
                idada TEXT,
                cep TEXT,
                endereco TEXT,
                numero text,
                complemento text,
                bairro TEXT, 
                municipio TEXT,
                estado TEXT,
                imagem TEXT
                )""")
        print("Tabela AGENDA criado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar Agenda!")
    