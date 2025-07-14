
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
    
    def configState(self, combobox, text) -> None:
        self.view.configState(combobox, text)
    
    def chamarCurrentCB(self, combobox, index):
        self.view.currentCB(combobox, index)
    
    def chamarInsert(self, widget, text):
        self.view.setInsert(widget, text)
    
    def chamarDelete(self, widget):
        self.view.setDelete(widget)
    
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
    
    def getInt(self, valor):
        return self.model.getInt(valor)

    def pokemonsLista(self):
        return self.model.pokemonsLista()
    
    def verPoke(self, valor):
        return self.model.verPoke(valor)
    
    def ultimoPoke(self):
        return self.model.ultimoPoke()
    
    def chamarReView(self,
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
                     tipoDeDano,
                     danoAcao,
                     descAcao,
                     tags,
                     hp,
                     hpIV,
                     hpEV,
                     hpTotal,
                     atk,
                     atkIV,
                     atkEV,
                     atkTotal,
                     defs,
                     defsIV,
                     defsEV,
                     defsTotal,
                     spAtk,
                     spAtkIV,
                     spAtkEV,
                     spAtkTotal,
                     spDefs,
                     spDefsIV,
                     spDefsEV,
                     spDefsTotal,
                     spd,
                     spdIV,
                     spdEV,
                     spdTotal):
        self.view.mudarApelido(apelido)
        self.view.mudarNivel(nivel)
        self.view.mudarGenero(genero)
        self.view.mudarNome(nome)
        self.view.mudarTipoUm(tipoUm)
        self.view.mudarTipoDois(tipoDois)
        self.view.mudarNomeHabilidade(nomeHabilidade)
        self.view.mudarItem(item)
        self.view.mudarNatureza(natureza)
        self.view.mudarDescHabilidade(descHabilidade)
        self.view.mudarNomeAcao(nomeAcao)
        self.view.mudarTipoAcao(tipoAcao)
        self.view.mudarPp(pp)
        self.view.mudarPrecisao(precisao)
        self.view.mudarTipoDeDano(tipoDeDano)
        self.view.mudarDanoAcao(danoAcao)
        self.view.mudarDescAcao(descAcao)
        self.view.mudarTags(tags)
        self.view.mudarHp(hp)
        self.view.mudarHpIV(hpIV)
        self.view.mudarHpEV(hpEV)
        self.view.mudarHpTotal(hpTotal)
        self.view.mudarAtk(atk)
        self.view.mudarAtkIV(atkIV)
        self.view.mudarAtkEV(atkEV)
        self.view.mudarAtkTotal(atkTotal)
        self.view.mudarDefs(defs)
        self.view.mudarDefsIV(defsIV)
        self.view.mudarDefsEV(defsEV)
        self.view.mudarDefsTotal(defsTotal)
        self.view.mudarSpAtk(spAtk)
        self.view.mudarSpAtkIV(spAtkIV)
        self.view.mudarSpAtkEV(spAtkEV)
        self.view.mudarSpAtkTotal(spAtkTotal)
        self.view.mudarSpDefs(spDefs)
        self.view.mudarSpDefsIV(spDefsIV)
        self.view.mudarSpDefsEV(spDefsEV)
        self.view.mudarSpDefsTotal(spDefsTotal)
        self.view.mudarSpd(spd)
        self.view.mudarSpdIV(spdIV)
        self.view.mudarSpdEV(spdEV)
        self.view.mudarSpdTotal(spdTotal)
    
    def delTag(self, lista, valor):
        return self.model.delTag(lista, valor)