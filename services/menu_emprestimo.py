class Emprestimo:
    def __init__ (self, Usuario, Livro, ISBN, DataPublicacao, QuantidadeLivro):
        self.__Usuario = Usuario
        self.livro = Livro
        self.__ISBN = ISBN
        self.DataPublicacao = DataPublicacao
        self.QuantidadeLivro = QuantidadeLivro


        @property
        def Usuario (self):
            return Usuario
        
        @Usuario.setter
        def Usuario (self, Usuario):
            
        
