from model.CadastroModel import CadastroModel
class CadastroController:

    def __init__(self):
        pass

    def cadastro(self,cadTkfull):
        dados = CadastroModel()
        dados.setNome(cadTkfull.getTexto(2))
        dados.setEmail(cadTkfull.getTexto(4))
        dados.setCpf(cadTkfull.getTexto(6))
        dados.setSenha(cadTkfull.getTexto(8))
        dados.setEstado(cadTkfull.getTexto(18))
        dados.setCidade(cadTkfull.getTexto(20))
        dados.setDdd(cadTkfull.getTexto(16))
        dados.setNcelular(cadTkfull.getTexto(14))
        dados.setGenero(cadTkfull.getTexto(22))
        dados.setNmatricula(cadTkfull.getTexto(10))
        dados.setAulas(cadTkfull.getTexto(24))
        dados.setRenda(cadTkfull.getTexto(12))
        #return dados.cadastro()

        arq = open("Info.txt","a")
        linhas = arq.writelines(dados.cadastro())

        return("Prontinho, Agora Você Está Cadastrado !")

    def limpartexto(self,cadTkfull):
        a = CadastroModel()
        a.setNome(cadTkfull.apagarTexto(2))
        a.setEmail(cadTkfull.apagarTexto(4))
        a.setCpf(cadTkfull.apagarTexto(6))
        a.setSenha(cadTkfull.apagarTexto(8))
        a.setEstado(cadTkfull.apagarTexto(18))
        a.setCidade(cadTkfull.apagarTexto(20))
        a.setDdd(cadTkfull.apagarTexto(16))
        a.setNcelular(cadTkfull.apagarTexto(14))
        a.setGenero(cadTkfull.apagarTexto(22))
        a.setNmatricula(cadTkfull.apagarTexto(10))
        a.setAulas(cadTkfull.apagarTexto(24))
        a.setRenda(cadTkfull.apagarTexto(12))

    
