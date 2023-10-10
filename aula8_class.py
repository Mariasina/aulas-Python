class Casa:
    def __init__(self, area, rua, cor, nome=''):
        self.area = area
        self.rua = rua
        self.cor = cor
        self.nome = nome

casa1 = Casa("tres","rua dois","vermelho","ana")
print(casa1.area, casa1.rua, casa1.cor, casa1.nome)