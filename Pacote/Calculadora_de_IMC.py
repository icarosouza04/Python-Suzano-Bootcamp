# Exercitando a modularização de pacotes

from time import sleep

def Calculo_IMC(peso, altura):
    
    IMC = peso / (altura * altura)

    sleep(1)
    print(f"=" * 40)
    print(f"Você pesa {peso}Kg e mede {altura}m de altura.")
    print(f"=" * 40)
    sleep(1)
    print(f"Seu IMC é igual a {IMC:.2f}.")
    print(f"=" * 40)
    sleep(1)
    print("Calculando seu IMC...")
    print(f"=" * 40)
    sleep(1.5)

    if IMC < 18.5:
        print("Você está na faixa: Abaixo do Peso.")
    elif IMC > 18.5 and IMC < 24.9:
        print("Você está na faixa: Peso ideal.")
    elif IMC > 25 and IMC < 29.9:
        print("Você está na faixa: Sobrepeso.")
    elif IMC > 30 and IMC < 34.9:
        print("Você está na faixa: Obesidade Grau I.")
    elif IMC > 35 and IMC < 39.9:
        print("Você está na faixa: Obesidade Grau II.")
    else:
        print("Você está na faixa: Obesidade Grau III.")
    
    print(f"=" * 40)

