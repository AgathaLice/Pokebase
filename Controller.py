from Model import Model

class Controller():
    def __init__(self, View):

        self.model = Model()

        self.view = View

    def sair():
        Model.sair()

    def chamarRaise(self, tela):
        self.view.levantarTela(tela)