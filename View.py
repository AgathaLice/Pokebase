
from Controller import Controller

from PIL import ImageTk, Image
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

        '''backgroundStr = "BackgroundClaro.png"
        background = Image.open(backgroundStr)
        self.tkBg = ImageTk.PhotoImage(background)'''

        self.background = ctk.CTkImage(light_image=Image.open("BackgroundClaro.png"),
                                  dark_image=Image.open("BackgroundClaro.png"),
                                  size=(self.width, self.height))
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
        Controller.sair()


    def inicia(self):
        #* Define a janela com as telas, instanciando e desenhando todas.
        #! Chama cada tela, dando RAISE na TELA DE MENU.


        self.menu = self.telaMenu(self.root)
        self.insercao = self.telaInsercao(self.root)
        self.listagem = self.telaListagem(self.root)
        self.visualizacao = self.telaVisualizacao(self.root)
        self.tutorial = self.telaTutorial(self.root)

        self.bgLabel = ctk.CTkLabel(self.root,
                                   image=self.background)
        self.bgLabel.place(x=0,
                           y=0)


    def telaMenu(self, root):
        menu = ctk.CTkFrame(self.root)
        menu.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky='nsew')

        return menu

    def telaInsercao(self, root):
        insercao = ctk.CTkFrame(self.root)
        insercao.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky='nsew')

        return insercao

    def telaListagem(self, root):
        listagem = ctk.CTkFrame(self.root)
        listagem.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky='nsew')

        return listagem

    def telaVisualizacao(self, root):
        visualizacao = ctk.CTkFrame(self.root)
        visualizacao.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky='nsew')

        return visualizacao

    def telaTutorial(self, root):
        tutorial = ctk.CTkFrame(self.root)
        tutorial.grid(row=12,
                  column=12,
                  rowspan=12,
                  columnspan=12,
                  sticky='nsew')

        return tutorial


    def levantarTela(self, tela):
        tela.tkraise()