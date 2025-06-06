
import sys
from Controller import Controller

import tkinter as tk #TODO Lembra que isso vai ser o TkCustom depois

class View():
    
    def __init__(self):
        self.root = tk.Tk()
        
        self.controller = Controller(self)
        
        self.inicia()
        
        self.root.bind('<Escape>', self.sair)
        
        self.root.mainloop()


    def sair(self, evento=None):
        Controller.sair()
    
    
    def inicia(self):
        #* Define a janela com as telas, instanciando e desenhando todas.
        #! Chama cada tela, da última a primeira, dando RAISE na TELA DE MENU.
        
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.state("zoomed")
        
        menu = tk.Frame(self.root)
        menu.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky='nsew')
        
        
        insercao = tk.Frame(self.root)
        insercao.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky=tk.W+tk.E+tk.N+tk.S)
        
        listagem = tk.Frame(self.root)
        listagem.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky=tk.W+tk.E+tk.N+tk.S)
        
        visualizacao = tk.Frame(self.root)
        visualizacao.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky=tk.W+tk.E+tk.N+tk.S)
        
        turorial = tk.Frame(self.root)
        turorial.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky=tk.W+tk.E+tk.N+tk.S)
        
        
        menu.tkraise()


"""

"""