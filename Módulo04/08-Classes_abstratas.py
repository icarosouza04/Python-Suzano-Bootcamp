# Classes abstratas com o módulo ABC

from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass


    @abstractmethod
    def desligar(self):
        pass

    
    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")


    def desligar(self):
        print("Deslingando a TV...")
        print("Desligada!")


    @property
    def marca(self):
        return "LG"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o ar condicionado...")
        print("Ligado!")


    def desligar(self):
        print("Desligando o ar condicionado")
        print("Desligado")

    
    @property
    def marca(self):
        return "Springer"


controle = ControleTV()

controle.ligar()
controle.desligar()

print(controle.marca)

controle = ControleArCondicionado()

controle.ligar()
controle.desligar()

print(controle.marca)
