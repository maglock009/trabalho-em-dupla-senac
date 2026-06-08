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
        try:
            if name.isdigit():
                raise ValueError
            else:
                self.nome = name
        except ValueError:
            print("O nome não deve conter dígitos ou caracteres especiais.")
            return
    
    @property
    def cpfs(self):
        return self.cpf
    
    @cpfs.setter
    def cpfs(self, valor):
        try:
            if valor.isdigit() and len(str(valor)) == 11:
                self.cpf = valor
            else:
                raise ValueError
        except ValueError:
            print("O CPF deve conter apenas dígitos numéricos.")
            return
    
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email
    
    @staticmethod
    def validar_telefone(telefone):
        return telefone.isdigit() and len(telefone) == 11
    