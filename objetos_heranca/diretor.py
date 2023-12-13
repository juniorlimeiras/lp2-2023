from gerente import Gerente
class Diretor(Gerente):
    def __init__(self, nome, cpf, sal, email, senha, qtde, seg):
        super().__init__(nome, cpf, sal, email, senha, qtde)
        self._seg = seg

    def get_bonifica(self):
        return super().get_bonifica() + 300