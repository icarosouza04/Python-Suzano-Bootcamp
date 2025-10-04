# Recursos públicos e privados

class Conta:
    def __init__(self, nro_agencia = "0001", saldo = 0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    
    def depositar(self, valor):
        self._saldo += valor


    def sacar(self, valor):
        self._saldo -= valor


    def mostrar_saldo(self):
        return self._saldo


conta = Conta(100)
conta.depositar(100)

print(conta._saldo)
print(conta.nro_agencia)
print(conta.mostrar_saldo())

# Propiedades

class Foo:
    def __init__(self, x = None):
        self._x = x

    @property
    def x(self):
        return self._x or 0


    @x.setter
    def x(self, value):
        self._x += value


    @x.deleter
    def x(self):
        self._x = 0



foo = Foo(10)

print(foo.x)

del foo.x

print(foo.x)

foo.x = 10

print(foo.x)

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento


    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Icaro", 2004)

print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
