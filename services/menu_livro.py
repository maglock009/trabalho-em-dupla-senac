from datetime import datetime

class Livro:
    def __init__(self,Titulo,ISBN,Autor,Editora,AnoPublicacao,QuantidadeLivro):
        self.titulo = Titulo
        self.ISBN = ISBN
        self.Autor = Autor
        self.Editora = Editora 
        self.AnoPublicacao = AnoPublicacao
        self.QuantidadeLivro = QuantidadeLivro
    
    @staticmethod 
    def validar_titulo(titulo):
        if len(str(titulo)) <= 0:
            print("O título não deve estar vazio.")
        else:
            return titulo
            
    @staticmethod
    def validar_isbn(ISBN):
        if str(ISBN).isdigit() and len(str(ISBN)) == 11:
            return ISBN
        else:
            print("O código ISBN inserido é inválido.")
    
    @staticmethod
    def validar_autor(Autor):
        if str(Autor).isdigit() and len(str(Autor)) <= 0:
            print("O nome do autor não deve conter dígitos.")
        else:
            return Autor
    
    @staticmethod
    def validar_editora(Editora):
        if len(str(Editora)) == 0:
            raise ValueError("O nome da editora não deve estar vazio.")
        else:
            return Editora

    @staticmethod
    def validar_quantidade(QuantidadeLivro):
        if QuantidadeLivro == int() and QuantidadeLivro > 0:
            return QuantidadeLivro
        else:
            print("A quantidade de livros deve ser representada por números inteiros.")
    
    @staticmethod
    def validar_ano_publicacao(AnoPublicacao):
        if AnoPublicacao == datetime.fromisoformat():
            return AnoPublicacao
        else:
            print("O ano de publicação definido tem formato inválido.")
    
