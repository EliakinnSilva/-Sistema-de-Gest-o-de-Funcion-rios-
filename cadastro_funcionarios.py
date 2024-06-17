import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import datetime

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
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Funcao TEXT NOT NULL,
            HorarioInicio TEXT NOT NULL,
            HorarioFim TEXT NOT NULL,
            DataAdmissao TEXT NOT NULL
        )
    ''')
    conn.commit()
    desconectar_bd(conn)

# Função para salvar um novo funcionário no banco de dados
def salvar_funcionario():
    nome = entry_nome.get()
    funcao = entry_funcao.get()
    horario_inicio = combo_inicio.get()
    horario_fim = combo_fim.get()
    data_admissao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if nome and funcao and horario_inicio and horario_fim:
        conn, cursor = conectar_bd()
        cursor.execute('''INSERT INTO funcionarios (Nome, Funcao, HorarioInicio, HorarioFim, DataAdmissao) 
                          VALUES (?, ?, ?, ?, ?)''', (nome, funcao, horario_inicio, horario_fim, data_admissao))
        conn.commit()
        desconectar_bd(conn)
        messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
        limpar_campos()
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")

# Função para limpar os campos de entrada após o cadastro
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_funcao.delete(0, tk.END)
    combo_inicio.current(0)
    combo_fim.current(0)

# Função principal para criar a interface gráfica
def criar_interface():
    root = tk.Tk()
    root.title("Cadastro de Funcionários")

    # Criar tabela funcionarios se ainda não existir
    criar_tabela_funcionarios()

    # Label e Entry para o nome do funcionário
    label_nome = tk.Label(root, text="Nome:")
    label_nome.grid(row=0, column=0, padx=10, pady=5)
    global entry_nome
    entry_nome = tk.Entry(root, width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    # Label e Entry para a função do funcionário
    label_funcao = tk.Label(root, text="Função:")
    label_funcao.grid(row=1, column=0, padx=10, pady=5)
    global entry_funcao
    entry_funcao = tk.Entry(root, width=30)
    entry_funcao.grid(row=1, column=1, padx=10, pady=5)

    # Label e ComboBox para selecionar o horário de início
    label_inicio = tk.Label(root, text="Horário de Início:")
    label_inicio.grid(row=2, column=0, padx=10, pady=5)
    global combo_inicio
    horarios = ["07:00", "08:00", "09:00", "10:00", "11:00", "12:00",
                "13:00", "14:00", "15:00", "16:00", "17:00", "18:00",
                "19:00", "20:00", "21:00","22:00"]
    combo_inicio = ttk.Combobox(root, values=horarios, width=10)
    combo_inicio.grid(row=2, column=1, padx=10, pady=5)
    combo_inicio.current(0)  # Define o valor inicial

    # Label e ComboBox para selecionar o horário de fim
    label_fim = tk.Label(root, text="Horário de Fim:")
    label_fim.grid(row=3, column=0, padx=10, pady=5)
    global combo_fim
    combo_fim = ttk.Combobox(root, values=horarios, width=10)
    combo_fim.grid(row=3, column=1, padx=10, pady=5)
    combo_fim.current(0)  # Define o valor inicial

    # Botão para cadastrar o funcionário
    button_cadastrar = tk.Button(root, text="Cadastrar Funcionário", command=salvar_funcionario)
    button_cadastrar.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()

# Executar a interface
if __name__ == "__main__":
    criar_interface()
