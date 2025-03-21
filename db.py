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
                categoria TEXT,
                subcategoria TEXT,
                email TEXT,
                nascimento TEXT,
                idade TEXT,
                cep TEXT,
                endereco TEXT,
                numero text,
                complemento text,
                bairro TEXT, 
                municipio TEXT,
                
            FOREIGN KEY(categoria) REFERENCES categoria(nome) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY(subcategoria) REFERENCES subcategoria(nome) ON UPDATE CASCADE ON DELETE CASCADE     
                )""")
        print("Tabela AGENDA criado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar Agenda!")
    
# Tabela Categoria
try:
    with con:
        cur= con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
                )""")
        print("Tabela categoria criado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar Categoria!")
    
# Tabela Subcategoria
try:
    with con:
        cur= con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS subcategoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL 
                )""")
        print("Tabela subcategoria criado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar Categoria!")
    