class CuentaBancaria:
    def __init__(self, tasa_interes=0.01, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance

    def deposito(self, cantidad):
        self.balance += cantidad
        return self

    def retiro(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("Fondos insuficientes. No se pudo realizar el retiro.")
        return self

    def mostrar_info_cuenta(self):
        print(f"Tasa de interés: {self.tasa_interes * 100}% | Saldo actual: {self.balance}")
        return self

    def generar_interes(self):
        self.balance += self.balance * self.tasa_interes
        return self

cliente1 = CuentaBancaria().deposito(100).deposito(200).deposito(300).retiro(150).generar_interes().mostrar_info_cuenta()
cliente2 = CuentaBancaria().deposito(500).retiro(50).retiro(100).retiro(100).retiro(20).generar_interes().mostrar_info_cuenta()