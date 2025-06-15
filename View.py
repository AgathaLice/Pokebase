
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
        
        pokebola = "C:\\Users\\migue\\Documents\\GitHub\\Pokebase\\IconeNormal.png"
        self.icone = ImageTk.PhotoImage(Image.open(pokebola))
        self.root.iconphoto(True, self.icone)
        
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
        
        self.bgLabel = tk.Label(self.root, 
                                image=self.tkBg)
        self.bgLabel.place(x=0,
                           y=0,
                           relwidth=1,
                           relheight=1)
        
        self.levantarTela(self.menu)
    
    
    def telaMenu(self, root):
        menu = tk.Frame(self.root, background='pink')
        menu.pack()
        
        um = tk.Label(menu, text="1")
        dois = tk.Label(menu, text="2")
        tres = tk.Label(menu, text="3")
        quatro = tk.Label(menu, text="4")
        um.grid(row=0,
               column=0)
        dois.grid(row=0,
               column=1)
        tres.grid(row=0,
               column=2)
        quatro.grid(row=0,
               column=3)
        
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