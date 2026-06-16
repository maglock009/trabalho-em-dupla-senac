class Usuario:
    def __init__(self, nome, email, telefone, cpf, endereco):
        if not Usuario.validar_email(email):
            raise ValueError("Email inválido")
        if not Usuario.validar_telefone(telefone):
            raise ValueError("Telefone inválido")
        if not Usuario.validar_endereco(endereco):
            raise ValueError("Endereço inválido")
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.__cpf = cpf
        self.endereco = endereco
    
    @property 
    def nomes(self):
        return self.nome
    
    @nomes.setter
    def nomes(self, valor):
        try:
            if valor.isalpha() == True:
                self.nome = valor
            else:
                raise ValueError
        except ValueError:
            print("O nome não deve conter caracteres especiais.")
            return 
    
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, valor):
        try:
            if valor.isdigit() == True and len(valor) == 11:
                self.__cpf = valor
            else:
                raise ValueError
        except ValueError:
            print("Formato de CPF inválido.")
            return
        
    @staticmethod
    def validar_telefone(telefone):
        return len(telefone) == 11
        
    @staticmethod
    def validar_endereco(endereco):
        if len(str(endereco)) == 0:
            print("O campo de endereço não pode estar vazio.")
        else:
            return endereco
