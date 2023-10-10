class Retangulo:
    def __init__(self, base, altura, area=""):
        self.base = base
        self.altura = altura
        self.area = area

    def mostrar(self):
        self.area = self.base * self.altura
        print(f"O valor da área será: {self.area}")

valorBase = float(input("Digite o valor da base de seu retângulo: "))
valorAltura = float(input("Digite o valor da altura de seu retângulo: "))

resultado = Retangulo(valorBase, valorAltura)
resultado.mostrar()



     