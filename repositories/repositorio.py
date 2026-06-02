from mysql_repository_emprestimo import RepositorioMysql
from mysql_repository_usuario import RepositorioUsuarioMySQL
from mysql_repository_livro import RepositorioLivro
from config.database import conectar

class Repositorios (RepositorioUsuarioMySQL, RepositorioLivro, RepositorioMysql):
    def __init__ (self):
        self.conexao = conectar()
        self.cursor = self.conexao.cursor
