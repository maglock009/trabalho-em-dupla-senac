from abc import ABC, abstractmethod

class RepositorioLivro (ABC):
    @abstractmethod
    def cadastrar_livro(
        self,
        Titulo,
        ISBN,
        Autor,
        Editora,
        AnoPublicacao,
        QuantidadeLivro
    ):
        pass

    @abstractmethod
    def atualizar_livro (
        self,
        id,
        Título,
        ISBN,
        Autor,
        Editora,
        AnoPublicacao,
        QuantidadeLivro
    ):
        pass

    @abstractmethod
    def listar_livro (
        self
    ):
        pass

    @abstractmethod
    def excluir_livro (
        self,
        id
    ):
        pass
        




