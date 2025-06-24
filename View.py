
from Controller import Controller

from PIL import ImageTk, Image

import tkinter as tk
#TODO -> Refazer o design das telas de dados no figma

class View():
    
    def __init__(self):
        self.root = tk.Tk()
        
        self.controller = Controller(self)
        
        self.backgroundStr = "Imagens\\BackgroundClaro.png"
        self.background = Image.open(self.backgroundStr)
        self.tkBg = ImageTk.PhotoImage(self.background)
        
        pokebola = "Imagens\\IconeNormal.png"
        self.icone = ImageTk.PhotoImage(Image.open(pokebola))
        self.root.iconphoto(True, self.icone)
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        

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
        self.insercao = self.telaInsercao(self.root)
        self.listagem = self.telaListagem(self.root)
        self.visualizacao = self.telaVisualizacao(self.root)
        self.tutorial = self.telaTutorial(self.root)

        self.levantarTela(self.insercao) #! Estou trabalhando nessa tela atualmente.
        #todo Vai ser a tela de menu no futuro.
    
    
    def telaMenu(self, root):
        menu = tk.Frame(self.root)
        menu.grid(row=0,
                  column=0,
                  sticky='nsew')
        
        self.bgLabel = tk.Label(menu, 
                                image=self.tkBg)
        self.bgLabel.place(x=0,
                           y=0,
                           relwidth=1,
                           relheight=1)
        
        menu.columnconfigure([0, 2], weight=1)
        menu.columnconfigure(1, weight=1)
        menu.rowconfigure([0, 3], weight=3)
        menu.rowconfigure([1, 2], weight=1)
        
        novoPoke = tk.Button(menu,
                             text="Novo Pokémon",
                             command=lambda: self.levantarTela(self.insercao))
        ultimoPoke = tk.Button(menu,
                               text="Último Pokémon",
                               command=lambda: self.levantarTela(self.visualizacao))
        listaPoke = tk.Button(menu,
                              text="Lista dos Pokémons",
                              command=lambda: self.levantarTela(self.listagem))
        tutorial = tk.Button(menu,
                             text="Tutorial",
                             command=lambda: self.levantarTela(self.tutorial))
        
        novoPoke.grid(row=1,
                      column=1,
                      sticky='n')
        ultimoPoke.grid(row=1,
                      column=1,
                      sticky='s',
                      pady=125)
        listaPoke.grid(row=2,
                      column=1,
                      sticky='n',
                      pady=125)
        tutorial.grid(row=2,
                      column=1,
                      sticky='s')

        return menu
    
    
    def telaInsercao(self, root):
        insercao = tk.Frame(self.root)
        insercao.grid(row=0,
                  column=0,
                  sticky='nsew')
        
        self.bgLabel = tk.Label(insercao, 
                                image=self.tkBg)
        self.bgLabel.place(x=0,
                           y=0,
                           relwidth=1,
                           relheight=1)
        
        insercao.rowconfigure([0, 2, 7], weight=1)
        insercao.rowconfigure([1, 3, 6], weight=2)
        insercao.rowconfigure(4, weight=3)
        insercao.rowconfigure(5, weight=8)
        insercao.columnconfigure([0, 4], weight=1)
        insercao.columnconfigure(1, weight=4)
        insercao.columnconfigure(2, weight=5)
        insercao.columnconfigure(3, weight=9)
        
        return insercao
    
    
    def telaListagem(self, root):
        listagem = tk.Frame(self.root)
        listagem.grid(row=0,
                  column=0,
                  sticky='nsew')
        
        self.bgLabel = tk.Label(listagem, 
                                image=self.tkBg)
        self.bgLabel.place(x=0,
                           y=0,
                           relwidth=1,
                           relheight=1)
        
        return listagem
    
    
    def telaVisualizacao(self, root):
        visualizacao = tk.Frame(self.root)
        visualizacao.grid(row=0,
                  column=0,
                  sticky='nsew')
        
        self.bgLabel = tk.Label(visualizacao, 
                                image=self.tkBg)
        self.bgLabel.place(x=0,
                           y=0,
                           relwidth=1,
                           relheight=1)
        
        return visualizacao
    
    
    def telaTutorial(self, root):
        tutorial = tk.Frame(self.root)
        tutorial.grid(row=0,
                  column=0,
                  sticky='nsew')
        
        self.bgLabel = tk.Label(tutorial, 
                                image=self.tkBg)
        self.bgLabel.place(x=0,
                           y=0,
                           relwidth=1,
                           relheight=1)
        
        return tutorial
    
    
    def levantarTela(self, tela):
        tela.tkraise()
        return None
    
    def chamarController(self):
        self.controller.responder()