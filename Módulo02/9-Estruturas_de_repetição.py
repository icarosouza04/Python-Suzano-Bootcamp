# Estruturas de repetição

# Etapa 1 - for e range

texto = str(input("Informe um texto: "))

VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end = "")
else:
    print()
    print("Executa o final do laço.")

for numero in range(0, 51, 5):
    print(numero, end = " ")

print()


# Etapa 2 - while

opcao = -1

while opcao != 0:

    opcao = int(input("""[1] Sacar
[2] Extrato
[0] Sair\n"""))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

else:
    print("Obrigado por utilizar nosso sistema!")

while True:

    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

while True:

    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)
