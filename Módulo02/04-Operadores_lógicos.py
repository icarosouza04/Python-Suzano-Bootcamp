# Operadores lógicos

saldo = 1000
saque = 200
limite = 100

# Operadores True e False

saldo >= saque # Retorna True
saque <= limite # Retorna False

# Operador E (and)

saldo >= saque and saque <= limite # Retorna False

# Operador Ou (or)

saldo >= saque or saque <= limite # Retorna True

# Operador de negação

contatos_emergencia = [] # Uma lista vazia é considerada falsa

not 1000 > 1500 # Retorna True
not contatos_emergencia # Retorna True
not "saque 1500;" # False
not "" # True

# Operadores com parênteses

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp01 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque # Retorna True
print(exp01)

exp02 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # Retorna True
print(exp02)

# Tabela lógica

print(True and True) # Retorna True
print(True and False) # Retorna False
print(False and False) # Retorna 
print(True or True) # Retorna True
print(True or False) # Retorna True
print(False or False) # Retorna False

# Para (and) ser True, tudo deve ser True
# Para (or) ser True, apenas um deve ser True
