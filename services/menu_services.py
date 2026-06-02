from repositories.repositorio import Repositorios

class Sistema:

    def __init__(self, repositorio):
        self.repositorio = repositorio

    def menu(self):
        while True:
            print("1 - Cadastrar usuário")
            print("2 - Atualizar usuário")
            print("3 - Excluir usuário")
            print("4 - Listar usuários")
            print("5 - Cadastrar novo livro")
            print("6 - Atualizar informações do livro")
            print("7 - Excluir livros cadastrados")
            print("8 - Listar livros disponíveis")
            print("9 - Resgistrar empréstimo")
            print("10 - Listar empréstimos ativos")
            print("11 - Exibir histórico de empréstimos")
            print("12 - Sair")
            opcao = input("Selecione uma opção acima: ")
            #Ainda falta colocar os métodos dentro de cada case para funcionar a criação, atualização e exclusão de itens
            match opcao:
                case "1":
                    nome = input("Nome: ")
                    email = input("CPF: ")
                    cpf = input("CPF: ")
                    telefone = input("Telefone: ")
                
                case "2":
                    try:
                        id = int(input("ID do usuário a atualizar: "))

                        nome = input("Novo nome: ")

                        email = input("Novo email: ")

                        telefone = input("Novo contato de telefone: ")
                    except ValueError:
                        print("ID inválido")
                
                case "3":
                    try:
                        id = int(input("Digite o ID do usuário a deletar: "))
                    
                    except ValueError:
                        print("ID inválido")
                
                case "4":
                    #Case para listar usuários cadastrados
                    pass
                
                case "5":
                    titulo = input("Título: ")
                    autor = input("Autor: ")
                    editora = input("Editora: ")
                    ano_publicacao = input("Ano de publicação: ")
                    quantidade = input("Quantidade: ")
                    isbn = input("ISBN: ")
                
                case "6":
                    try:
                        id = int(input("Digite o ID do livro a atualizar: "))
                        titulo = input("Novo título: ")
                        quantidade = input("Nova quantidade: ")
                    except ValueError:
                        print("ID inválido.")
                    
                case "7":
                    try:
                        id = int(input("Digite o ID do livro a excluir: "))
                    except ValueError:
                        print("ID Inválido")
                
                case "8":
                    #Listar livros cadastrados
                    pass
                    
                case "9":
                    titulo = input("Digite o título do livro que busca: ")
                    #Adicionar método para realizar empréstimo
                
                case "10":
                    #Listar empréstimos ativos
                    pass

                case "11":
                    #Exibir histórico de empréstimos
                    pass

                case "12":
                    print("Encerrando sistema...")
                    break 

                case _:
                    print("Opção inválida")