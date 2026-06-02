from interfaces.repositorio_livro import RepositorioLivro
from config.database import conectar

class RepositorioLivroMysql:
    def __init__ (self):
        self.conexao = conectar ()
        self.cursor = self.conexao.cursor()
    
    
