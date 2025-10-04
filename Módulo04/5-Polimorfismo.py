# Polimofirmo com herança

class Passaro:
    def voar(self):
        print("Voando..")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar.")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar.")


# Exemplo ruim do uso de herança para "ganhar" o método voar.
class Aviao(Passaro):
    def voar(self):
        print("Avião decolando...")


def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
