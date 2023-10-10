# -*- coding: utf-8 -*-
import random

tentativas = 0
num = random.randint(1,1000)
while True:
    
    chute = int(input("Tente acertar qual número de 1 a 1000 foi gerado: "))
    
    if chute > num:
        print("Seu chute é maior que o número escolhido.")
        tentativas+=1
    elif chute < num:
        print("Seu chute é menor que o número escolhido.")
        tentativas+=1
    elif chute >= num - 3 and chute <= num + 3:
        print("Você está perto")
        tentativas+=1
    elif chute == num:
        print("Você acertou!")
        print(f"Foram necessárias {tentativas} tentativas")
        break