from datetime import datetime

class Emprestimo:
    def __init__ (self, TempoEmprestimo, DataRetirada, DataDevolucao, ValorEmprestimo):
        
        if not Emprestimo.validar_data(DataRetirada):
            raise ValueError ("Data inválida.")
        
        if not Emprestimo.validar_data(DataDevolucao):
            raise ValueError ("Data inválida")
        
        if not Emprestimo.validar_valor_emprestimo(ValorEmprestimo):
            raise ValueError("Valor de empréstimo inválido.")
        
        self.TempoEmprestimo = Emprestimo.validar_contagem(TempoEmprestimo)
        self.DataRetirada = DataRetirada
        self.DataDevolucao = DataDevolucao
        self.ValorEmprestimo = ValorEmprestimo
        

    
    @staticmethod
    def validar_valor_emprestimo(ValorEmprestimo):
        if str(ValorEmprestimo).isdigit() == False:
            raise ValueError("Erro o valor de empréstimo deve ser representado por dígitos numéricos.")
        else:
            return ValorEmprestimo
    
    @staticmethod
    def validar_contagem (TempoEmprestimo):
        try:
            TempoEmprestimo = int(TempoEmprestimo)
        except ValueError:
            raise ("O tempo de empréstimo deve ser um número inteiro")

        if TempoEmprestimo <= 0:
            raise ValueError ("O tempo de empréstimo deve ser maior que zero")
        
        if TempoEmprestimo > 30:
            raise ValueError ("O tempo máximo de empréstimo é 30 dias.")

        return TempoEmprestimo

    @staticmethod
    def validar_data (data):
        try:
            datetime.strptime (data, "%d/%m/%y")
            return True
        except ValueError:
            return False


        
