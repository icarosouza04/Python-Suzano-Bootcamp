# Manipulando strings

curso = "pYthon"

print(curso.upper())
print(curso.lower())
print(curso.title())

curso = "  Python  "

print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())

curso = "Python"

print(curso.center(10, "#"))
print(".".join(curso))

nome = "Icaro"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "Olá, Icaro!"

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("++++" + menu + "++++")
print(menu.center(14))
print(menu.center(14, "+"))
print("P-y-t-h-o-n")
print("-".join(menu))

for letra in menu:
    print(letra, end = "-")
print()
