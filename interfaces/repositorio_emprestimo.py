from abc import ABC, abstractmethod

class RepositorioEmprestimo(ABC):
    @abstractmethod
    def cadastrar_emprestimo(
        self,
        usuario,
        livro,
        tempo_emprestimo,
        data_retirada,
        data_devolucao,
        valor_emprestimo
    ):
        pass

    @abstractmethod
    def atualizar_emprestimo (
        self,
        id,
        usuario,
        livro,
        tempo_emprestimo,
        data_retirada,
        data_devolucao,
        valor_emprestimo
    ):
        pass

    @abstractmethod
    def listar_emprestimo (
        self
    ):
        pass

    @abstractmethod
    def deletar_emprestimo (
        self,
        id
    ):
        pass