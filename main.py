from repositories.mysql_repository_usuario import RepositorioUsuarioMySQL
from repositories.mysql_repository_livro import RepositorioLivroMysql
from repositories.mysql_repository_emprestimo import RepositorioMysql
from services.menu_usuario import Usuario
from services.menu_livro import Livro
from services.menu_emprestimo import Emprestimo

def main():
    
    while True:
        print("1 - Cadastrar usuário")
        print("2 - Atualizar usuário")
        print("3 - Excluir usuário")
        print("4 - Listar usuários")
        print("5 - Cadastrar livro")
        print("6 - Atualizar livro")
        print("7 - Excluir livro")
        print("8 - Listar livros")
        print("9 - Registrar empréstimo")
        print("10 - Atualizar empréstimo")
        print("11 - Excluir empréstimo")
        print("12 - Listar empréstimos")
        print("13 - Sair")

        opcao = input("Selecione uma opção acima: ").strip().lower()
        match opcao:
            case "1":
                nome = input("Digite o nome para cadastro: ")
                Usuario.validar_nome(nome)
                email = input("Digite o email para cadastro: ")
                Usuario.validar_email(email)
                telefone = input("Digite o número de telefone para cadastro: ")
                Usuario.validar_telefone (telefone)
                cpf = input("Digite o CPF para cadastro: ")
                #Usuario.validar_cpf(cpf)
                endereco = input("Digite o endereço do usuário: ")
                
                repositorio = RepositorioUsuarioMySQL(nome, email, telefone, cpf, endereco)

                repositorio.criar_usuario(nome, email, telefone, cpf, endereco)

            case "2":
                try: 
                    id = int(input("Digite o ID do usuário a atualizar: "))
                    nome = input("Digite o novo nome de usuário: ")
                    Usuario.validar_nome(nome)
                    email = input("Digite o novo endereço de email: ")
                    Usuario.validar_email(email)
                    telefone = input("Digite novo número de telefone: ")
                    Usuario.validar_telefone(telefone)
                    endereco = input("Digite o novo endereço do usuário: ")
                    Usuario.validar_endereco(endereco)
                    RepositorioUsuarioMySQL.atualizar_usuario(id, nome, email, telefone, endereco)
                except ValueError:
                    print("ID inválido.")
            
            case "3":
                try:
                    id = int(input("Digite o ID do usuário a excluir: "))
                    RepositorioUsuarioMySQL.deletar_usuario(id)
                except ValueError:
                    print("ID inválido.")
            
            case "4":
                RepositorioUsuarioMySQL.listar_usuarios()

            case "5":
                Titulo = input("Digite o título do livro: ")
                Livro.validar_titulo(Titulo)
                ISBN = input("Defina o código ISBN do livro: ")
                Livro.validar_isbn(ISBN)
                Autor = input("Digite o nome do autor do livro: ")
                Livro.validar_autor(Autor)
                Editora = input("Digite o nome da editora responsável pela publicação: ")
                Livro.validar_editora(Editora)
                AnoPublicacao = input("Digite o ano em que o livro foi publicado: ")
                Livro.validar_ano_publicacao(AnoPublicacao)
                QuantidadeLivro = input("Digite a quantidade de exemplares disponíveis: ")
                Livro.validar_quantidade(QuantidadeLivro)
                RepositorioLivroMysql.cadastrar_livro(Titulo, ISBN, Autor, Editora, AnoPublicacao, QuantidadeLivro)
            
            case "6":
                try:
                    id = int(input("Digite o ID do livro a atualizar: "))
                    Titulo = input("Digite o novo título do livro: ")
                    Livro.validar_titulo(Titulo)
                    ISBN = input("Digite o novo código ISBN do livro: ")
                    Livro.validar_isbn(ISBN)
                    Autor = input("Digite o nome do novo autor: ")
                    Livro.validar_autor(Autor)
                    Editora = input("Digite o nome da nova editora responsável pela publicação: ")
                    Livro.validar_editora(Editora)
                    AnoPublicacao = input("Digite o novo ano de publicação do livro: ")
                    Livro.validar_ano_publicacao(AnoPublicacao)
                    QuantidadeLivro = input("Digite a nova quantidade de exemplares: ")
                    Livro.validar_quantidade(QuantidadeLivro)
                    RepositorioLivroMysql.atualizar_livro(id, Titulo, ISBN, Autor, Editora, AnoPublicacao, QuantidadeLivro)
                except ValueError:
                    print("ID inválido")
            
            case "7":
                try:
                    id = int(input("Digite o ID do livro a excluir: "))
                    RepositorioLivroMysql.deletar_livro(id)
                except ValueError:
                    print("ID inválido.")
            
            case "8":
                RepositorioLivroMysql.listar_livro()
            
            case "9":
                TempoEmprestimo = input("Digite o tempo de empréstimo do livro: ")
                Emprestimo.validar_data(TempoEmprestimo)
                DataRetirada = input("Digite a data de retirada do empréstimo: ")
                Emprestimo.validar_data(DataRetirada)
                DataDevolucao = input("Digite a data de devolução do empréstimo: ")
                Emprestimo.validar_data(DataDevolucao)
                ValorEmprestimo = input("Digite o valor do empréstimo: ")
                Emprestimo.validar_valor_emprestimo(ValorEmprestimo)
                RepositorioMysql.cadastrar_emprestimo(TempoEmprestimo,DataRetirada,DataDevolucao,ValorEmprestimo)
            
            case "10":
                try:
                    id = int(input("Digite o ID do empréstimo a atualizar: "))
                    TempoEmprestimo = input("Digite o tempo de empréstimo do livro: ")
                    Emprestimo.validar_data(TempoEmprestimo)
                    DataRetirada = input("Digite a data de retirada do empréstimo: ")
                    Emprestimo.validar_data(DataRetirada)
                    DataDevolucao = input("Digite a data de devolução do empréstimo: ")
                    Emprestimo.validar_data(DataDevolucao)
                    ValorEmprestimo = input("Digite o valor do empréstimo: ")
                    Emprestimo.validar_valor_emprestimo(ValorEmprestimo)
                    RepositorioMysql.atualizar_emprestimo(TempoEmprestimo,DataRetirada,DataDevolucao,ValorEmprestimo)
                except ValueError:
                    print("ID inválido")
        
            case "11":
                try:
                    id = int(input("Digite o ID do empréstimo a excluir: "))
                    RepositorioMysql.deletar_emprestimo(id)
                except ValueError:
                    print("ID inválido")
            
            case "12":
                RepositorioMysql.listar_emprestimo()
            
            case "13":
                print("Encerrando sistema...")
                break

            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    main()

