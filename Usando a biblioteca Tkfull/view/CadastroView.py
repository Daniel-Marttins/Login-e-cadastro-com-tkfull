from view.Tkfull import Janela
from controller.CadastroController import CadastroController

class CadastroView:

    vetor = [["Nome:",input],
             ["Email:",input],
             ["CPF:",input],
             ["Senha:",complex],
             ["N.Matricula:",input],
             ["Renda:",input],
             ["N.Celular:",input],
             ["DDD:",('87','81','86','11','17','22')],
             ["Estado:",('Alagoas','Pernambuco','Paraíba','Paraná','Rio de Janeiro','São Paulo')],
             ["Cidade:",('Maceio','Garanhuns','Pará','Curitiba','Praia Grande','São Paulo')],
             ["Genéro:",('Masculino','Feminino')],
             ["Aulas:",('Presenciais','EAD','Semipresenciais')],
             ["*Sair","*Limpar",None,"*Cadastro"]]

    def __init__(self):
        self.cad = Janela()
        self.cad.gerar(self.vetor)
        self.cad.setEvento(27,self.ver)
        self.cad.setEvento(26,self.limpar)
        self.cad.setEvento(25,self.cad.fechar)
        self.cad.start()

    def ver(self):
        inf = CadastroController()
        msg = inf.cadastro(self.cad)
        self.cad.mensagem(msg)

    def limpar(self):
        apg = CadastroController()
        lp = apg.limpartexto(self.cad)

        
