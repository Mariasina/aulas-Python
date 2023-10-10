# -*- coding: utf-8 -*-
import random

def lista(limiteI, limiteS, tamanho):
    listaNum = []
    
    for i in range(tamanho):
        aleatorio = random.randint(limiteI, limiteS)
        listaNum.append(aleatorio)
    
    return listaNum
    

limiteIUs = int(input("Digite o limite inferior da lista: "))
limiteSUs = int(input("Digite o limite superior da lista: "))
tamanhoUs = int(input("Digite o tamanho da lista: "))

minhaLista = lista(limiteIUs, limiteSUs, tamanhoUs)
print(minhaLista)

for j in minhaLista:
    for i in range(tamanhoUs - 1):
        if minhaLista[i] > minhaLista[i+1]:  
            minhaLista[i], minhaLista[i+1] = minhaLista[i+1], minhaLista[i]
print(minhaLista)