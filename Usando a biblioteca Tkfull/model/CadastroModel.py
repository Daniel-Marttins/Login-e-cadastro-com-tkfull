
class CadastroModel:

    def __init__(self):

        self.__nome = str
        self.__email = str
        self.__cpf = str
        self.__senha = str
        self.__estado = str
        self.__cidade = str
        self.__ddd = str
        self.__ncelular = str
        self.__genero = str
        self.__nmatricula = str
        self.__aulas = str
        self.__renda = str

    def setNome(self,Nome):
        self.__nome = Nome
    def setEmail(self,Email):
        self.__email = Email
    def setCpf(self,Cpf):
        self.__cpf = Cpf
    def setSenha(self,Senha):
        self.__senha = Senha
    def setEstado(self,Estado):
        self.__estado = Estado
    def setCidade(self,Cidade):
        self.__cidade = Cidade
    def setDdd(self,Ddd):
        self.__ddd = Ddd
    def setNcelular(self,Ncelular):
        self.__ncelular = Ncelular
    def setGenero(self,Genero):
        self.__genero = Genero
    def setNmatricula(self,Nmatricula):
        self.__nmatricula = Nmatricula
    def setAulas(self,Aulas):
        self.__aulas = Aulas
    def setRenda(self,Renda):
        self.__renda = Renda

    def getNome(self):
        return self.__nome
    def getEmail(self):
        return self.__email
    def getCpf(self):
        return self.__cpf
    def getSenha(self):
        return self.__senha
    def getEstado(self):
        return self.__estado
    def getCidade(self):
        return self.__cidade
    def getDdd(self):
        return self.__ddd
    def getNcelular(self):
        return self.__ncelular
    def getGenero(self):
        return self.__genero
    def getNmatricula(self):
        return self.__nmatricula
    def getAulas(self):
        return self.__aulas
    def getRenda(self):
        return self.__renda


    def cadastro(self):
        no = self.getNome()
        em = self.getEmail()
        cp = self.getCpf()
        se = self.getSenha()
        es = self.getEstado()
        ci = self.getCidade()
        dd = self.getDdd()
        nc = self.getNcelular()
        ge = self.getGenero()
        nm = self.getNmatricula()
        au = self.getAulas()
        re = self.getRenda()
        retorno = no +'\n' + em +'\n' + cp +'\n' + se +'\n' + es +'\n' + ci +'\n' + dd +'\n' + nc +'\n' + ge +'\n' + nm +'\n' + au +'\n' + re +'\n'
        return retorno

    def limpartexto(self):
        n = self.getNome()
        e = self.getEmail()
        c = self.getCpf()
        s = self.getSenha()
        e = self.getEstado()
        c = self.getCidade()
        d = self.getDdd()
        n = self.getNcelular()
        g = self.getGenero()
        n = self.getNmatricula()
        a = self.getAulas()
        r = self.getRenda()
        rtn = n +'\n' + e +'\n' + c +'\n' + s +'\n' + e +'\n' + c +'\n' + d +'\n' + n +'\n' + g +'\n' + n +'\n' + a +'\n' + r +'\n'

    def fecharaba(self):
        x = self.setEvento()
        
