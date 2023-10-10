class Livros():
    def __init__(self, titulo, qtdPaginas, paginasLidas):
        self.__titulo = titulo
        self.__qtdPaginas = qtdPaginas
        self.__paginasLidas = paginasLidas


    def getTitulo(self):
        return self.__titulo
    
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def getqtdPaginas(self):
        return self.__qtdPaginas
    
    def setqtdPaginas(self, qtdPaginas):
        self.__qtdPaginas = qtdPaginas

    def getpaginasLidas(self):
        return self.__paginasLidas
    
    def setpaginasLidas(self, paginasLidas):
        self.__paginasLidas = paginasLidas

    def verificarProgresso(self):
        porcentagem = self.__paginasLidas * 100 / self.__qtdPaginas
        print(f"Você leu {porcentagem}% do seu livro!!!!!!!!")

class TestarLivros(Livros):
    def livrofavorito(self):
        self.__titulo = "Pequeno Príncipe"

        self.__qtdPaginas = 98

        self.__paginasLidas = 20
    
        print(f"O livro {self.__titulo} tem {self.__qtdPaginas} páginas.")


nome = input("Digite o título do seu livro: ")
paginas = int(input("Digite a quantidade de páginas do seu livro: "))
paginasLido = int(input("Digite a quantidade de páginas lidas: "))

lido = Livros(nome, paginas, paginasLido)
lido.verificarProgresso()

pequeno = TestarLivros(nome, paginas, paginasLido)
pequeno.livrofavorito()