
from Controller import Controller

from PIL import ImageTk, Image

import tkinter as tk #TODO Lembra que isso vai ser o TkCustom depois
#TODO Refaz por weight

class View():
    
    def __init__(self):
        self.root = tk.Tk()
        
        self.controller = Controller(self)

        self.grids = [i for i in range(12)]
        
        self.backgroundStr = "BackgroundClaro.png"
        self.background = Image.open(self.backgroundStr)
        self.tkBg = ImageTk.PhotoImage(self.background)
        
        pokebola = "IconeNormal.png"
        self.icone = ImageTk.PhotoImage(Image.open(pokebola))
        self.root.iconphoto(True, self.icone)
        
        self.root.grid_rowconfigure(0, 
                                    weight=1, 
                                    uniform=True)
        self.root.grid_columnconfigure(0, 
                                       weight=1, 
                                       uniform=True)

        self.inicia()
        
        self.root.bind('<Escape>', self.sair)
        
        self.root.mainloop()


    def sair(self, evento=None):
        Controller.sair()
    
    
    def inicia(self):
        #* Define a janela com as telas, instanciando e desenhando todas.
        #! Chama cada tela, dando RAISE na TELA DE MENU.
        
        self.root.state("zoomed")
        
        self.menu = self.telaMenu(self.root)
        '''
        self.insercao = self.telaInsercao(self.root)
        self.listagem = self.telaListagem(self.root)
        self.visualizacao = self.telaVisualizacao(self.root)
        self.tutorial = self.telaTutorial(self.root)'''
        
        
        
        self.levantarTela(self.menu)
        print(self.grids)
    
    
    def telaMenu(self, root):
        menu = tk.Frame(self.root)
        menu.grid(row=0, 
                  column=0, 
                  sticky="nsew")

        menu.grid_rowconfigure(self.grids, weight=1, uniform=True)
        menu.grid_columnconfigure(self.grids, weight=1, uniform=True)

        self.bgLabel = tk.Label(menu, 
                                image=self.tkBg)
        self.bgLabel.place(x=0,
                           y=0,
                           relwidth=1,
                           relheight=1)

        eC = tk.Frame(menu, background='yellow', height=10, width=10)
        dC = tk.Frame(menu, background='green', height=10, width=10)
        dB = tk.Frame(menu, background='blue', height=10, width=10)
        eB = tk.Frame(menu, background='pink', height=10, width=10)

        eC.grid(row=0, column=0, columnspan=11, sticky='nsew')
        dC.grid(row=0, column=11, rowspan=11, sticky='nsew')
        dB.grid(row=11, column=1, columnspan=11, sticky='nsew')
        eB.grid(row=1, column=0, rowspan=11, sticky='nsew')
        
        novoPokemon = tk.Button(menu,
                                text="Novo Pokémon",
                                command=self.chamarController)
        novoPokemon.grid(row=3,
                         column=4,
                         columnspan=4,
                         sticky='nsew')
        
        return menu
    '''
    def telaInsercao(self, root):
        insercao = tk.Frame(self.root)
        insercao.grid(row=0,
                  column=0,
                  rowspan=11,
                  columnspan=11,
                  sticky='nsew')
        
        return insercao
    
    def telaListagem(self, root):
        listagem = tk.Frame(self.root)
        listagem.grid(row=0,
                  column=0,
                  rowspan=11,
                  columnspan=11,
                  sticky='nsew')
        
        return listagem
    
    def telaVisualizacao(self, root):
        visualizacao = tk.Frame(self.root)
        visualizacao.grid(row=0,
                  column=0,
                  rowspan=11,
                  columnspan=11,
                  sticky='nsew')
        
        return visualizacao
    
    def telaTutorial(self, root):
        tutorial = tk.Frame(self.root)
        tutorial.grid(row=0,
                  column=0,
                  rowspan=11,
                  columnspan=11,
                  sticky='nsew')
        
        return tutorial
    '''
    
    def levantarTela(self, tela):
        tela.tkraise()
        return None
    
    def chamarController(self):
        self.controller.responder()