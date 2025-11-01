# Listas

frutas = ["Laranja", "Maçã", "Uva", "Pera"]

print(frutas[-1])
print(frutas[-3])

frutas = []
numeros = (list(range(10)))
letras = list("Python")

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

lista = ["P", "y", "t", "h", "o", "n"]

print(lista)
print(lista[2:])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

jogos = ["Samurai Warriors 5", "Yakuza 0", "Nioh"]

for jogo in jogos:
    print(jogo)

for indice, jogo in enumerate(jogos):
    print(f"{indice} - {jogo}")

numeros = [1, 30, 21, 2, 9, 65, 34, 12, 88, 97]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

numeros2 = [1, 12, 4, 66, 95, 77]
pares2 = [numero for numero in numeros2 if numero % 2 == 0]

numeros3 = [3, 7, 14, 2, 77, 98, 41]
quadrado = []

for numero in numeros3:
    quadrado.append(numero ** 2)

# Métodos

jogos2 = ["Fortnite", "League of Legends", "Valorant", 2017, 2009, 2020]

print(jogos2)

jogos2.clear() # Limpa a lista

print(jogos2)

jogos3 = ["Dynasty Warriors 5", "Warriors Orochi", 2005, 2007]

jogos4 = jogos2.copy() # Faz uma cópia da lista
jogos4 = jogos3.copy()

print(jogos4)

plataformas = ["PS1", "PS2", "PS3", "PS4", "PS5" , "PS4"]

plataformas.count("PS1") # Exibe quantas vezes o elemento aparece na lista
plataformas.count("PS2")
plataformas.count("PS3")
plataformas.count("PS4")
plataformas.count("PS5")

print(plataformas)

plataformas.extend(["XBOX", "XBOX 360", "XBOX ONE", "XBOX SERIES"]) # Adiciona uma lista a outra lista

print(plataformas)

print(plataformas.index("XBOX")) # Exibe o primeiro índice onde o elemento aparece
print(plataformas.index("PS4"))

plataformas.pop() # Remove o último elemento da lista
plataformas.pop()
plataformas.pop()
plataformas.pop(6)

plataformas.remove("XBOX") # Remove o elemento indicado

plataformas.reverse() # Inverte a lista

print(plataformas)

plataformas.sort() # Ordena a lista em ordem alfabética
plataformas.sort(Reverse = True) # Ordena a listaem ordem afabética, e inverte-a
plataformas.sort(key = lambda x: len(x)) # Ordena do menor elemento para o maior
plataformas.sort(key = lambda x: len(x), reverse = True) # Ordena do maior elemento para o menor

sorted(plataformas, key = lambda x: len(x)) # Função parecida com a anterior
sorted(plataformas, key = lambda x: len(x), reverse = True)
print(sorted(plataformas))

print(len(plataformas)) # Exibe o tamanho da lista
