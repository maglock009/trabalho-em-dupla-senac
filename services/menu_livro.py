from datetime import datetime

class Livro:
    def __init__(self,Titulo,ISBN,Autor,Editora,AnoPublicacao,QuantidadeLivro):
        if not Livro.validar_titulo(Titulo):
            raise ValueError("Título inválido.")
        if not Livro.validar_isbn(ISBN):
            raise ValueError("Código ISBN inválido.")
        if not Livro.validar_autor(Autor):
            raise ValueError("Nome do autor inválido.")
        if not Livro.validar_editora(Editora):
            raise ValueError("Nome da editora não pode estar vazio.")
        if not Livro.validar_ano_publicacao(AnoPublicacao):
            raise ValueError("Ano de publicação inválido.")
        if not Livro.validar_quantidade(QuantidadeLivro):
            raise ValueError("Quantidade de livros inválida.")
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
    
