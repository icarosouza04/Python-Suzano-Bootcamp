# Interpolação de variáveis

nome = "Icaro"
idade = 21
curso = "Sistemas de Informação"
periodo = "2º"
pessoa = {"nome": "Icaro", "idade": 21, "curso": "Sistemas de Informação", "periodo": "2º"}
creditos = 35.675

# Old-style

print("Olá, me chamo %s. Eu possuo %d anos de idade, estou cursando %s, atualmente no %s período da graduação." % (nome, idade, curso, periodo))

# .format

print("Olá, me chamo {}. Eu possuo {} anos de idade, estou cursando {}, atualmente no {} período da graduação.".format(nome, idade, curso, periodo))

# .format (com identificação)

print("Olá, me chamo {nome}. Eu possuo {idade} anos de idade, estou cursando {curso}, atualmente no {periodo} período da graduação.".format(nome = nome, idade = idade, curso = curso, periodo = periodo))

print("Olá, me chamo {nome}. Eu possuo {idade} anos de idade, estou cursando {curso}, atualmente no {periodo} período da graduação.".format(**pessoa))

# f-string

print(f"Olá, me chamo {nome}. Eu possuo {idade} anos de idade, estou cursando {curso}, atualmente no {periodo} período da graduação.")

# Formatar string com f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")

# Outros exemplos

dados = {"nome": "Icaro", "idade": 21}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade,nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade,nome))

print("Nome: {nome} Idade: {idade}".format(nome = nome, idade = idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age = idade, name = nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Créditos: {creditos:5.1f}")
