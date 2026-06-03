from repositories.repositorio import Repositorios
from datetime import datetime

class Sistema:

    def __init__(self):
        self.repositorio = Repositorios()
        self.datetime = datetime()

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
            print("10 - Atualizar empréstimo")
            print("11 - Listar empréstimos ativos") 
            print("12 - Exibir histórico de empréstimos")
            print("13 - Sair")
            opcao = input("Selecione uma opção acima: ")
            #Ainda falta colocar os métodos dentro de cada case para funcionar a criação, atualização e exclusão de itens
            match opcao:
                case "1":
                    while True:
                        try:
                            nome = input("Digite o nome do usuário: ").title()
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
                        

                                
                
                    Repositorios.atualizar_emprestimo(nome,email,cpf,telefone)

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
                        Repositorios.deletar_usuario(id)
                    
                    except ValueError:
                        print("ID inválido")
                
                case "4":
                    Repositorios.listar_usuarios()
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
                    try:
                        usuario = input("Digite o nome do usuário: ").title()
                        if usuario in Repositorios.listar_usuarios():
                            continue
                        else:
                            raise ValueError()
                    except ValueError:
                        print("Usuário não encontrado.")
                    livro = input("Digite o título do livro desejado: ")
                    try:
                        tempo_emprestimo = int(input("Digite o tempo de empréstimo: "))
                    except ValueError:
                        print("Erro o número de dias deve ser um número inteiro.")
                        return
                    data_retirada = datetime.fromisoformat(input("Digite a data inicial do empréstimo: "))
                    data_devolucao = datetime.fromisoformat(input("Digite a data de devolução: "))
                    try:
                        valor_emprestimo = float(input("Digite o valor do empréstimo: "))
                    except ValueError:
                        print("O valor não deve conter caracteres alfabéticos.")
                    
                    Repositorios.cadastrar_emprestimo(usuario,livro,tempo_emprestimo,data_retirada,data_devolucao,valor_emprestimo)
                
                case "10":
                    try:
                        id = int(input("Digite o ID do livro a atualizar: "))
                    except ValueError:
                        print("ID não encontrado.")
                    
                    #Atualizar emprestimo
                    pass

                case "11":
                    Repositorios.listar_emprestimo()
                    pass

                case "12":
                    #Histórico de empréstimos
                    break 

                case _:
                    print("Opção inválida")