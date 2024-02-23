from autenticavel import Autenticavel


class Sistema:
    def login(self, objeto):
        #if isinstance(objeto, Autenticavel):
        #try:
        if objeto.autenticar(objeto._senha):
            print('Logado')
        else:
            print('Não logado')
        #except AttributeError:
        #    print(f'{objeto.__class__.__name__} Não autenticavel')