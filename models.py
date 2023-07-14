from datetime import datetime


class Operacion:
    def __init__(self, envia, destino, fecha, valor):
        self.numeroenvia = envia
        self.numerodestino = destino
        self.fecha = fecha
        self.valor = valor


class Cuenta:
    def __init__(self, nombre, numero, saldo, contactos):
        self.nombre = nombre
        self.numero = numero
        self.saldo = saldo
        self.contactos = list()
        for u in contactos:
            self.contactos.append(u)
        self.historial = list()
        self.historial.append(saldo)
        self.historial.append("Operaciones de " + nombre)

    def contactos(self):
        return self.contactos

    def recibir(self, numero, valor):
        self.saldo += int(valor)

        self.historial[0] = valor

        self.historial.append("Pago recibido de " + valor + "de " + numero)

        return True

    def pagar(self, numero, valor):

        if (self.saldo >= int(valor)):
            self.saldo -= int(valor)
            self.historial[0] = valor

            self.historial.append("Pago realizado de " + valor + "a " + numero)

            return True
        
        return False

    def historial(self):
        return self.historial

operacion = [Operacion(123, 231, str(datetime.now()), 100)]
cuentas = [Cuenta("Paolo", 444, 1000, ["123:Piero", "456:Valolz"]), Cuenta(
    "Piero", 500, 1000, ["444:Paolo", "456:Valolz"])]
