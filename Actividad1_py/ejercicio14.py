import math

class Calculos:
  @staticmethod
  def cuadrado(numero):
    return math.pow(numero, 2)

  @staticmethod
  def cubo(numero):
    return math.pow(numero, 3)


def main():
    numero = float(input("Ingrese un número: "))

    cuadrado = Calculos.cuadrado(numero)
    cubo = Calculos.cubo(numero)

    print(f'El cuadrado de {numero} es {cuadrado}\nEl cubo de {numero} es {cubo}')


if __name__ == "__main__":
    main()