# Desafio 01 - Sistema bancário

menu = """
======== BANCO ========

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=======================
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:

        deposito = float(input("Informe o valor a ser depositado: R$"))

        if deposito > 0:
            print(f"O valor R${deposito} foi depositado com sucesso!")
            
            saldo += deposito

            extrato += f"Valor depositado: R${deposito}\n"
        
        else:
            print("Valor inválido. Tente novamente.")

    elif opcao == 2:

        saque = float(input("Informe o valor a ser sacado: R$"))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:

            print("Operação falhou! O valor retirado execeu o saldo.")
        
        elif excedeu_limite:
            
            print("Operação falhou! O valor retirado excedeu o limite.")

        elif excedeu_saques:

            print("Operação falhou! A quantidade limite de saques diários foi excedida.")

        elif saque > 0:

            print(f"Valor R${saque} retirado com sucesso!")
            
            saldo -= saque
            extrato += f"Valor sacado: R${saque}\n"
            numero_saques += 1
        
        else:

            print("Operação falhou! O valor informado é inválido.")


    elif opcao == 3:
        
        print("Exibindo o extrato bancário...")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print("\n======== EXTRATO ========\n")
        print(extrato)
        print(f"Saldo: R${saldo:.2f}\n")
        print("=========================")

    elif opcao == 0:

        print("Saindo do sistema...")
        break
    
    else:

        print("Opção inválida. Tente novamente")
