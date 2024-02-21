from funcionario import Funcionario
class ControleDeBonificacao:
    _total = 0

    def registra(self, func): # A referência 'func' diz respeito a qualquer tipo de Funcionários
        #if hasattr(func, 'get_bonifica'):
        #if isinstance(func, Funcionario):
        try:
            print(func.get_bonifica())
            ControleDeBonificacao._total += func.get_bonifica()
        except AttributeError as ae:
            print(f'Erro: {ae} \nO objeto {func} não possui bonificação.')

    @classmethod
    def total(cls):
        return cls._total