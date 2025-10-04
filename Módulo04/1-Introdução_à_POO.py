# Introdução à Programação Orientada a Objetos (POO)

class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):

        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    
    def buzinar(self):
        print("Buzinando...")

    
    def parar(self):
        print("Parando...")

    
    def correr(self):
        print("Correndo...")

    
    def __str__(self):
        return f"Bicicleta: {self.modelo}, {self.cor}, {self.ano}, {self.valor}"


    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(f'{chave}: {valor}' for chave, valor in self.__dict__.items())}"


    def __str__(self):
        return f"{self.__class__.__name__}: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"


b1 = Bicicleta("Azul", "Caloi", 2020, 600)

b1.buzinar()
b1.parar()
b1.correr()

print(b1)

b2 = Bicicleta("Vermelho", "Monark", 2021, 800)

b2.buzinar()
b2.parar()
b2.correr()

print(b2)
