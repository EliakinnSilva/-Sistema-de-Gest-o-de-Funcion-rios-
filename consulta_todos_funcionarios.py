import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Função para conectar ao banco de dados
def conectar_bd():
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()
    return conn, cursor

# Função para desconectar do banco de dados
def desconectar_bd(conn):
    conn.close()

# Função para buscar todos os funcionários no banco de dados
def buscar_todos_funcionarios():
    conn, cursor = conectar_bd()
    cursor.execute('''SELECT * FROM funcionarios''')
    funcionarios = cursor.fetchall()
    desconectar_bd(conn)
    return funcionarios

# Função para exibir todos os funcionários em uma nova janela
def mostrar_todos_funcionarios():
    funcionarios = buscar_todos_funcionarios()
    if funcionarios:
        root_resultados = tk.Tk()
        root_resultados.title("Todos os Funcionários")

        # Criar uma tabela para mostrar os resultados
        table = ttk.Treeview(root_resultados, columns=("MATRÍCULA", "Nome", "Função", "Horário", "Presença ou Falta", "Status"))
        table.heading("#0", text="ID")
        table.heading("MATRÍCULA", text="MATRÍCULA")
        table.heading("Nome", text="Nome")
        table.heading("Função", text="Função")
        table.heading("Horário", text="Horário")
        table.heading("Presença ou Falta", text="Presença ou Falta")
        table.heading("Status", text="Status")

        for funcionario in funcionarios:
            table.insert("", tk.END, text=funcionario[0], values=(funcionario[1], funcionario[2], funcionario[3], funcionario[4], funcionario[5]))

        table.pack(padx=20, pady=20)

        root_resultados.mainloop()
    else:
        messagebox.showinfo("Sem Funcionários", "Não há funcionários cadastrados.")

# Função principal para criar a interface gráfica
def criar_interface():
    root = tk.Tk()
    root.title("Consulta de Todos os Funcionários")

    frame_consulta = ttk.Frame(root, padding="20 10")
    frame_consulta.grid(row=0, column=0, sticky="nsew")

    button_consultar = ttk.Button(frame_consulta, text="Consultar Todos os Funcionários", command=mostrar_todos_funcionarios)
    button_consultar.grid(row=0, column=0, padx=5, pady=5)

    root.mainloop()

# Executar a interface
if __name__ == "__main__":
    criar_interface()
