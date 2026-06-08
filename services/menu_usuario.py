class Usuario:
    def __init__(self, nome, email, telefone, cpf, endereco):
        if not Usuario.validar_email(email):
            raise ValueError("Email inválido")
        if not Usuario.validar_telefone(telefone):
            raise ValueError("Telefone inválido")
        if not Usuario.validar_nome (nome):
            raise ValueError ("Nome inválido")
        if not Usuario.validar_cpf(cpf):
            raise ValueError ("CPF inválido")
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
        if str(name).isdigit():
            raise ValueError
        else:
            self.nome = name
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, valor):
        try:
            if len(str(valor)) == 11:
                self.__cpf = valor
        except ValueError:
            print("Formato de CPF inválido.")
    
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email
    
    @staticmethod
    def validar_telefone(telefone):
        return len(telefone) == 11

    @staticmethod
    def validar_nome(nome):
        if any(char.isdigit() for char in str(nome)):
            print ("O seu nome não pode ter números.")
            return False
        elif not str(nome).strip():
            print ("O seu nome não pode estar vazio.")
            return False
        else:
            return True
    
    @staticmethod
    def validar_cpf (cpf):
        if len(str(cpf)) != 0 or str(cpf).isalpha()==True:
            raise ValueError ("CPF inválido")
        else:
            return cpf
