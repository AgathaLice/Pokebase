
from Controller import Controller

from PIL import ImageTk, Image

import tkinter as tk #TODO Lembra que isso vai ser o TkCustom depois

class View():
    
    def __init__(self):
        self.root = tk.Tk()
        
        self.controller = Controller(self)
        
        backgroundStr = "C:\\Users\\migue\\Documents\\GitHub\\Pokebase\\BackgroundClaro.png"
        background = Image.open(backgroundStr)
        self.tkBg = ImageTk.PhotoImage(background)
        
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
        
        self.menu = self.telaMenu(self.root)
        self.insercao = self.telaInsercao(self.root)
        self.listagem = self.telaListagem(self.root)
        self.visualizacao = self.telaVisualizacao(self.root)
        self.tutorial = self.telaTutorial(self.root)
        
        self.menu.tkraise()
    
    
    def telaMenu(self, root):
        menu = tk.Frame(self.root)
        menu.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky='nsew')
        self.bgLabel = tk.Label(self.root, 
                                image=self.tkBg)
        self.bgLabel.place(x=0,
                           y=0,
                           relwidth=1,
                           relheight=1)
        
        return menu
    
    def telaInsercao(self, root):
        insercao = tk.Frame(self.root)
        insercao.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky='nsew')
        
        return insercao
    
    def telaListagem(self, root):
        listagem = tk.Frame(self.root)
        listagem.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky='nsew')
        
        return listagem
    
    def telaVisualizacao(self, root):
        visualizacao = tk.Frame(self.root)
        visualizacao.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky='nsew')
        
        return visualizacao
    
    def telaTutorial(self, root):
        tutorial = tk.Frame(self.root)
        tutorial.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky='nsew')
        
        return tutorial
    
    
    def levantarTela(self, tela):
        self.tela.tkraise()