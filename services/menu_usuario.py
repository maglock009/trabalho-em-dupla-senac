class Usuario:
    def __init__(self, nome, email, telefone, cpf, endereco):
        if not Usuario.validar_email(email):
            raise ValueError("Email inválido")
        if not Usuario.validar_telefone(telefone):
            raise ValueError("Telefone inválido")
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.endereco = endereco

    @property
    def nomes(self):
        return self.nome
    
    @nomes.setter
    def nomes(self, name):
        if str(name).isdigit():
            raise ValueError
        else:
            self.nome = name
    
    @property
    def cpfs(self):
        return self.cpf
    
    @cpfs.setter
    def cpfs(self, valor):
        try:
            if len(str(valor)) == 11:
                self.cpf = valor
        except ValueError:
            print("O CPF deve conter apenas dígitos numéricos.")
            return
    
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email
    
    @staticmethod
    def validar_telefone(telefone):
        return len(str(telefone)) == 11
    
