from repositories.mysql_repository_usuario import RepositorioUsuarioMySQL
from services.menu_usuario import Usuario

try:
    Usuario(nome = input("nome: "))
except ValueError:
    print("Erro")

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
                nome = input("Digite o nome para cadastro: ")
                Usuario.validar_nome(nome)
                email = input("Digite o email para cadastro: ")
                Usuario.validar_email(email)
                telefone = input("Digite o número de telefone para cadastro: ")
                Usuario.validar_telefone (telefone)
                cpf = input("Digite o CPF para cadastro: ")
                Usuario.validar_cpf(cpf)
                endereco = input("Digite o endereço do usuário: ")
                Usuario.validar_endereco(endereco)
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

