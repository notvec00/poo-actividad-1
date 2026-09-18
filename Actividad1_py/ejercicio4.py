class CalcularEdades:
  @staticmethod
  def edalber(edjuan):
    return 2*edjuan/3

  @staticmethod
  def edana(edjuan):
    return 4*edjuan/3

  @staticmethod
  def edmama(edjuan,edana,edalber):
    return edjuan + edana +edalber


def main():
    edjuan = float(input("Ingrese la edad de Juan: "))

    edalber = CalcularEdades.edalber(edjuan)
    edana = CalcularEdades.edana(edjuan)
    edmama = CalcularEdades.edmama(edjuan, edalber, edana)

    print(f'La edad de Juan es {edjuan} años\nLa edad de Alberto es {edalber} años\nLa edad de Ana es {edana} años\nLa edad de la Mama es {edmama} años')


if __name__ == "__main__":
    main()

