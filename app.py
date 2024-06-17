import tkinter as tk
from tkinter import ttk
import cadastro_funcionarios
import consulta_funcionarios
import consulta_todos_funcionarios
import atualizar_funcionarios
import deletar_funcionarios 

# Função para abrir a janela de cadastro de funcionários
def abrir_cadastro():
    cadastro_funcionarios.criar_interface()

# Função para abrir a janela de consulta de funcionários
def abrir_consulta():
    consulta_funcionarios.criar_interface()

# Função para abrir a janela de consulta de todos os funcionários
def abrir_consulta_todos():
    consulta_todos_funcionarios.criar_interface()

# Função para abrir a janela de atualização de funcionários
def abrir_atualizacao():
    atualizar_funcionarios.criar_interface()

# Função para abrir a janela de exclusão de funcionários
def abrir_exclusao():
    deletar_funcionarios.criar_interface()

# Função principal para criar a interface do menu
def criar_menu():
    root = tk.Tk()
    root.title("Menu Principal")

    frame_menu = ttk.Frame(root, padding="20 10")
    frame_menu.grid(row=0, column=0, sticky="nsew")

    button_cadastro = ttk.Button(frame_menu, text="Cadastrar Funcionário", command=abrir_cadastro)
    button_cadastro.grid(row=0, column=0, padx=10, pady=5)

    button_consulta = ttk.Button(frame_menu, text="Consultar Funcionário", command=abrir_consulta)
    button_consulta.grid(row=1, column=0, padx=10, pady=5)

    button_consulta_todos = ttk.Button(frame_menu, text="Consultar Todos os Funcionários", command=abrir_consulta_todos)
    button_consulta_todos.grid(row=2, column=0, padx=10, pady=5)

    button_atualizacao = ttk.Button(frame_menu, text="Atualizar Funcionário", command=abrir_atualizacao)
    button_atualizacao.grid(row=3, column=0, padx=10, pady=5)

    button_exclusao = ttk.Button(frame_menu, text="Excluir Funcionário", command=abrir_exclusao)
    button_exclusao.grid(row=4, column=0, padx=10, pady=5)

    root.mainloop()

# Executar o menu principal
if __name__ == "__main__":
    criar_menu()
