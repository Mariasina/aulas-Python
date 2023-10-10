class Pessoa():
    def __init__(self, nome, idade, genero):
        self.__nome = nome
        self.__idade = idade
        self.__genero = genero
        
    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome

    def getIdade(self):
        return self.__idade
    
    def setIdade(self, idade):
        self.__idade = idade
    
    def getGenero(self):
        return self.__genero
    
    def setGenero(self, genero):
        self.__genero = genero

class Funcionario(Pessoa):
    def __init__(self, cargo, salario, numFuncionario):
        self.__cargo = cargo
        self.__salario = salario
        self.__numFuncionario = numFuncionario

    def getCargo(self):
        return self.__cargo
    
    def setCargo(self, cargo):
        self.__cargo = cargo

    def getSalario(self):
        return self.__salario
    
    def setSalario(self, salario):
        self.__salario = salario
    
    def getNumFuncionario(self):
        return self.__numFuncionario
    
    def setNumFuncionario(self, numFuncionario):
        self.__numFuncionario = numFuncionario

    def bonificacaoFunc(self):
        bonificacao = self.__salario * 0.10

class Gerente(Funcionario):
    def __init__(self, setor):
        self.__setor = setor

    def bonificacaoGer(self):
        bonificacao = self.__salario * 0.15

class Departamento():
    def __init__(self, nomeDep, listaFunc):
        self.__nomeDep = nomeDep
        self.__listaFunc = listaFunc
        listaFunc = []

    def adicionarFunc(self):
        self.__listaFunc.append(self.__nome)
        print(self.__listaFunc)

adicionar = Departamento.adicionarFunc()