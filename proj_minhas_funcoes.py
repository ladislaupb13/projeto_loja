
import sqlite3 # importa a pasta SQL  para dentro do python

conexao = sqlite3.connect("sistemaVendasJunior.sqlite3")

"""A função a seguir insere clientes no banco de dados."""
def cadastrar_cliente(conexao):
    cursor = conexao.cursor() # cursor para executar comandos SQL, tanto os DML como os DDL
    nome = input("Digite o Nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    telefone = input("Digite o Telefone do cliente: ")
    endereco = input("Digite o Endereço do cliente: ")

    comando = f"""
    INSERT INTO Clientes (nome, cpf, telefone, endereco) VALUES (?, ?, ?, ?)
    """
    valores = [nome, cpf, telefone, endereco]
    cursor.execute(comando, valores)
    conexao.commit() #Atualiza a inserção de clientes em TEMPO REAL

def mostrar_clientes(conexao):
    cursor = conexao.cursor() # cursor para executar comandos SQL, tanto os DML como os DDL
    
    comando = f"""
    SELECT * FROM Clientes;
    """
    dados = cursor.execute(comando)
    for dado in dados:
        print(dado)

def add_marcas(conexao):
    cursor = conexao.cursor()

    comando = f"""INSERT INTO Marcas (nome_marca) VALUES("Fire Appareal")""" #Aqui você mesmo adicona a marca

    cursor.execute(comando)

def mostrar_marcas(conexao):
    cursor = conexao.cursor()

    comando = f"""
    SELECT * FROM Marcas;
    """
     
    marcas = cursor.execute(comando)
    for marca in marcas:
        print(marca)

def add_produtos(conexao):
    cursor = conexao.cursor()
    
    tipo = input("Qual o tipo do seu produto? ")
    preco = input("Qual o preço do seu produto? ")
    qtd_estoque = input("Quantos produtos tem no seu estoque? ")
    mostrar_marcas(conexao)
    marca_id = int(input("Digite o id da marca: "))

    
    comando = f"""INSERT INTO Produto (tipo, preco, qtd_estoque, marca_id) VALUES(?,?,?,?)"""

    valores = [tipo, preco, qtd_estoque,marca_id]

    cursor.execute(comando, valores)
    conexao.commit()

