from Telas import TelaInsercao
from Telas import TelaListagem
from Telas import TelaMenu
from Telas import TelaTutorial
from Telas import TelaVisualizacao

#! VOCÊ NÃO CONSEGUE FAZER CADA TELA EM UM FILE DIFERENTE

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
        
        TelaMenu.menu = tk.Frame(self.root)
        TelaMenu.menu.grid(row = 12,
                  column = 12,
                  rowspan = 12,
                  columnspan = 12,
                  sticky = tk.W+tk.E+tk.N+tk.S)
        
        TelaInsercao.insercao = tk.Frame(self.root)
        TelaInsercao.insercao.grid(row = 12,
                  column = 12,
                  rowspan = 12,
                  columnspan = 12,
                  sticky = tk.W+tk.E+tk.N+tk.S)
        
        TelaListagem.listagem = tk.Frame(self.root)
        TelaListagem.listagem.grid(row = 12,
                  column = 12,
                  rowspan = 12,
                  columnspan = 12,
                  sticky = tk.W+tk.E+tk.N+tk.S)
        
        TelaVisualizacao.visualizacao = tk.Frame(self.root)
        TelaVisualizacao.visualizacao.grid(row = 12,
                  column = 12,
                  rowspan = 12,
                  columnspan = 12,
                  sticky = tk.W+tk.E+tk.N+tk.S)
        
        TelaTutorial.turorial = tk.Frame(self.root)
        TelaTutorial.turorial.grid(row = 12,
                  column = 12,
                  rowspan = 12,
                  columnspan = 12,
                  sticky = tk.W+tk.E+tk.N+tk.S)
        return None