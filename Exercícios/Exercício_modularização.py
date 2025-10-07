# Exercitando a modularização de pacotes

from Pacote import Calculadora_de_IMC

print("========== CALCULADORA DE IMC ==========")

peso = float(input("Informe seu peso(Kg): "))
altura = float(input("Informe sua altura(m): "))

Calculadora_de_IMC.Calculo_IMC(peso, altura)
