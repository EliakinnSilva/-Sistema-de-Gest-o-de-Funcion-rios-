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

# Função para buscar dados de um funcionário pelo ID
def buscar_funcionario_por_id(id):
    conn, cursor = conectar_bd()
    cursor.execute('''SELECT * FROM funcionarios WHERE MATRICULA = ?''', (id,))
    funcionario = cursor.fetchone()
    desconectar_bd(conn)
    return funcionario

# Função para atualizar dados de um funcionário
def atualizar_funcionario(matricula, nome, funcao, horario_inicio, horario_fim, data_admissao):
    conn, cursor = conectar_bd()
    cursor.execute('''
        UPDATE funcionarios
        SET Nome = ?, Funcao = ?, HorarioInicio = ?, HorarioFim = ?, DataAdmissao = ?
        WHERE MATRICULA = ?
    ''', (nome, funcao, horario_inicio, horario_fim, data_admissao, matricula))
    conn.commit()
    desconectar_bd(conn)

# Função para limpar os campos de entrada
def limpar_campos():
    entry_matricula.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_funcao.delete(0, tk.END)
    entry_horario_inicio.delete(0, tk.END)
    entry_horario_fim.delete(0, tk.END)
    entry_data_admissao.delete(0, tk.END)

# Função para carregar os dados do funcionário selecionado
def carregar_funcionario():
    matricula = entry_matricula.get()
    if matricula:
        funcionario = buscar_funcionario_por_id(matricula)
        if funcionario:
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, funcionario[1])
            entry_funcao.delete(0, tk.END)
            entry_funcao.insert(0, funcionario[2])
            entry_horario_inicio.delete(0, tk.END)
            entry_horario_inicio.insert(0, funcionario[3])
            entry_horario_fim.delete(0, tk.END)
            entry_horario_fim.insert(0, funcionario[4])
            entry_data_admissao.delete(0, tk.END)
            entry_data_admissao.insert(0, funcionario[5])
        else:
            messagebox.showwarning("Funcionário não encontrado", f"Não há funcionário com a matrícula {matricula}.")
    else:
        messagebox.showwarning("Campo Vazio", "Por favor, digite a matrícula para buscar.")

# Função para salvar as alterações do funcionário
def salvar_atualizacao():
    matricula = entry_matricula.get()
    nome = entry_nome.get()
    funcao = entry_funcao.get()
    horario_inicio = entry_horario_inicio.get()
    horario_fim = entry_horario_fim.get()
    data_admissao = entry_data_admissao.get()

    if matricula and nome and funcao and horario_inicio and horario_fim and data_admissao:
        atualizar_funcionario(matricula, nome, funcao, horario_inicio, horario_fim, data_admissao)
        messagebox.showinfo("Sucesso", "Dados do funcionário atualizados com sucesso.")
        limpar_campos()
    else:
        messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")

# Função principal para criar a interface gráfica
def criar_interface():
    root = tk.Tk()
    root.title("Atualização de Funcionário")

    frame_atualizacao = ttk.Frame(root, padding="20 10")
    frame_atualizacao.grid(row=0, column=0, sticky="nsew")

    label_matricula = ttk.Label(frame_atualizacao, text="Matrícula:")
    label_matricula.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    global entry_matricula
    entry_matricula = ttk.Entry(frame_atualizacao, width=10)
    entry_matricula.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    button_buscar = ttk.Button(frame_atualizacao, text="Buscar", command=carregar_funcionario)
    button_buscar.grid(row=0, column=2, padx=5, pady=5)

    label_nome = ttk.Label(frame_atualizacao, text="Nome:")
    label_nome.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    global entry_nome
    entry_nome = ttk.Entry(frame_atualizacao, width=40)
    entry_nome.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="w")

    label_funcao = ttk.Label(frame_atualizacao, text="Função:")
    label_funcao.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    global entry_funcao
    entry_funcao = ttk.Entry(frame_atualizacao, width=40)
    entry_funcao.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="w")

    label_horario_inicio = ttk.Label(frame_atualizacao, text="Horário Início:")
    label_horario_inicio.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    global entry_horario_inicio
    entry_horario_inicio = ttk.Entry(frame_atualizacao, width=15)
    entry_horario_inicio.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    label_horario_fim = ttk.Label(frame_atualizacao, text="Horário Fim:")
    label_horario_fim.grid(row=3, column=2, padx=5, pady=5, sticky="e")
    global entry_horario_fim
    entry_horario_fim = ttk.Entry(frame_atualizacao, width=15)
    entry_horario_fim.grid(row=3, column=3, padx=5, pady=5, sticky="w")

    label_data_admissao = ttk.Label(frame_atualizacao, text="Data Admissão:")
    label_data_admissao.grid(row=4, column=0, padx=5, pady=5, sticky="e")
    global entry_data_admissao
    entry_data_admissao = ttk.Entry(frame_atualizacao, width=15)
    entry_data_admissao.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    button_atualizar = ttk.Button(frame_atualizacao, text="Salvar Atualização", command=salvar_atualizacao)
    button_atualizar.grid(row=5, columnspan=4, padx=5, pady=10)

    root.mainloop()

# Executar a interface
if __name__ == "__main__":
    criar_interface()
