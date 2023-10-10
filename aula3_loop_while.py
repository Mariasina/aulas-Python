# -*- coding: utf-8 -*-
limite = int(input("Digite um número para o limite da soma: "))

num = 0
repeticoes = 1

while repeticoes <= limite:
    num += repeticoes
    repeticoes += 1

print("O valor da soma é: ", num)
    