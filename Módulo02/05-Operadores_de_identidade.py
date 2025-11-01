# Operadores de identidade

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

# O (is) compara elementos e verifica se o objeto ocupa a mesma memória que o elemento

curso is nome_curso # Retorna True
curso is not nome_curso # Retorna False
saldo is limite # Retorna True

saldo = 1000
limite = 500

print(saldo is limite) # Retorna False
print(saldo is not limite) # Retorna True

limite = 1000

print(saldo is limite) # Retorna True
print(saldo is not limite) # Retorna False
