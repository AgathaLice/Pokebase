from Telas import TelaInsercao
from Telas import TelaListagem
from Telas import TelaMenu
from Telas import TelaTutorial
from Telas import TelaVisualizacao

from Controller import Controller

import tkinter as tk #TODO Lembra que isso vai ser o TkCustom depois

class View():
    
    def __init__(self):
        self.root = tk.Tk()
        
        self.controller = Controller(self)
        self.telaMenu = TelaMenu(self)
        self.telaInsercao = TelaInsercao(self)
        self.telaListagem = TelaListagem(self)
        self.telaVisualizacao = TelaVisualizacao(self)
        self.telaTutorial = TelaTutorial(self)
        
        self.inicia()
        
        self.root.bind('<Escape>', self.sair)
        
        self.root.mainloop()

#TODO chamar o controller    
    def sair(self):
        Controller.sair(self)
    
    
    def inicia(self):
        #* Define a janela com as telas, instanciando e desenhando todas.
        #! Chama cada tela, da última a primeira, dando RAISE na TELA DE MENU.
        return None