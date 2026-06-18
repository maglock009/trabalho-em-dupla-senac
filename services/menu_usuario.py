class Usuario:
    def __init__(self, nome, email, telefone, cpf, endereco):
        if not Usuario.validar_nome(nome):
            raise ValueError("Nome inválido")
        if not Usuario.validar_cpf(cpf):
            raise ValueError("CPF inválido")
        if not Usuario.validar_email(email):
            raise ValueError("Email inválido")
        if not Usuario.validar_telefone(telefone):
            raise ValueError("Telefone inválido")
        if not Usuario.validar_endereco(endereco):
            raise ValueError("Endereço inválido")
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.endereco = endereco
    
    @staticmethod
    def validar_nome(nome):
        if len(str(nome)) < 1 or str(nome).isdigit():
            raise ValueError
        else:
            return True
    
    @staticmethod
    def validar_cpf(cpf):
        if cpf.isdigit() and len(cpf) == 11:
            return True
        else:
            return False
        
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email
        
    @staticmethod
    def validar_telefone(telefone):
        return len(telefone) == 11
        
    @staticmethod
    def validar_endereco(endereco):
        if len(str(endereco)) == 0:
            print("O campo de endereço não pode estar vazio.")
            return False
        else:
            return endereco
