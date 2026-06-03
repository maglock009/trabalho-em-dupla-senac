from abc import ABC, abstractmethod

class RepositorioUsuario(ABC):
    @abstractmethod
    def cadastrar_usuario(
        self,
        nome,
        email,
        telefone,
        cpf,
        endereco
    ):
        pass

    @abstractmethod
    def atualizar_usuario(
        self,
        id,
        nome,
        email,
        telefone,
        endereco
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