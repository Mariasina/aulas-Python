# -*- coding: utf-8 -*-
arquivo = open('arquivo.txt','r')

ler = arquivo.read()
semVirgula = ler.replace(',', ' ')
semPonto = semVirgula.replace('.',' ')
semParen1 = semPonto.replace('(',' ')
semParen2 = semParen1.replace(')',' ')
minusculo = semParen2.lower()

split = minusculo.split()

palavra = input("Digite uma palavra: ")
print(split.count(palavra))

arquivo.close()


# lista = []

# 

# for i in split:
#     lista.append(split.count(i))
    
# print(str(list(zip(split[palavra], lista[palavra]))))