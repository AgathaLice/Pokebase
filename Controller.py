
from Model import Model

class Controller():
    def __init__(self, View):

        self.model = Model()

        self.view = View

    def sair(self):
        self.model.sair()

    def responder(self):
        resposta = self.model.responder()
        if resposta == 1: print("Controller recebeu a resposta")