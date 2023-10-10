ano = int(input("Qual ano você nasceu? "))

resultado = 2023 - ano

if resultado >= 0 and resultado < 16:
    print("Você não pode votar.")
elif resultado >= 18 and resultado < 70:
    print("Seu voto é obrigatório.")     
else:
    print("Seu voto é facultativo.")
