from services.menu_livro import Livro
from config.database import conectar

class RepositorioLivroMysql (Livro):
    def __init__ (self, Titulo,ISBN,Autor,Editora,AnoPublicacao,QuantidadeLivro):
        super().__init__(Titulo, ISBN, Autor, Editora, AnoPublicacao, QuantidadeLivro)
        self.conexao = conectar ()
        self.cursor = self.conexao.cursor()
    
    def cadastrar_livro (
            self,
            Titulo,
            ISBN,
            Autor,
            Editora,
            AnoPublicacao,
            QuantidadeLivro
    ):
        
        sql = """
        INSERT INTO livro (Titulo, ISBN, Autor, Editora, AnoPublicacao, QuantidadeLivro)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (Titulo, ISBN, Autor, Editora, AnoPublicacao, QuantidadeLivro)

        self.cursor.execute (sql, valores)

        self.conexao.commit()

        print (
            f"Livro {Titulo} registrado com sucesso."
        )
    
    def atualizar_livro (
            self,
            id,
            NovoTitulo,
            NovoISBN,
            NovoAutor,
            NovoEditora,
            NovoAnoPublicacao,
            NovoQuantidadeLivro
    ):
        
        sql = """
        UPDATE livro
        SET Titulo = %s,
            ISBN = %s,
            Autor = %s,
            Editora = %s,
            AnoPublicacao = %s,
            QuantidadeLivro = %s
        WHERE id = %s
        """

        valores = (
            NovoTitulo,
            NovoISBN,
            NovoAutor,
            NovoEditora,
            NovoAnoPublicacao,
            NovoQuantidadeLivro,
            id
        )

        self.cursor.execute(
            sql,
            valores
        )

        self.conexao.commit()

        if self.cursor.rowcount > 0: 
            print ("Livro atualizado com sucesso")
        else:
            print ("Livro não encontrado.")
        


    def listar_livro (self):
        sql = """SELECT id, Titulo, ISBN, Autor, Editora, AnoPublicacao, QuantidadeLivro from livro"""

        self.cursor.execute (sql)

        livros = self.cursor.fetchall()

        if len(livros) == 0:
            print ("Nenhum Livro registrado.")
        
        for id, Titulo, ISBN, Autor, Editora, AnoPublicacao, QuantidadeLivro in livros:
            print (f"ID: {id} | Título: {Titulo} | ISBN: {ISBN} | Autor: {Autor} | Editora: {Editora} | Ano de Publicação: {AnoPublicacao} | Quantidade do Livro no acervo: {QuantidadeLivro}")


    def deletar_livro (
            self,
            id
    ):

        sql = """
        DELETE FROM livro
        WHERE id = %s
        """

        valores = (id,)

        self.cursor.execute (
            sql,
            valores
        )

        if self.cursor.rowcount > 0:
            print ("Livro deletado com sucesso.")

        else:
            print ("Livro não encontrado")













#  @abstractmethod
#     def cadastrar_livro(
#         self,
#         Titulo,
#         ISBN,
#         Autor,
#         Editora,
#         AnoPublicacao,
#         QuantidadeLivro
#     ):
#         pass

#     @abstractmethod
#     def atualizar_livro (
#         self,
#         id,
#         Título,
#         ISBN,
#         Autor,
#         Editora,
#         AnoPublicacao,
#         QuantidadeLivro
#     ):
#         pass

#     @abstractmethod
#     def listar_livro (
#         self
#     ):
#         pass

#     @abstractmethod
#     def excluir_livro (
#         self,
#         id
#     ):
#         pass
        
