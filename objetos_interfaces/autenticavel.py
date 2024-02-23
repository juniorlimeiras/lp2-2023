import abc

class Autenticavel(abc.ABC):
    """
    A interface Autenticavel define como os usuários
    devem autenticar no sistema.
    """
    @abc.abstractmethod
    def autenticar(self, senha):
        """
        O método deve verificar a senha e retornar um booleano
        """
        pass