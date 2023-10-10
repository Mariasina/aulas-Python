# -*- coding: utf-8 -*
def escolha_corretor(escolhaC):
    if escolhaC >= 5:
        print("Escolha inválida!")
    return escolhaC

while True:
    try:
        
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
    
        escolha = int(input("Escolha entre: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n0 - Sair \n"))
        
        corrigir = escolha_corretor(escolha)
        
        #continuar = bool(input("Digite 0 se quiser sair, para continuar digite qualquer valor: ")) 
        
        if escolha == 1:
            soma = num1 + num2
            print("O resultado da soma é: ", soma)
        elif escolha == 2:
            sub = num1 - num2
            print("O resultado da subtração é: ", sub)
        elif escolha == 3:
            multi = num1 * num2
            print("O resultado da multiplicação é: ", multi)
        elif escolha == 4:
            div = num1 / num2
            print("O resultado da divisão é: ", div)
        elif escolha == 0:
            break
        
        continuar = int(input("Digite 0 se quiser sair, para continuar digite qualquer valor: "))
        if continuar == 0:
            break
    except ValueError:
        print("Valor inválido! Tente novamente...")
    except KeyboardInterrupt:
        print("\nPrograma terminado com sucesso!")  
        break

