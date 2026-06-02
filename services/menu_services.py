from repositories.repositorio import Repositorios

class Sistema:

    def __init__(self):
        self.repositorio = Repositorios()

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
                    while True:
                        try:
                            nome = input("Digite o nome do usuário: ")
                            if nome.isdigit():
                                raise ValueError
                            else:
                                break
                        except ValueError:
                            print("Nome inválido.")
                    
                        @staticmethod
                        def validar_email(email):
                            return "@" in email and "." in email
                        
                        email = input("Digite o email para cadastro: ")
                        if validar_email(email):
                            pass
                        else:
                            return
                        
                        while True:
                            try:
                                telefone = int(input("Digite o número de telefone para cadastro: "))
                                if len(telefone) == 11:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Formato de número de telefone inválido.")

                        while True:
                            try:
                                cpf = int(input("Digite o CPF para cadastro: "))
                                if len(cpf) == 11:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Formato de CPF inválido.")
                        
                        endereco = input("Digite o endereço do usuário: ")
                            
                        Repositorios.cadastrar_usuario(nome,email,telefone,cpf,endereco)
                        

                                
                
                case "2":
                    try:
                        id = int(input("ID do usuário a atualizar: "))

                    except ValueError:
                        print("ID inválido")

                    try:
                        nome = input("Digite o novo nome do usuário: ")
                        if nome.isdigit():
                            raise ValueError
                    except ValueError:
                        print("O nome digitado é inválido.")
                    
                    
                    @staticmethod 
                    def validar_email(email):
                        return "@" in email and "." in email
                    email = input("Digite o novo email do usuário: ")
                    if not validar_email(email):
                        return
                    
                    try:
                        telefone = int(input("Digite o novo número de telefone do usuário: "))
                        if len(telefone) != 11:
                            raise ValueError
                    except ValueError:
                        print("Formato de número de telefone inválido.")
                    
                    endereco = input("Digite o nome do novo endereço do usuário: ")
                    Repositorios.atualizar_usuario(id, nome, email, telefone, endereco)
                    
                        
                
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