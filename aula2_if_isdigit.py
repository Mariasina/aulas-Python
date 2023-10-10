# -*- coding: utf-8 -*-
resposta = 42

numero = (input("Dê um palpite de qual é o número secreto: "))

if numero.isdigit():
    if numero == 42:
        print("Você acertou!")
    else:
        print("Você errou!")    
else:
    print("Valor invalido!")        

    