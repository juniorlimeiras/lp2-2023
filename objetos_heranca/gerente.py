from funcionario import Funcionario
class Gerente(Funcionario): #Herdando tudo que existe na classe Funcionario (mãe)
    def __init__(self, nome, cpf, salario, email, senha, qtde):
        super().__init__(nome,cpf,salario,email)
        self._senha = senha
        self._qtde_func = qtde

    def autentica(self, senha):
        if senha == self._senha:
            return True
        else:
            return False

    def get_bonifica(self):
        return super().get_bonifica() + self._salario/100