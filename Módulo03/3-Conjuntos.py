# Conjuntos

set([1, 2, 3, 1, 2, 3, 4]) # Elimina elementos repetidos
set("Abacaxi") # Elimina elementos repetidos, mas não garante a ordem em que vão ser exibidos
set(("PS1", "PS2", "PS2", "PS3", "PS4", "PS5"))

linguagens = {"Python", "Java", "Python"} # "{}" representa o comando set (não recomendado)

numeros = {1, 2, 3, 4}
numeros2 = {1, 2, 5, 6}
numeros3 = {7, 8, 9, 10}

numeros = list(numeros)
print(numeros[0])

jogos = {"Nioh", "Nioh 2", "Nioh 3"}

for jogo in jogos:
    print(jogo)

for indice,jogo in enumerate(jogos):
    print(f"{indice + 1} - {jogo}")

jogos2 = {"Dark Souls", "Dark Souls 2", "Dark Souls 3", "Nioh 3"}

print(jogos.union(jogos2)) # Exibe a união entre conjuntos
print(jogos.intersection(jogos2)) # Exibe a interseção entre conjuntos
print(jogos.difference(jogos2)) # Exibe a diferença entre conjuntos
print(jogos.symmetric_difference(jogos2)) # Exibe todos os elementos que não estão na interseção do conjunto
print(numeros.issubset(numeros2)) # Verifica se todos os elementos do 1º termo estão presentes no 2º
print(numeros.issuperset(numeros2)) # O mesmo que o anterior, invertido
print(numeros.isdisjoint(numeros2)) # Exibe elementos que não se repetem nos conjuntos
print(numeros.isdisjoint(numeros3)) # Exibe elementos que não se repetem nos conjuntos

sorteio = {1, 2}

sorteio.add(3) # Adiciona um elemento
sorteio.add(4)
sorteio.add(3) # Ignora pois o 3 já foi adicionado

sorteio.discard(4) # Descarta o valor
sorteio.discard(5)

sorteio.remove(1) # Remove o elemento se ele existir

sorteio.pop(3) # Exclui o valor indicado

len(sorteio) # Exibe o tamanho do conjunto

1 in sorteio # Verifica se o elemento está presente
2 in sorteio # Verifica se o elemento está presente

sorteio.copy() # Cria uma cópia

sorteio.clear() # Limpa
