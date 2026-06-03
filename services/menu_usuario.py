class Usuario:
    def __init__(self, nome, email, telefone, cpf, endereco):
        if not Usuario.validar_email(email):
            raise ValueError("Email inválido")
        if not Usuario.validar_telefone(telefone):
            raise ValueError("Telefone inválido")
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.__cpf = cpf
        self.endereco = endereco

    @property
    def nomes(self):
        return self.nome
    
    @nomes.setter
    def nomes(self, name):
        if name.isdigit():
            raise ValueError
        else:
            self.nome = name
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, valor):
        try:
            valor = int()
            if len(valor) == 11:
                self.__cpf = valor
        except ValueError:
            print("Formato de CPF inválido.")
    
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email
    
    @staticmethod
    def validar_telefone(telefone):
        return len(telefone) == 11
    
