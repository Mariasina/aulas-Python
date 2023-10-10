# -*- coding: utf-8 -*-
menu = {'Hamburguer':10,"Hotdog":6.5,"Salada":4,"Suco":4,"Refrigerante":4.5,"Água":2}

comida = input("Digite a comida que você deseja: ")
bebida = input("Digite a bebida que você deseja: ")

total = menu[comida] + menu[bebida]

print("O valor total é de: ", total)
