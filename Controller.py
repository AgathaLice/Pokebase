
from Model import Model

class Controller():
    def __init__(self, View):

        self.model = Model()

        self.view = View

    def sair():
        Model.sair()

    def chamarRaise(self, tela):
        self.view.levantarTela(tela)
    
    def addTagInsercao(self,
                       valor,
                       tagsCB,
                       tagsAtuais,
                       salvar: bool
                       ) -> None | dict:
        novosValoresTags: dict = self.model.addTagInsercao(valor,
                                                           tagsCB,
                                                           tagsAtuais,
                                                           salvar)
        return novosValoresTags
    
    def validacaoNomeAcaoCB(self, valorCB):
        return self.view.validacaoNomeAcaoCB(valorCB)
    
    def chamarRegister(self):
        return self.view.registerValidacaoCB()
    
    def criarListaMoves(self,
                        valorCB,
                        movesCB,
                        contador) -> None | dict:
        return self.model.criarListaMoves(valorCB,
                                          movesCB, 
                                          contador)
    
    def configState(self, combobox, text) -> None:
        self.view.configState(combobox, text)
    
    def chamarEditarMoves(self,
                          contador,
                          movesCB,
                          opcao):
        self.model.editarMoves(contador,
                               movesCB,
                               opcao)
    
    def chamarCurrentCB(self, combobox, index):
        self.view.currentCB(combobox, index)
    
    def chamarInsert(self, widget, text):
        self.view.setInsert(widget, text)
    
    def chamarDelete(self, widget):
        self.view.setDelete(widget)
    
    def salvarMove(self,
                   movesDict,
                   moveAtual,
                   nome,
                   tipo,
                   pp,
                   precisao,
                   categoria,
                   dano,
                   descricao):
        return self.controller.salvarMove(movesDict,
                                          moveAtual,
                                          nome,
                                          tipo,
                                          pp,
                                          precisao,
                                          categoria,
                                          dano,
                                          descricao)
    
    def salvar(self,
               apelido,
               nivel,
               genero,
               nome,
               tipoUm,
               tipoDois,
               nomeHabilidade,
               item,
               natureza,
               descHabilidade,
               nomeAcao,
               tipoAcao,
               pp,
               precisao,
               categoria,
               danoAcao,
               descAcao,
               tags,
               hp,
               hpIV,
               hpEV,
               atk,
               atkIV,
               atkEV,
               defs,
               defsIV,
               defsEV,
               spAtk,
               spAtkIV,
               spAtkEV,
               spDefs,
               spDefsIV,
               spDefsEV,
               spd,
               spdIV,
               spdEV):
        self.model.salvar(apelido,
                               nivel,
                               genero,
                               nome,
                               tipoUm,
                               tipoDois,
                               nomeHabilidade,
                               item,
                               natureza,
                               descHabilidade,
                               nomeAcao,
                               tipoAcao,
                               pp,
                               precisao,
                               categoria,
                               danoAcao,
                               descAcao,
                               tags,
                               hp,
                               hpIV,
                               hpEV,
                               atk,
                               atkIV,
                               atkEV,
                               defs,
                               defsIV,
                               defsEV,
                               spAtk,
                               spAtkIV,
                               spAtkEV,
                               spDefs,
                               spDefsIV,
                               spDefsEV,
                               spd,
                               spdIV,
                               spdEV)