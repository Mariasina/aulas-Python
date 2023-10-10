# -*- coding: utf-8 -*-

num = int(input("Digite um número inteiro: "))
multiplo = 0

for i in range(2, num):
    if num % i == 0:
        multiplo+=1
        
if multiplo == 0:
    print(f"O número {num} é primo")
else:
    print(f"O número {num} não é primo")
    
        
