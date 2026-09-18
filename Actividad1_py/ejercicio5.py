import math


class Seguimiento:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.suma = 0

    def sumar_x(self):
        self.suma += self.x

    def actualizar_x(self):
        self.x = self.x + math.pow(self.y, 2)

    def sumar_division(self):
        self.suma += self.x / self.y

    def mostrar_resultado(self):
        print(f"El valor de la suma es: {self.suma}")


def main():
    seguimiento = Seguimiento(20, 40)
    seguimiento.sumar_x()
    seguimiento.actualizar_x()
    seguimiento.sumar_division()
    seguimiento.mostrar_resultado()


if __name__ == "__main__":
    main()