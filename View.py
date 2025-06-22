
from Controller import Controller

from PIL import Image
#TODO remover imports

#TODO Telas tem um quadrado preto

import customtkinter as ctk
import tkinter as tk

class View():

    def __init__(self):

        ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        self.root = ctk.CTk()

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{str(self.width)}x{str(self.height)}")

        self.controller = Controller(self)

        self.background = ctk.CTkImage(light_image=Image.open("BackgroundClaro.png"),
                                  dark_image=Image.open("BackgroundClaro.png"),
                                  size=(self.width, self.height)) 
        #! Fix: width é um pouco demais, diminuir para imagem não ficar esticada horizontalmente
                                    #size=(1500, 1000)



        '''pokebola = "IconeNormal.png"
        self.icone = ImageTk.PhotoImage(Image.open(pokebola))
        self.root.iconphoto(True, self.icone)'''



        self.root.after(0, lambda:self.root.state('zoomed'))

        self.inicia()

        self.root.bind('<Escape>', self.sair)

        self.levantarTela(self.menu)

        self.root.mainloop()


    def sair(self, evento=None):
        self.controller.sair()


    def inicia(self):
        #* Define a janela com as telas, instanciando e desenhando todas.
        #! Chama cada tela, dando RAISE na TELA DE MENU.


        self.menu = self.telaMenu(self.root)
        self.insercao = self.telaInsercao(self.root)
        self.listagem = self.telaListagem(self.root)
        self.visualizacao = self.telaVisualizacao(self.root)
        self.tutorial = self.telaTutorial(self.root)

        bgLabel = ctk.CTkLabel(self.root,
                               image=self.background)
        bgLabel.place(x=0,
                      y=0)
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)


    def telaMenu(self, root):
        menu = ctk.CTkFrame(self.root)
        menu.grid(row=0,
                  column=0,
                  sticky='nsew')
        
        bgLabel = ctk.CTkLabel(menu,
                               image=self.background)
        bgLabel.place(x=0,
                      y=0)
        
        menu.columnconfigure([0, 2], weight=1)
        menu.columnconfigure(1, weight=1)
        menu.rowconfigure(0, weight=3)
        menu.rowconfigure([1, 3, 4], weight=2)
        menu.rowconfigure(2, weight=1)
        
        novoPoke = ctk.CTkButton(menu,
                                 height=70,
                                 width=450,
                                 corner_radius=40,
                                 text="Novo Pokémon")
        ultimoPoke = ctk.CTkButton(menu,
                                   height=70,
                                   width=450,
                                   corner_radius=40,
                                   text="Último Pokémon")
        listaPoke = ctk.CTkButton(menu,
                                  height=70,
                                  width=450,
                                  corner_radius=40,
                                  text="Lista dos Pokémons")
        tutorial = ctk.CTkButton(menu,
                                 height=70,
                                 width=450,
                                 corner_radius=40,
                                 text="Tutorial")
        
        novoPoke.grid(row=1,
                      column=1,
                      sticky='n')
        ultimoPoke.grid(row=1,
                      column=1,
                      sticky='s')
        listaPoke.grid(row=3,
                      column=1,
                      sticky='n')
        tutorial.grid(row=3,
                      column=1,
                      sticky='s')

        return menu

    def telaInsercao(self, root):
        insercao = ctk.CTkFrame(self.root)
        insercao.grid(row=0,
                  column=0,
                  sticky='nsew')
        
        insercao.columnconfigure(0, weight=1)
        insercao.rowconfigure(0, weight=1)
        
        bgLabel = ctk.CTkLabel(insercao,
                                   image=self.background)
        bgLabel.place(x=0,
                           y=0)

        return insercao

    def telaListagem(self, root):
        listagem = ctk.CTkFrame(self.root)
        listagem.grid(row=0,
                  column=0,
                  sticky='nsew')
        
        listagem.columnconfigure(0, weight=1)
        listagem.rowconfigure(0, weight=1)
        
        bgLabel = ctk.CTkLabel(listagem,
                                   image=self.background)
        bgLabel.place(x=0,
                           y=0)

        return listagem

    def telaVisualizacao(self, root):
        visualizacao = ctk.CTkFrame(self.root)
        visualizacao.grid(row=0,
                  column=0,
                  sticky='nsew')
        
        visualizacao.columnconfigure(0, weight=1)
        visualizacao.rowconfigure(0, weight=1)
        
        bgLabel = ctk.CTkLabel(visualizacao,
                                   image=self.background)
        bgLabel.place(x=0,
                           y=0)

        return visualizacao

    def telaTutorial(self, root):
        tutorial = ctk.CTkFrame(self.root)
        tutorial.grid(row=0,
                  column=0,
                  sticky='nsew')
        
        tutorial.columnconfigure(0, weight=1)
        tutorial.rowconfigure(0, weight=1)
        
        bgLabel = ctk.CTkLabel(tutorial,
                                   image=self.background)
        bgLabel.place(x=0,
                           y=0)

        return tutorial


    def levantarTela(self, tela):
        tela.tkraise()