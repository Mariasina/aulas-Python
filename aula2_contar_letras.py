# -*- coding: utf-8 -*-

nome = input("Digite seu nome completo apenas com letras minúsculas: ")

nomeMaius = nome.title()
nomeCount = nome.replace(' ', '')

print(nomeMaius, "Seu nome possui caracteres")
print(len(nomeCount))

