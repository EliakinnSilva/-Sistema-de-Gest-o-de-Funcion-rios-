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

# Função para realizar a consulta por nome
def consultar_por_nome():
    nome = entry_nome.get()
    if nome:
        conn, cursor = conectar_bd()
        cursor.execute('''SELECT * FROM funcionarios WHERE Nome LIKE ?''', ('%' + nome + '%',))
        funcionarios = cursor.fetchall()
        desconectar_bd(conn)
        mostrar_resultados(funcionarios)
    else:
        messagebox.showwarning("Campo Vazio", "Por favor, digite o nome para consultar.")

# Função para realizar a consulta por matrícula
def consultar_por_matricula():
    matricula = entry_matricula.get()
    if matricula:
        conn, cursor = conectar_bd()
        cursor.execute('''SELECT * FROM funcionarios WHERE MATRICULA = ?''', (matricula,))
        funcionarios = cursor.fetchall()
        desconectar_bd(conn)
        mostrar_resultados(funcionarios)
    else:
        messagebox.showwarning("Campo Vazio", "Por favor, digite a matrícula para consultar.")

# Função para exibir os resultados da consulta em uma nova janela
def mostrar_resultados(funcionarios):
    if not funcionarios:
        messagebox.showinfo("Sem Resultados", "Nenhum funcionário encontrado.")
        return

    root_resultados = tk.Tk()
    root_resultados.title("Resultados da Consulta")

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
        if len(funcionario) >= 6:  # Verificar se há pelo menos 6 elementos na tupla
            table.insert("", tk.END, text=funcionario[0], values=(funcionario[1], funcionario[2], funcionario[3], funcionario[4], funcionario[5]))
        else:
            messagebox.showwarning("Erro nos Dados", "Os dados do funcionário estão incompletos.")
            continue

    table.pack(padx=20, pady=20)

    root_resultados.mainloop()


# Função principal para criar a interface gráfica
def criar_interface():
    root = tk.Tk()
    root.title("Consulta de Funcionários")

    frame_consulta = ttk.Frame(root, padding="20 10")
    frame_consulta.grid(row=0, column=0, sticky="nsew")

    label_nome = ttk.Label(frame_consulta, text="Consultar por Nome:")
    label_nome.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    global entry_nome
    entry_nome = ttk.Entry(frame_consulta, width=40)
    entry_nome.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    button_consultar_nome = ttk.Button(frame_consulta, text="Consultar por Nome", command=consultar_por_nome)
    button_consultar_nome.grid(row=0, column=2, padx=5, pady=5)

    label_matricula = ttk.Label(frame_consulta, text="Consultar por Matrícula:")
    label_matricula.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    global entry_matricula
    entry_matricula = ttk.Entry(frame_consulta, width=10)
    entry_matricula.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    button_consultar_matricula = ttk.Button(frame_consulta, text="Consultar por Matrícula", command=consultar_por_matricula)
    button_consultar_matricula.grid(row=1, column=2, padx=5, pady=5)

    root.mainloop()

# Executar a interface
if __name__ == "__main__":
    criar_interface()
