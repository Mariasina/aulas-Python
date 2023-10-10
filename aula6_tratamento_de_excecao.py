# -*- coding: utf-8 -*-
# while True:
#     try:
#         x = int(input("Digite um número: "))
#         print("Valor válido!")
#         break
#     except ValueError:
#         print("Valor inválido! Tente novamente...")

##############################################

# def ordenado(colecao):
#     try:
#         colecao.sort()
#     except AttributeError:
#         print("Imutável")
#     print(colecao, '\n')
    
# ordenado([3,2,1])
# ordenado((3,2,1))
# ordenado('321')

##############################################

def exemplo(x):
    if x < 0:
        raise StopIteration
    x = x - 1
    return x

x = 5

while True:
    try:
        x = exemplo(x)
        print(x)
    except StopIteration:
        break