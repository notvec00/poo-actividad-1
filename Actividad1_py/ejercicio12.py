class Nomina:
  @staticmethod
  def salario_bruto(horas, valor_hora):
    return horas * valor_hora

  @staticmethod
  def retencion(salario_bruto, porcentaje):
    return salario_bruto * porcentaje / 100

  @staticmethod
  def salario_neto(salario_bruto, retencion):
    return salario_bruto - retencion


def main():
    horas = 48
    valor_hora = 5000
    porcentaje_retencion = 12.5

    bruto = Nomina.salario_bruto(horas, valor_hora)
    retencion = Nomina.retencion(bruto, porcentaje_retencion)
    neto = Nomina.salario_neto(bruto, retencion)

    print(f'El salario bruto es {bruto}\nLa retención en la fuente es {retencion}\nEl salario neto es {neto}')


if __name__ == "__main__":
    main()