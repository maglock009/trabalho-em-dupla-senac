from abc import ABC, abstractmethod

class RepositorioUsuario(ABC):
    @abstractmethod
    def cadastrar_usuario(
        self,
        nome,
        email,
        telefone,
        cpf
    ):
        pass

    @abstractmethod
    def atualizar_usuario(
        self,
        id,
        nome,
        email,
        telefone
    ):
        pass

    @abstractmethod
    def listar_usuarios(
        self
    ):
        pass

    @abstractmethod
    def excluir_usuario(
        self,
        id
    ):
        pass