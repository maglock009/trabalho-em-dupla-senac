class Emprestimo:
    def __init__ (self, TempoEmprestimo, DataRetirada, DataDevolucao, ValorEmprestimo):
        if not Emprestimo.validar_data(TempoEmprestimo):
            raise ValueError ("Data inválida.")
        if not Emprestimo.validar_data(DataRetirada):
            raise ValueError ("Data inválida.")
        if not Emprestimo.validar_data(DataDevolucao):
            raise ValueError ("Data inválida")
        self.__ValorEmprestimo = ValorEmprestimo

    @property
    def ValorEmprestimo (self):
        return self.__ValorEmprestimo

    @ValorEmprestimo.setter
    def ValorEmprestimo (self,valor):
        if valor.isdigit() == False:
            raise ValueError
        else:
            self.ValorEmprestimo = valor
        




        
