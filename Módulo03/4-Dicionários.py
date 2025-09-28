# Dicionários

pessoa = {"nome": "Icaro", "idade": 21}

pessoa = dict(nome = "Icaro", idade = 21)

pessoa["telefone"] = "9156-0096" # Adiciona o elemento ao dicionário

pessoa["nome"] # Icaro
pessoa["idade"] # 21
pessoa["telefone"] # 9156-0096

contatos = {
    "icarosouza04@outlook.com": {"nome": "Icaro", "telefone": "9156-0096"}
}

contatos["icarosouza04@outlook.com"]["telefone"] # 9156-0096

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

copia = contatos.copy() # Cria uma cópia do dicionário

dict.fromkeys(["nome", "telefone"]) # Cria chaves
dict.fromkeys(["nome", "telefone"], "vazio") # Cria chaves com o elemento atribuído

contatos.get("chave") # Busca o elemento, se não encontrar, retorna None
contatos.get("chave", {}) # Busca o elemento, se não encontrar, retorna o elemento informado
contatos.get("icarosouza04@outlook.com", {}) # Retorna o elemento, se o mesmo existir

contatos.items() # Retorna uma lista de tuplas

contatos.keys() # Retorna apenas as chaves do dicionário

contatos.pop("icarosouza04@outlook.com") # Remove a chave e retorna o valor
contatos.pop("icarosouza04@outlook.com", "Chave não encontrada.") # Remove a chave e retorna o valor passado como parâmetro

# contatos.popitem() # Remove os items na sequência, se estiver vazio, retorna um KeyError

contato = {"nome": "Icaro", "idade": 21}

contato.setdefault("nome", "Cesar")
contato.setdefault("telefone", "xxxx-xxxx")

print(contato)

contato.update({"icarosouza04@outlook,com": {"nome": "Icaro Cesar"}}) # Atualiza e adiciona o elemento no dicionário

print(contato)

print(contato.values()) # Retorna os valores do dicionário

print("nome" in contato) # Verifica se a chave está presente

del contatos["icarosouza04@outlook.com"]["nome"]
del contatos["icarosouza04@outlook.com"] # Remove completamente
del contato["idade"]
