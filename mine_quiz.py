import random

print("==================================================\nBem vindo ao Quiz de Craftings de Minecraft!\n==================================================\n\nAdivinhe qual o item baseado na descrição do seu crafting:\n")
pontos = 0
while True: 
    try:
        # arquivo = open('itens.txt','r')
        # ler = arquivo.read()
        # split = ler.split(",")
        
        # arquivo2 = open('descricao.txt','r')
        # ler2 = arquivo2.read()
        # split2 = ler2.split(",")
        
        # item = []
        # descricao = []
        
        # item.append(split)
        # descricao.append(split2)
        
        item = ["picareta de madeira", "picareta de ferro", "escudo", "cama", "tnt", "bolo", "trilho", "funil", "fogueira", "luneta", "cenoura dourada", "sopa de coelho", "quadro", "livro", "relógio", "lampião", "laço", "bigorna", "escada", "toca disco"]
        descricao = ["Esse item é feito por 3 madeiras e 2 gravetos", "Esse item é feito com 3 ferros refinados e 2 gravetos", "Esse item é feito com 1 ferros refinados e 6 madeiras", "Esse item é feito com 3 lãs e 3 madeiras", "Esse item é feito com 4 areias e 5 pólvoras", "Esse item é feito com 3 baldes de leite, 2 açucar, 1 ovo e 3 trigos", "Esse item é feito com 6 ferros refinados e 1 graveto", "Esse item é feito com 5 ferros refinados e um baú", "Esse item é feito 3 madeiras brutas, 3 gravetos e 1 carvão", "Esse item é feito com 3 cobres refinados e 1 ametista", "Esse item é feito com 1 cenoura e 8 pepitas de ouro", "Esse item é feito de 1 tigela, 1 cenoura, 1 cogumelo vermelho, 1 coelho assado e uma batata assada", "Esse item é feito por 1 lã e 8 gravetos", "Esse item é feito com 1 couro e 3 papéis", "Esse item é feito 1 redstone e 4 ouros","Esse item é feito com 1 tocha e 8 pepitas de ferro","Esse item é feito com 4 linhas e 1 bola de slime","Esse item é feito com 3 blocos de ferro e 4 ferros refinados","Esse item é feito com 7 gravetos","Esse item é feito com 8 madeiras e 1 diamante"]
        numero = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        chances = 3
        
    
        aleatorio = random.choice(numero)
        
        
        if aleatorio == 0:
            print(descricao[0])
            print("Dificuldade: fácil")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if minusculo == "picareta de madeira" or  minusculo == "machado de madeira":
                    print("\nVocê acertou!")
                    pontos += 1
                    # descricao.remove("Esse item e feito por 3 madeiras e 2 gravetos")
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era picareta de madeira ou machado de madeira.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 1:
            print(descricao[1])
            print("Dificuldade: fácil")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if minusculo == "picareta de ferro" or minusculo == "machado de ferro":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era picareta de ferro ou machado de ferro.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 2:
            print(descricao[2])
            print("Dificuldade: médio")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "escudo":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era escudo.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 3:
            print(descricao[3])
            print("Dificuldade: fácil")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "cama":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era cama.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 4:
            print(descricao[4])
            print("Dificuldade: fácil")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "tnt":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era TNT.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 5:
            print(descricao[5])
            print("Dificuldade: médio")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "bolo":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era bolo.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 6:
            print("Dificuldade: difícil")
            print(descricao[6])
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "trilho":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era trilho.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 7:
            print("Dificuldade: difícil")
            print(descricao[7])
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "funil":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era funil.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 8:
            print(descricao[8])
            print("Dificuldade: médio")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "fogueira":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era fogueira.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 9:
            print(descricao[9])
            print("Dificuldade: fácil")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "luneta":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era luneta.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 10:
            print(descricao[10])
            print("Dificuldade: fácil")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "cenoura dourada":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era cenoura dourada.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 11:
            print(descricao[11])
            print("Dificuldade: difícil")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "sopa de coelho":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era sopa de coelho.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 12:
            print(descricao[12])
            print("Dificuldade: médio")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "quadro":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era quadro.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 13:
            print(descricao[13])
            print("Dificuldade: fácil")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "livro":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era livro.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 14:
            print(descricao[14])
            print("Dificuldade: difícil")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "relógio":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era relógio.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 15:
            print(descricao[15])
            print("Dificuldade: médio")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "lampião":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era lampião.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
        
        if aleatorio == 16:
            print(descricao[16])
            print("Dificuldade: médio")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "laço":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era laço.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 17:
            print(descricao[17])
            print("Dificuldade: fácil")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "bigorna":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era bigorna.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
        
        if aleatorio == 18:
            print(descricao[18])
            print("Dificuldade: fácil")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "escada":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era escada.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
            
        if aleatorio == 19:
            print(descricao[19])
            print("Dificuldade: médio")
            while chances != 0:
                resposta = input("\nDigite a qual item a descrição se refere: ")
                minusculo = resposta.lower()
                if resposta == "toca disco" or resposta == "toca-disco":
                    print("\nVocê acertou!")
                    pontos += 1
                    print("\nPontuação atual: ",pontos)
                    break
                else:
                    print("\nVocê errou!")
                    print("\nVocê tem mais", chances-1, "chances.")
                    chances -= 1
            if chances == 0: 
                print("A resposta correta era toca-disco.\n\nVocê perdeu todas as suas chances.\nPontuação final: ",pontos)
                break
        
        
    except KeyboardInterrupt:
            print("\n\nInterrompido com Sucesso!")
            break
            
            
