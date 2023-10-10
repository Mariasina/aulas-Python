class Animais:
    def __init__(self, tipo, nome):
        self.__tipo = tipo
        self.__nome = nome

    def classificar(self):
        gato = []
        cachorro = []
        peixe = []
        if self.__tipo == "gato":
            gato.append(self.__nome)
        elif self.__tipo == "cachorro":
            cachorro.append(self.__nome)
        else:
            peixe.append(self.__nome)
            
        print(f"Gatos: {gato}\nCachorros: {cachorro}\nPeixe: {peixe}")

i = 0
for i in range(5):
    tipoAni = input(f"Digite o tipo do {i+1}º animal: ")
    nomeAni = input(f"Digite o nome do {i+1}º animal: ")
    i += 1
    resultado = Animais(tipoAni,nomeAni)
    resultado.classificar()
    



