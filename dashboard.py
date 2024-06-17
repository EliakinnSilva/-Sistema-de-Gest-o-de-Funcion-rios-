import pandas as pd
import random
import tkinter as tk
from tkinter import messagebox
import os

# Listas de exemplo
nomes = ["João da Silva", "Maria Oliveira", "Pedro Santos", "Ana Costa", "Carlos Souza", 
         "Fernanda Lima", "Lucas Almeida", "Mariana Rocha", "José Pereira", "Patrícia Martins",
         "Ricardo Mendes", "Beatriz Gonçalves", "Paulo Ramos", "Camila Santos", "Tiago Ferreira",
         "Bruna Carvalho", "Renato Oliveira", "Juliana Araújo", "Gustavo Fernandes", "Carolina Freitas",
         "Roberto Lima", "Aline Souza", "André Silva", "Larissa Castro", "Felipe Rodrigues",
         "Vanessa Melo", "Eduardo Pinto", "Sabrina Santos", "Diego Almeida", "Letícia Costa",
         "Marcelo Barbosa", "Tatiana Lima", "Gabriel Sousa", "Renata Gomes", "Alexandre Silva",
         "Natália Monteiro", "Fábio Nogueira", "Verônica Pereira", "Bruno Almeida", "Clara Santos",
         "Rafael Ribeiro", "Bianca Costa", "Rogério Carvalho", "Fernanda Sousa", "Daniel Almeida",
         "Sofia Martins", "Victor Oliveira", "Luciana Santos", "Samuel Costa", "Gabriela Souza"]
funcoes = ["Administrador", "Vendedor", "TI", "Gerente", "Analista", "Atendente", "Supervisor", "Auxiliar"]
horarios = ["08:00 - 17:00", "09:00 - 18:00", "10:00 - 19:00", "12:00 - 21:00"]
presenca = ["Presente", "Faltou"]
status = ["Ativo", "De Férias", "De Licença", "Demitido"]

def generate_data():
    # Criação dos dados
    data_filled = {
        "MATRICULA": range(1, 51),
        "Nome": nomes,
        "Função": [random.choice(funcoes) for _ in range(50)],
        "Horário": [random.choice(horarios) for _ in range(50)],
        "Presente ou Faltou": [random.choice(presenca) for _ in range(50)],
        "Status": [random.choice(status) for _ in range(50)]
    }

    # Criação do DataFrame
    df_filled = pd.DataFrame(data_filled)

    # Definindo o caminho do arquivo para a pasta raiz do projeto
    project_root = r"C:\Users\eliak\Downloads\dashboard em py"
    file_path_filled = os.path.join(project_root, "funcionarios_com_status.xlsx")
    
    # Salvando o DataFrame no caminho especificado
    df_filled.to_excel(file_path_filled, index=False)

    # Exibindo uma mensagem de sucesso
    messagebox.showinfo("Sucesso", f"Arquivo salvo como {file_path_filled}")

    # Imprime o caminho completo do arquivo salvo
    print(f"Arquivo salvo em: {file_path_filled}")

# Criação da janela principal
root = tk.Tk()
root.title("Gerador de Dados de Funcionários")

# Define o tamanho da janela
root.geometry("300x300")

# Criação do botão
button = tk.Button(root, text="Gerar e Salvar Dados", command=generate_data)
button.pack(pady=20)

# Inicia o loop principal da interface gráfica
root.mainloop()
