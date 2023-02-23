class Usuario:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def deposito(self, amount):
        self.amount += amount
        return self

    def retiro(self, amount):
        self.amount -= amount
        return self

    def mostrar_balance(self):
        print(f"Usuario: {self.name}, Total en cuenta: {self.amount}")
        return self

    def transferir_dinero(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.mostrar_balance()
        user.mostrar_balance()
        return self


# creación instancias de clase Usuario
cristina = Usuario('Cristina')
sofia = Usuario('Sofia')
tomas = Usuario('Tomas')

cristina.deposito(1000000).deposito(700000).deposito(
    5000000).retiro(3500000).mostrar_balance()

sofia.deposito(2500000).deposito(2000000).retiro(
    400000).retiro(100000).mostrar_balance()

tomas.deposito(800000).retiro(150000).retiro(
    200000).retiro(50000).mostrar_balance()

sofia.transferir_dinero(400000, cristina)
