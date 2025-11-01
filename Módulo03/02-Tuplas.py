# Tuplas são imutáveis

frutas = ("Laranja", "Pera", "Uva",)

letras = tuple("Python")

numeros = tuple([1, 2, 3, 4])

país = ("Brasil",)

print(frutas[0])
print(frutas[-1])

jogos = ("God of War", "Ghost of Tsushima",)

for jogo in jogos:
    print(jogo)

for indice,jogo in enumerate(jogos):
    print(f"{indice + 1} - {jogo}")

jogos.count("God of War")
jogos.index("Ghost of Tsushima")
len(jogos)
