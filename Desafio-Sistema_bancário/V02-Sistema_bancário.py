# Desafio 01 - Sistema bancário

import textwrap

def menu():

    menu = """
    ======== BANCO ========

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar contas
    [0] Sair

    =======================
    """

    return input(textwrap.dedent(menu))


def depositar(saldo, deposito, extrato, /):

    if deposito > 0:
        saldo += deposito
        extrato += f"{'Depósito':<12} R${deposito:.2f}\n"
        print(f"\nDepósito no valor de R${deposito} foi realizado com sucesso!\n")
    
    else:
        print("\nOperação falhou! O valor informado é inválido!")

    return saldo, extrato


def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = saque > saldo
    excedeu_limite = saque > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não possui saldo suficiente.\n")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.\n")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques diários excedido.\n")

    elif saque > 0:
        saldo -= saque

        extrato += f"{'Saque':<12} R${saque:.2f}\n"

        numero_saques += 1

        print(f"\nSaque no valor de R${saque:.2f} realizado com sucesso!\n")

    else:
        print("\nOperação falhou! O valor informado é inválido!\n")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):

    print("\n======== EXTRATO BANCÁRIO ========\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"{'Saldo':<12} R${saldo:.2f}\n")
    print("====================================")


def criar_usuario(usuarios):

    cpf = input("Informe o CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário com este CPF!")

        return

    nome = str(input("Informe o nome completo: "))
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")

        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, operação encerrada!")


def listar_contas(contas):

    for conta in contas:
        linha = f"""\n
        Agência\t {conta["agencia"]}
        C/C\t {conta["numero_conta"]}
        Titular\t {conta["usuario"]["nome"]}
        """
        print("=" * 40)
        print(textwrap.dedent(linha))


def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = int(menu())

        if opcao == 1:

            deposito = float(input("Informe o valor a ser depositado: R$"))

            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao == 2:

            saque = float(input("Informe o valor a ser retirado: R$"))

            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                saque = saque,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
            )

        elif opcao == 3:

            exibir_extrato(saldo, extrato = extrato)

        elif opcao == 4:

            criar_usuario(usuarios)

        elif opcao == 5:

            numero_conta = len(contas) + 1
            
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            
            
        elif opcao == 6:

            listar_contas(contas)

        elif opcao == 0:

            print("\nEncerrando o programa...")
            break

        else:
            print("\nOpção inválida! Selecione a operação conforme indicado.")


main()
