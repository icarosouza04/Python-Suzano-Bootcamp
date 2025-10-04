# Construtor e destrutores (Métodos especiais: __init__ e __del__)

class Cachorro:

    def __init__(self, nome, cor, acordado = True):

        print("Inicializando a classe Cachorro")

        self.nome = nome
        self.cor = cor
        self.acordado = acordado


    def __del__(self):
        print("Cachorro finalizado.")


    def falar(self):
        print("Au au")


def cria_cachorro():
    c = Cachorro("Rex", "Marrom", False)
    return c

c = cria_cachorro()

print(c)

c = Cachorro("Scooby", "Preto", False)

print("Cachorro criado.")

del c

print("Cachorro bonito.")
