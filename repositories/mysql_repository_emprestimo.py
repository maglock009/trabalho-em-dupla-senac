from services.menu_emprestimo import Emprestimo
from config.database import conectar

class RepositorioMysql (Emprestimo):
    def __init__ (self):
        self.conexao = conectar()
        self.cursor = self.conexao.cursor()
    
    def cadastrar_emprestimo (
            self,
            usuario,
            livro,
            tempo_emprestimo,
            data_retirada,
            data_devolucao,
            valor_emprestimo
    ):
        sql = """ INSERT INTO emprestimos (Usuarios_idUsuarios, livros_idlivros, TempoEmprestimo, DataRetirada, DataDevolucao, ValorEmprestimo)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = usuario, livro, tempo_emprestimo, data_retirada, data_devolucao, valor_emprestimo

        self.cursor.execute(sql, valores)
        self.conexao.commit()

        print (
            f"Empréstimo do livro {livro} feito pelo usuário {usuario} no valor RS {valor_emprestimo} com sucesso."
        )
    
    def atualizar_emprestimo (
            self,
            id,
            novo_usuario,
            novo_livro,
            novo_tempo_emprestimo,
            novo_data_retirada,
            novo_data_devolucao,
            novo_valor_emprestimo
    ):
        
        sql = """
        UPDATE emprestimos
        SET Usuarios_idUsuarios = %s,
            livros_idlivros = %s,
            tempo_emprestimo = %s,
            data_retirada = %s,
            data_devolucao = %s,
            valor_emprestimo = %s
        WHERE idEmprestimos = %s
        """

        valores = (
            novo_usuario,
            novo_livro,
            novo_tempo_emprestimo,
            novo_data_retirada,
            novo_data_devolucao,
            novo_valor_emprestimo,
            id
        )

        self.cursor.execute(sql,valores)

        self.conexao.commit()
        if self.cursor.rowcount > 0:
            print(
                "Empréstimo atualizado" 
                "com sucesso"
            )
        else:
            print (
                "Empréstimo não encontrado" 
            )

    def listar_emprestimo (self):
        sql = """SELECT idEmprestimos, Usuarios_idUsuarios, livros_idlivros, TempoEmprestimo, DataRetirada, DataDevolucao, ValorEmprestimo FROM emprestimos"""

        self.cursor.execute(sql)

        emprestimo = self.cursor.fetchall()

        if len(emprestimo) == 0:
            print (
                "Nenhum empréstimo registrado ainda."
            )
            return
        
        for id, usuario, livro, tempo_emprestimo, data_retirada, data_devolucao, valor_emprestimo in emprestimo:
            print (f"ID: {id} | Usuário: {usuario} | Livro: {livro} | Tempo de Emprestimo: {tempo_emprestimo} | Data de retirada: {data_retirada} | Data de devolução: {data_devolucao} | Valor do empréstimo: {valor_emprestimo}")

    def deletar_emprestimo (
            self,
            id
    ):
        
        sql = """
        DELETE FROM emprestimos
        WHERE idEmprestimos = %s
        """

        valores = (id,)

        self.cursor.execute(
            sql, 
            valores
        )

        self.conexao.commit()

        if self.cursor.rowcount > 0:
            print ("Empréstimo deletado com sucesso.")
        

        else: 
            print("Empréstimo não encontrado.")






#  @abstractmethod
#     def cadastrar_emprestimo(
#         self,
#         usuario,
#         livro,
#         tempo_emprestimo,
#         data_retirada,
#         data_devolucao,
#         valor_emprestimo
#     ):
#         pass

#     @abstractmethod
#     def atualizar_emprestimo (
#         self,
#         id,
#         usuario,
#         livro,
#         tempo_emprestimo,
#         data_retirada,
#         data_devolucao,
#         valor_emprestimo
#     ):
#         pass

#     @abstractmethod
#     def listar_emprestimo (
#         self
#     ):
#         pass

#     @abstractmethod
#     def deletar_emprestimo (
#         self,
#         id
#     ):
#         pass