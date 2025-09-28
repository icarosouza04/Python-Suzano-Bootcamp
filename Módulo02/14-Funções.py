# Funções

def mensagem1():

    print("Olá!")


def mensagem2(nome):

    print(f"Seja bem-vindo {nome}!")


def mensagem3(nome = "Icaro"):

    print(f"Seja bem-vindo {nome}!")


mensagem1()
mensagem2("Icaro")
mensagem2(nome = "Icaro")
mensagem3()

def calcular_total(numeros):

    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):

    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([18, 19, 25]))
print(retorna_antecessor_e_sucessor(28))

def salvar_jogo(plataforma, nome, ano, estilo):

    print(f"Jogo adicionado com sucesso!\n{plataforma}/{nome}/{ano}/{estilo}")


salvar_jogo("PS2","Dynasty Warriors 5",2005,"Musou")
salvar_jogo(plataforma = "PS2", nome = "Samurai Warriors 2", ano = 2006, estilo = "Musou")
salvar_jogo(**{"plataforma": "PS4", "nome": "Nioh", "ano": 2017, "estilo": "RPG de ação"})

def exibir_letra(nome_da_musica, *letra, **autores):

    texto = "\n".join(letra)
    dados_do_autor = "\n".join([f"{chave.title()}: {valor}" for chave, valor in autores.items()])
    letra_da_musica = f"\n{nome_da_musica}\n\n{texto}\n\n{dados_do_autor}"
    print(letra_da_musica)
    

exibir_letra("Mistakes And Regrets", """
No matter where I want to be
I've just begun
It's hard to know?
I've never been there before
It make me want to show you
That despite my mistakes and regrets
My biggest wish
Is to be on the right side
But if today I stumble, please
Don't condemn me now

Hey, I'm still here
Hey, I'm the same
Hey, why all this?
If all we have to do
Is wait for the day to end
And let the next day
Bring us something better
To make this something better
Something really special
And let go
For all that remains

No matter where I was today
I've just begun
'Cause every start again
It's a new life
It make me wanna show you
That despite my mistakes and regrets
My biggest wish
Is to be always by your side
But if today I'm on the right track
Please, don't forget that

Hey, maybe now
We find out how
Many reasons are needed for
Verses, so normal and simple
As these ones I wrote
Going round and round
Just to get to the end
To tell you
I love you
My love

No matter where I was today
I've just begun""",

autor = "Guilherme De Sá",
álbum = "Íngreme",
ano = 2017)

# "/" Define parâmetros a serem passados por posição.

def salvar_jogo2(plataforma, /, nome, ano, estilo):

    print(f"Jogo adicionado com sucesso!\n{plataforma}/{nome}/{ano}/{estilo}")


salvar_jogo2("PS4", nome = "Nioh 2", ano = 2020, estilo = "RPG de ação")

# "*" Define parâmetros a serem passados por chave/nome.

def salvar_jogo3(*, plataforma, nome, ano, estilo):

    print(f"Jogo adicionado com sucesso!\n{plataforma}/{nome}/{ano}/{estilo}")


salvar_jogo3(plataforma = "PS4", nome = "Warriors Orochi 4 ", ano = 2018, estilo = "Musou")

# "/" e "*" Define quais parâmetros serão por posição e quais serão por chave/nome. É um modelo híbrido.

def salvar_jogo4(plataforma, nome,/ , *, ano, estilo):

    print(f"Jogo adicionado com sucesso!\n{plataforma}/{nome}/{ano}/{estilo}")


salvar_jogo4("PS4", "Elden Ring", estilo = "RPG de ação", ano = 2022)

def somar(a, b):
    
    return a + b


def subtrair(a, b):

    return a - b


def multiplicar(a, b):

    return a * b


def dividir(a, b):

    return a / b


def exibir_resultado(a, b, funcao):

    resultado = funcao(a, b)
    
    print(f"O resultado da operação é igual a {resultado}.")


exibir_resultado(10, 45, somar)
exibir_resultado(10, 5, subtrair)
exibir_resultado(7, 7, multiplicar)
exibir_resultado(100, 10, dividir)

# Escopo local e global

salario = 2000

def salario_bonus(bonus, lista):

    global salario

    salario += bonus
    lista_aux = lista.copy()

    lista_aux.append(2)

    print(f"lista_aux = {lista_aux}")

    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)

print(salario_com_bonus)
print(lista)
