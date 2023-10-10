class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def soma(self):
        soma = self.numero1 + self.numero2
        print("\nA soma dos números é:", soma)

    def sub(self):
        sub = self.numero1 - self.numero2
        print("\nA subtração dos números é:",sub)
        
    def mult(self):
        mult = self.numero1 * self.numero2
        print("\nA subtração dos números é:",mult)
    
    def div(self):
        div = self.numero1 / self.numero2
        print("\nA divisão dos números é:",div)


class CalculadoraCientifica(Calculadora):
    def raiz(self):
        raiz1 = self.numero1 ** (1/2)
        raiz2 = self.numero2 ** (1/2)
        print(f"\nA raiz dos números é {raiz1} e {raiz2}" )

    def potencia(self):
        potencia1 = self.numero1 ** 2
        potencia2 = self.numero2 ** 2
        print(f"\nA potência ao quadrado dos números é {potencia1} e {potencia2}" )


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("\nDigite o segundo número: "))

calculadora1 = Calculadora(num1,num2)
calculadora2 = CalculadoraCientifica(num1,num2)

calculadora1.soma()
calculadora1.sub()
calculadora1.mult()
calculadora1.div()
calculadora2.raiz()
calculadora2.potencia()