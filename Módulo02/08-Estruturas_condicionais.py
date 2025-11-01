# Estruturas condicionais

# Etapa 1 - Condição simples

saldo = 2000.0

saque = float(input("Digite o valor a ser retirado: R$"))

if saldo >= saque:
    print("Realizando o saque...")
else:
    print("Saldo insuficiente.")

print("-" * 20)
opcao = int(input("""Informe uma opção:
[1] Sacar
[2] Extrato\n"""))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("Opção inválida.")

MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe a idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade. Tem direito a CNH.")

if idade < MAIOR_IDADE:
    print("Menor de idade. Não possui o direito a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade. Tem direito a CNH.")
else:
    print("Menor de idade. Não possui o direito a CNH.")
    

if idade >= MAIOR_IDADE:
    print("Maior de idade. Tem direito a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Possui apenas o direito a realizar aulas teóricas.")
else:
    print("Menor de idade. Não possui o direito a CNH.")


# Etapa 2 - Condição aninhada

conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial.")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente.")

elif conta_universitaria:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente.")


elif conta_especial:
    print("Conta especial selecionada.")

else:

    print("Sistema não reconheceu o tipo de conta. Entre em contato com seu gerente.")


# Etapa 3 - Condição ternária

saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
