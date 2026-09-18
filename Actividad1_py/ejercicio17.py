import math

class Circulo:
  @staticmethod
  def area(radio):
    return math.pi * math.pow(radio, 2)

  @staticmethod
  def circunferencia(radio):
    return 2 * math.pi * radio


def main():
    radio = float(input("Ingrese el radio del círculo: "))

    area = Circulo.area(radio)
    circunferencia = Circulo.circunferencia(radio)

    print(f'El área del círculo es {area}\nLa longitud de la circunferencia es {circunferencia}')


if __name__ == "__main__":
    main()