# -*- coding: utf-8 -*-
import math

def operacoes(num1):
    fatorial = math.factorial(num1)
    inverso = num1 ** -1
    quadrado = num1 ** 2
    raiz = num1 // 2
    
    return quadrado, raiz, inverso, fatorial

numero = int(input("Digite um número: "))

resultados = operacoes(numero)

print("Os resultados do elevado ao quadrado, raiz quadrada, inverso do número e fatorial, nessa ordem, são:", resultados)