from interfaces.repositorio_usuario import RepositorioUsuario
from config.database import conectar


class RepositorioUsuarioMySQL(RepositorioUsuario):
    def __init__(self, nome, email, cpf, telefone):
        self.nome = nome
        self.email = email
        self.__cpf = cpf
        self.telefone = telefone
        self.conexao = conectar()
        self.cursor = self.conexao.cursor()
        super().__init__()

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, valor):
        if valor.isalpha():
            self.nome = valor
        else:
            raise ValueError("O nome não deve conter número ou caracteres especiais: ")
        
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email
    
    @staticmethod
    def validar_telefone(telefone):
        return len(telefone) == 11

    @property 
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, valido):
        if len(valido) == 11:
            self.__cpf = valido
        else:
            raise ValueError("Formato de CPF inválido.")
    
