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

# Função para excluir um funcionário do banco de dados
def excluir_funcionario(matricula):
    conn, cursor = conectar_bd()
    cursor.execute('''DELETE FROM funcionarios WHERE MATRICULA = ?''', (matricula,))
    conn.commit()
    desconectar_bd(conn)

# Função para limpar os campos de entrada
def limpar_campos():
    entry_matricula.delete(0, tk.END)

# Função para confirmar a exclusão do funcionário
def confirmar_exclusao():
    matricula = entry_matricula.get()
    if matricula:
        funcionario = buscar_funcionario_por_id(matricula)
        if funcionario:
            resposta = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir o funcionário {funcionario[1]}?")
            if resposta:
                excluir_funcionario(matricula)
                messagebox.showinfo("Sucesso", f"Funcionário {funcionario[1]} excluído com sucesso.")
                limpar_campos()
        else:
            messagebox.showwarning("Funcionário não encontrado", f"Não há funcionário com a matrícula {matricula}.")
    else:
        messagebox.showwarning("Campo Vazio", "Por favor, digite a matrícula para excluir.")

# Função principal para criar a interface gráfica
def criar_interface():
    root = tk.Tk()
    root.title("Exclusão de Funcionário")

    frame_exclusao = ttk.Frame(root, padding="20 10")
    frame_exclusao.grid(row=0, column=0, sticky="nsew")

    label_matricula = ttk.Label(frame_exclusao, text="Matrícula do Funcionário:")
    label_matricula.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    global entry_matricula
    entry_matricula = ttk.Entry(frame_exclusao, width=10)
    entry_matricula.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    button_excluir = ttk.Button(frame_exclusao, text="Excluir Funcionário", command=confirmar_exclusao)
    button_excluir.grid(row=1, columnspan=2, padx=5, pady=10)

    root.mainloop()

# Executar a interface
if __name__ == "__main__":
    criar_interface()
