import sqlite3

# Função para conectar ao banco de dados
def conectar_bd():
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()
    return conn, cursor

# Função para desconectar do banco de dados
def desconectar_bd(conn):
    conn.close()

# Função para criar a tabela funcionarios, se ainda não existir
def criar_tabela_funcionarios():
    conn, cursor = conectar_bd()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
            MATRICULA INTEGER PRIMARY KEY,
            Nome TEXT NOT NULL,
            Funcao TEXT,
            HorarioInicio TEXT,
            HorarioFim TEXT,
            DataAdmissao TEXT
        )
    ''')
    conn.commit()
    desconectar_bd(conn)

# Função principal para inicializar o banco de dados
def inicializar_banco_dados():
    criar_tabela_funcionarios()
    print("Banco de dados inicializado com sucesso.")

if __name__ == "__main__":
    inicializar_banco_dados()
