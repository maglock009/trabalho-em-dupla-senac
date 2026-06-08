class Livro:
    def __init__(self,Titulo,ISBN,Autor,Editora,AnoPublicacao,QuantidadeLivro):
        self.titulo = Titulo
        self.__ISBN = ISBN
        self.Autor = Autor
        self.Editora = Editora 
        self.AnoPublicacao = AnoPublicacao
        self.QuantidadeLivro = QuantidadeLivro

    @property
    def ISBN(self):
        return self.__ISBN

    @ISBN.setter
    def ISBN(self, valor):
        if str(valor).isdigit() and len(str(valor)) == 13:
            self.__ISBN = valor
        else:
            raise ValueError("O código ISBN do livro deve conter apenas 13 dígitos.")

    @property
    def quantidade_livros(self):
        return self.QuantidadeLivro

    @quantidade_livros.setter
    def quantidade_livros(self, valor):
        try:
            if valor == int():
                self.QuantidadeLivro = valor
        except ValueError:
            print("A quantidade de livros deve ser representada por um número inteiro.")

    @property
    def autor(self):
        return self.Autor

    @autor.setter
    def autor(self, nome):
        if str(nome).isdigit():
            raise ValueError
        else:
            self.Autor = nome