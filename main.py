from services.menu_emprestimo import Sistema

class menu(Sistema):
    def __init__ (self):
         self.sistema = Sistema()

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
                print("9 - Registrar empréstimo")
                print("10 - Atualizar empréstimo")
                print("11 - Listar empréstimos ativos") 
                print("12 - Exibir histórico de empréstimos")
                print("13 - Sair")
                opcao = input("Selecione uma opção acima: ")
            
                match opcao:
                    case "1":
                            