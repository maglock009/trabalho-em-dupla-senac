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
                    try:
                        nome = input("Digite o nome para cadastro: ")
                        email = input("Digite o email para cadastro: ")
                        telefone = input("Digite o número de telefone para cadastro: ")
                        cpf = input("Digite o CPF para cadastro: ")
                        endereco = input("Digite o endereço do usuário: ")
                        
                        usuario = Usuario (nome,email,telefone,cpf,endereco)
                        
                        repositorio = RepositorioUsuarioMySQL()
                        
                        repositorio.criar_usuario(
                            usuario.nome, 
                            usuario.email, 
                            usuario.telefone, 
                            usuario.cpf, 
                            usuario.endereco
                        )
                    except ValueError as erro:
                        print (erro)

            case "2":
                try: 
                    id = int(input("Digite o ID do usuário a atualizar: "))
                    nome = input("Digite o novo nome do usuário: ")
                    cpf = input ("Digite o novo CPF do usuário")
                    email = input("Digite o novo endereço de email: ")
                    telefone = input("Digite novo número de telefone: ")
                    endereco = input("Digite o novo endereço do usuário: ")
                    
                    usuario = Usuario (nome,email,telefone,cpf,endereco)
                   
                    repositorio = RepositorioUsuarioMySQL()
                    
                    repositorio.atualizar_usuario(
                        id,
                        usuario.nome, 
                        usuario.email, 
                        usuario.telefone, 
                        usuario.cpf, 
                        usuario.endereco
                    )
                except ValueError as erro:
                    print(erro)
            
            case "3":
                try:
                    id = int(input("Digite o ID do usuário a excluir: "))

                    if id <= 0:
                        raise ValueError ("ID inválido.")
                    
                    repositorio = RepositorioUsuarioMySQL()

                    repositorio.deletar_usuario(id)
                    
                except ValueError as erro:
                    print(erro)
            
            case "4":
                repositorio = RepositorioUsuarioMySQL()
                repositorio.listar_usuarios()

            case "5":
                try:
                    Titulo = input("Digite o título do livro: ")
                    ISBN = input("Defina o código ISBN do livro: ")
                    Autor = input("Digite o nome do autor do livro: ")
                    Editora = input("Digite o nome da editora responsável pela publicação: ")
                    AnoPublicacao = input("Digite o ano em que o livro foi publicado: ")
                    QuantidadeLivro = input("Digite a quantidade de exemplares disponíveis: ")

                    livro = Livro (Titulo, ISBN, Autor, Editora, AnoPublicacao, QuantidadeLivro)

                    repositorio = RepositorioLivroMysql()

                    repositorio.cadastrar_livro(livro.Titulo, livro.ISBN, livro.Autor, livro.Editora, livro.AnoPublicacao, livro.QuantidadeLivro)

                except ValueError as erro:
                    print (erro)
            
            case "6":
                try:
                    id = int(input("Digite o ID do livro a atualizar: "))
                    Titulo = input("Digite o novo título do livro: ")
                    ISBN = input("Digite o novo código ISBN do livro: ")
                    Autor = input("Digite o nome do novo autor: ")
                    Editora = input("Digite o nome da nova editora responsável pela publicação: ")
                    AnoPublicacao = input("Digite o novo ano de publicação do livro: ")
                    QuantidadeLivro = input("Digite a nova quantidade de exemplares: ")

                    livro = Livro (Titulo, ISBN, Autor, Editora, AnoPublicacao, QuantidadeLivro)

                    repositorio = RepositorioLivroMysql()

                    repositorio.atualizar_livro(
                        id, 
                        livro.Titulo, 
                        livro.ISBN, 
                        livro.Autor, 
                        livro.Editora, 
                        livro.AnoPublicacao, 
                        livro.QuantidadeLivro
                    )

                except ValueError as erro:
                    print(erro)
            
            case "7":
                try:
                    id = int(input("Digite o ID do livro a excluir: "))

                    if id <= 0:
                        raise ValueError("ID inválido.")
                    
                    repositorio = RepositorioLivroMysql()

                    repositorio.deletar_livro(id)

                except ValueError as erro:
                    print(erro)
            
            case "8":
                repositorio = RepositorioLivroMysql()
                repositorio.listar_livro()
            
            case "9":
                try:
                    id_usuario = int(input("Digite o ID do usuário que deseja realizar um empréstimo: "))
                    id_livro = int(input("Digite o ID do livro que o usuário deseja:"))
                    
                    if id_usuario <= 0 or id_livro <= 0: 
                        raise ValueError ("ID inválido.")

                    TempoEmprestimo = input("Digite o tempo de empréstimo do livro: ")
                    DataRetirada = input("Digite a data de retirada do empréstimo: ")
                    DataDevolucao = input("Digite a data de devolução do empréstimo: ")
                    ValorEmprestimo = input("Digite o valor do empréstimo: ")
        
                    emprestimo = Emprestimo (
                        TempoEmprestimo, 
                        DataRetirada, 
                        DataDevolucao, 
                        ValorEmprestimo
                    )

                    repositorio = RepositorioMysql()

                    repositorio.cadastrar_emprestimo(
                        id_usuario,
                        id_livro,
                        emprestimo.TempoEmprestimo,
                        emprestimo.DataRetirada,
                        emprestimo.DataDevolucao,
                        emprestimo.ValorEmprestimo
                    )
                
                except ValueError as erro:
                    print(erro)
            
            case "10":
                try:
                    id = int(input("Digite o ID do empréstimo a atualizar: "))
                    id_usuario = int(input("Digite o ID do novo usuário: "))
                    id_livro = int(input("Digite o ID do novo livro: "))
                    TempoEmprestimo = int(input("Digite o tempo de empréstimo do livro: "))
                    DataRetirada = input("Digite a data de retirada do empréstimo: ")
                    DataDevolucao = input("Digite a data de devolução do empréstimo: ")
                    ValorEmprestimo = input("Digite o valor do empréstimo: ")

                    emprestimo = Emprestimo (
                        TempoEmprestimo, 
                        DataRetirada, 
                        DataDevolucao, 
                        ValorEmprestimo
                    )

                    repositorio = RepositorioMysql()

                    repositorio.atualizar_emprestimo(
                        id,
                        id_usuario,
                        id_livro,
                        emprestimo.TempoEmprestimo,
                        emprestimo.DataRetirada,
                        emprestimo.DataDevolucao,
                        emprestimo.ValorEmprestimo
                    )

                except ValueError as erro:
                    print(erro)
        
            case "11":
                try:
                    id = int(input("Digite o ID do empréstimo a excluir: "))

                    if id <= 0:
                        raise ValueError("ID inválido.")

                    repositorio = RepositorioMysql()

                    repositorio.deletar_emprestimo(id)

                except ValueError as erro:
                    print(erro)
            
            case "12":
                repositorio = RepositorioMysql()
                repositorio.listar_emprestimo()
            
            case "13":
                print("Encerrando sistema...")
                break

            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    main()

