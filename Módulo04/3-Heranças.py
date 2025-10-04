# Herança simples

class Veiculo:

    def __init__(self, cor, placa, numero_rodas):

        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(f'{chave}: {valor}' for chave, valor in self.__dict__.items())}"


class Motocicleta(Veiculo):
    
    pass

class Carro(Veiculo):

    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{"Sim," if self.carregado else "Não"} está carregado.")


moto = Motocicleta("Preto", "ABC-1234", 2)
carro = Carro("Verde", "DEF-5678", 4)
caminhao = Caminhao("Branco", "GHI-9101", 10, False)

print(moto)
print(carro)
print(caminhao)

# Herança múltipla

class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(f'{chave}: {valor}' for chave, valor in self.__dict__.items())}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

    def __str__(self):
        return "Mamífero"


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

    def __str__(self):
        return "Ave"


class Gato(Mamifero):
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas


class FalarMixin:
    def falar(self):
        return "Oi, estou falando!"

        
class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        print(Ornitorrinco.__mro__)
        super().__init__(cor_pelo = cor_pelo, cor_bico = cor_bico, nro_patas = nro_patas)

    def __str__(self):
        return "Ornitorrinco"


gato = Gato(nro_patas = 4, cor_pelo = "Branco")
ornitorrinco = Ornitorrinco(nro_patas = 4, cor_pelo = "Azul", cor_bico = "Laranja")

print(gato)
print(ornitorrinco)
