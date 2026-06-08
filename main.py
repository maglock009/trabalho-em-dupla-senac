<<<<<<< HEAD
=======
from repositories.mysql_repository_usuario import RepositorioUsuarioMySQL
from services.menu_usuario import Usuario

def main():
    while True:
        print("1 - Cadastrar usuário")
        print("2 - Atualizar usuário")
        print("3 - Excluir usuário")
        print("4 - Listar usuários")
        print("5 - Sair")

        opcao = input("Selecione uma opção acima: ").strip().lower()
        match opcao:
            case "1":
                Usuario.nome = input("Digite o nome para cadastro: ")
                Usuario.email = input("Digite o email para cadastro: ")
                Usuario.telefone = input("Digite o número de telefone para cadastro: ")
                Usuario.cpf = input("Digite o CPF para cadastro: ")
                Usuario.endereco = input("Digite o endereço do usuário: ")
                RepositorioUsuarioMySQL.criar_usuario(nome, email, telefone, cpf, endereco)

            case "2":
                try: 
                    id = int(input("Digite o ID do usuário a atualizar: "))
                    nome = input("Digite o novo nome de usuário: ")
                    email = input("Digite o novo endereço de email: ")
                    telefone = input("Digite novo número de telefone: ")
                    endereco = input("Digite o novo endereço do usuário: ")
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
                print("Encerrando cadastro...")
                break

            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    main()

>>>>>>> 413aaeb074f4742d505574dc10ce4dffb6cadd01
