# -*- coding: utf-8 -*-
quantidade = int(input("Digite um número para a quantidade de fatores da série Fibonacci: "))

lista=[0,1]

for i in range(2, quantidade):
    lista.append(lista[i-1] + lista[i-2])
    
print(lista[:quantidade])

# for i in range(quantidade):
#     termo3 = termo1 + termo2
#     for j in range(termo3):
#         termoResult = termo3 + termo2
#         print(termoResult)
