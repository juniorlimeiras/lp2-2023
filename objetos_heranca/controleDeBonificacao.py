from funcionario import Funcionario
class ControleDeBonificacao:
    def __init__(self):
        self._total = 0

    def registra(self, func): # A referência 'func' diz respeito a qualquer tipo de Funcionários
        #if hasattr(func, 'get_bonifica'):
        #if isinstance(func, Funcionario):
        try:
            self._total += func.get_bonifica()
        except AttributeError as ae:
            print(f'Erro: {ae} \nO objeto {func} não possui bonificação.')

    def get_total(self):
        return self._total