from imports import*
import sqlite3

# Criar conexão
try:
    con = sqlite3.connect('database.db')
    print("Conexão com Banco de Dados efetuado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao se conecatar ao Banco de Dados, favor verificar!")
    
# Tabela de Agenda
def criar_contato(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO agenda(nome,ddd,contato,categoria,subcategoria,email,nascimento,idade,cep,endereco,numero,complemento,bairro,municipio,imagem) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)
# Ver contato
def ver_contato():
    try:
        with con:
            cur = con.cursor()
            cur.execute('SELECT * FROM agenda')
            return cur.fetchall()
    except Exception as e:
        print(f"Erro ao buscar contatos: {e}")
        return []
def atualizar_contato(i):
    with con:
        cur = con.cursor()
        query = "UPDATE agenda SET nome=?,ddd=?,contato=?,categoria=?,subcategoria=?,email=?,nascimento=?,idade=?,cep=?,endereco=?,numero=?,complemento=?,bairro=?,municipio=?,imagem=? WHERE id=?"
        cur.execute(query, i) 
# Deletar contato
def deletar_contato(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM agenda WHERE id=?"
        cur.execute(query,i)
#***********************************************************************************************************************************************************************************************************
# Criar categoria
def criar_categoria(i):
    cur = con.cursor()
    query = "INSERT INTO categoria(nome) values(?)"
    cur.execute(query, i)
# Deletar categoria
def deletar_categoria(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM categoria WHERE id=?"
        cur.execute(query,i) 
#***********************************************************************************************************************************************************************************************************
# Criar subcategoria
def criar_subcategoria(i):
    cur = con.cursor()
    query = "INSERT INTO subcategoria(nome) values(?)"
    cur.execute(query, i)
# Deletar subcategoria
def deletar_subcategoria(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM subcategoria WHERE id=?"
        cur.execute(query,i)   