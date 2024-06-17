# Sistema de Gestão de Funcionários

O Sistema de Gestão de Funcionários é uma aplicação desenvolvida em Python que permite cadastrar, consultar, atualizar e excluir informações de funcionários em um ambiente corporativo.

## Funcionalidades

- **Cadastro de Funcionário**: Permite o cadastro de novos funcionários com informações como nome, função, horário de trabalho, etc.
- **Consulta de Funcionário**: Permite consultar funcionários por nome ou matrícula.
- **Atualização de Dados**: Permite atualizar informações de funcionários existentes, como função e horário de trabalho.
- **Exclusão de Funcionário**: Permite remover funcionários do sistema.
- **Consulta de Todos os Funcionários**: Permite visualizar todos os funcionários cadastrados no sistema.

## Tecnologias Utilizadas

- Python
- SQLite
- tkinter (para interface gráfica)

## Estrutura do Projeto

- `app.py`: Contém o menu principal e integra as funcionalidades.
- `cadastro_funcionarios.py`: Funcionalidade de cadastro de funcionários.
- `consulta_funcionarios.py`: Funcionalidade de consulta de funcionários.
- `atualizar_funcionarios.py`: Funcionalidade de atualização de dados de funcionários.
- `deletar_funcionarios.py`: Funcionalidade de exclusão de funcionários.
- `database.db`: Arquivo de banco de dados SQLite para armazenar informações dos funcionários.
- `requirements.txt`: Lista de dependências Python necessárias para o projeto.

## Exemplos de Uso

### Cadastro de Funcionário:

![Cadastro de Funcionário](exemplos/cadastro.png)

### Consulta de Funcionário por Nome:

![Consulta de Funcionário por Nome](exemplos/consulta.png)

### Atualização de Dados do Funcionário:

![Atualização de Dados do Funcionário](exemplos/atualizacao.png)

### Exclusão de Funcionário:

![Exclusão de Funcionário](exemplos/exclusao.png)

### Consulta de Todos os Funcionários:

![Consulta de Todos os Funcionários](exemplos/consulta_todos.png)

## Notas de Implementação

- A interface gráfica foi desenvolvida utilizando o módulo tkinter do Python para facilitar a interação do usuário.
- O banco de dados SQLite foi escolhido pela sua simplicidade e facilidade de integração com Python.
- Utilizamos o padrão MVC (Model-View-Controller) para organizar o código, separando a lógica de negócio (model) da apresentação (view) e controle (controller).

## Autor

- Eliakinn Enoque ([LinkedIn](https://www.linkedin.com/in/eliakinnenoque/))

## Contato

- Email: eliakinnenoque@gmail.com

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
