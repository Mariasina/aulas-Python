# -*- coding: utf-8 -*-
vitorias = 0
while True:
    import random
    
    num1 = int(input("Digite um número de 1 a 10: "))
    jogador1 = input("Par ou Impar? ")
    
    lista = [1,2,3,4,5,6,7,8,9,10]
    num2 = random.choice(lista)
    resultado = num1 + num2
    
    print("O computador escolheu: ", num2)
    print("Resultado: ", resultado)
    
    if jogador1 == "par" and resultado % 2 == 0:
        print("Você venceu!")
        vitorias += 1
        print("Vitórias: ", vitorias)
        
    elif jogador1 == "impar" and resultado % 2 == 0:
        print("Você perdeu!")
        print("Vitórias: ", vitorias)
        break
    
    elif jogador1 == "par" and resultado % 2 != 0:
        print("Você perdeu!")
        print("Vitórias: ", vitorias)
        break
    
    elif jogador1 == "impar" and resultado % 2 != 0:
        print("Você venceu!")
        vitorias += 1
        print("Vitórias: ", vitorias)
     

    final = int(input("Digite 0 para sair "))
    if final == 0:
        break




