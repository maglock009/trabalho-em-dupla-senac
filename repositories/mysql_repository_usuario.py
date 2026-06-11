from config.database import conectar
from interfaces.repositorio_usuario import RepositorioUsuario
from services.menu_usuario import Usuario

class RepositorioUsuarioMySQL(Usuario):
    def __init__(self):
        self.conexao = conectar()
        self.cursor = self.conexao.cursor()


    def criar_usuario(self,nome,email,telefone,cpf,endereco):

        sql = """INSERT INTO usuarios (Nome,Email,Telefone,CPF,Endereco)
        VALUES (%s,%s,%s,%s,%s)
        """

        valores = (nome, email, telefone, cpf, endereco)

        self.cursor.execute(sql,valores)

        self.conexao.commit()

        print(
            f"Usuário {nome} "
            f"criado com sucesso."
        )

    def listar_usuarios(self):

        sql = "SELECT idUsuarios, nome, email, telefone, cpf, endereco FROM usuarios"

        self.cursor.execute(sql)

        usuarios = self.cursor.fetchall()

        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
            return

        for id, nome, email, telefone, cpf, endereco in usuarios:
            print(f"ID: {id} | Nome: {nome} | Email: {email} | Telefone: {telefone} | CPF: {cpf} | Endereço: {endereco}")

    def atualizar_usuario(
        self,
        id,
        novo_nome,
        novo_email,
        novo_telefone,
        novo_endereco
    ):

        sql = """
        UPDATE usuarios
        SET nome = %s,
            email = %s,
            telefone = %s,
            endereco = %s
        WHERE idUsuarios = %s
        """

        valores = (
            novo_nome,
            novo_email,
            novo_telefone,
            novo_endereco,
            id
        )

        self.cursor.execute(
            sql,
            valores
        )

        self.conexao.commit()

        if self.cursor.rowcount > 0:

            print(
                "Usuário atualizado "
                "com sucesso."
            )

        else:

            print(
                "Usuário não encontrado."
            )

    def deletar_usuario(self, id):

        sql = """
        DELETE FROM usuarios
        WHERE idUsuarios = %s
        """

        valores = (id,)

        self.cursor.execute(
            sql,
            valores
        )

        self.conexao.commit()

        if self.cursor.rowcount > 0:

            print(
                "Usuário deletado "
                "com sucesso."
            )

        else:

            print(
                "Usuário não encontrado."
            )
