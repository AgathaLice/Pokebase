
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
        
        insercao.rowconfigure([0, 1, 2, 3, 4,
                               5, 6, 7, 8, 9,
                               10, 11, 12, 13,
                               14, 15, 16, 17,
                               18],
                              weight=1)
        insercao.rowconfigure(19, weight=2)
        insercao.columnconfigure(0, weight=9)
        insercao.columnconfigure(1, weight=11)
        
        voltarMenu = tk.Button(insercao,
                               text="Voltar ao Menu")
    
        infoSize = 20
        
        frameApelido = tk.Frame(insercao, background='pink')
        frameApelido.grid(row=0,
                        column=1,
                        sticky='nw',
                        pady=(30, 0))
        apelido = tk.Label(frameApelido,
                           text="Apelido",
                           font=('Yu Gothic UI Semibold', infoSize))
        apelido_E = tk.Entry(frameApelido,
                             width=40,
                             font=('Yu Gothic UI Semibold', infoSize))
        
        frameNivel = tk.Frame(insercao, background='darkblue')
        frameNivel.grid(row=0,
                        column=1,
                        sticky='ne',
                        padx=(0, 60),
                        pady=(30, 0))
        nivel = tk.Label(frameNivel,
                         text="Nível",
                         font=('Yu Gothic UI Semibold', infoSize))
        nivel_E = tk.Entry(frameNivel,
                           width=3,
                           font=('Yu Gothic UI Semibold', infoSize))
        
        frameGenero = tk.Frame(insercao, background='red')
        frameGenero.grid(row=1,
                         column=0,
                         sticky='ne',
                         padx=50)
        genero = tk.Label(frameGenero,
                          text="Gênero",
                          font=('Yu Gothic UI Semibold', infoSize))
        genero_CB = tk.Entry(frameGenero, width=9) #* Combobox
        
        frameNome = tk.Frame(insercao, background='yellow')
        frameNome.grid(row=2,
                       column=0,
                       sticky='ne',
                       padx=50)
        nome = tk.Label(frameNome,
                        text="Nome",
                        font=('Yu Gothic UI Semibold', infoSize))
        nome_E = tk.Entry(frameNome,
                          width=12,
                          font=('Yu Gothic UI Semibold', infoSize))
        
        frameTipoUm = tk.Frame(insercao, background='blue')
        frameTipoUm.grid(row=1,
                        column=0,
                        sticky='nw',
                        padx=(60, 0))
        tipoUm = tk.Label(frameTipoUm,
                          text="Tipo 1",
                          font=('Yu Gothic UI Semibold', infoSize))
        tipoUm_CB = tk.Entry(frameTipoUm, width=8) #* Combobox
        
        frameTipoDois = tk.Frame(insercao, background='darkblue')
        
        tipoDois = tk.Label(frameTipoDois,
                            text="Tipo 2",
                            font=('Yu Gothic UI Semibold', infoSize))
        tipoDois_CB = tk.Entry(frameTipoDois, width=8) #* Combobox
        frameTipoDois.grid(row=2,
                        column=0,
                        sticky='nw',
                        padx=(60, 0))
        
        frameNomeHabilidade = tk.Frame(insercao, background='grey')
        frameNomeHabilidade.grid(row=1,
                                 column=1,
                                 sticky='nw',
                                 padx=(0, 60))
        nomeHabilidade = tk.Label(frameNomeHabilidade,
                                  text="Nome da Habilidade",
                                  font=('Yu Gothic UI Semibold', infoSize))
        nomeHabilidade_E = tk.Entry(frameNomeHabilidade,
                                    width=30,
                                    font=('Yu Gothic UI Semibold', infoSize))
        
        frameItem = tk.Frame(insercao, background='pink')
        frameItem.grid(row=3,
                       column=0,
                       sticky='nw',
                       padx=(60, 0))
        item = tk.Label(frameItem,
                        text="Item",
                        font=('Yu Gothic UI Semibold', infoSize))
        item_E = tk.Entry(frameItem,
                          width=16,
                          font=('Yu Gothic UI Semibold', infoSize))
        
        frameNatureza = tk.Frame(insercao, background='grey')
        frameNatureza.grid(row=4,
                           column=0,
                           sticky='nw',
                           padx=(60, 0))
        natureza = tk.Label(frameNatureza,
                            text="Natureza",
                            font=('Yu Gothic UI Semibold', infoSize))
        natureza_CB = tk.Entry(frameNatureza, width=30) #* Combobox
        
        frameDescHabilidade = tk.Frame(insercao, background='lightgreen')
        frameDescHabilidade.grid(row=2,
                                 column=1,
                                 rowspan=3,
                                 padx=(0, 60))
        descHabilidade = tk.Label(frameDescHabilidade,
                                  text="Descrição da Habilidade",
                                  font=('Yu Gothic UI Semibold', infoSize))
        descHabilidade_Txt = tk.Text(frameDescHabilidade,
                                     width=110,
                                     height=4,
                                     font=('Yu Gothic UI Semibold', 10)) #? Text entry
        
        framePoder = tk.Frame(insercao, background='yellow')
        framePoder.grid(row=5,
                        column=0,
                        sticky='nw',
                        padx=(60, 0))
        nomePoder = tk.Label(framePoder,
                             text="Nome do Poder",
                             font=('Yu Gothic UI Semibold', infoSize))
        nomePoder_E = tk.Entry(framePoder,
                               width=16,
                               font=('Yu Gothic UI Semibold', infoSize))
        
        framePoderStats = tk.Frame(insercao, background='red')
        framePoderStats.grid(row=6,
                             column=0,
                             sticky='nw',
                             padx=(60, 0))
        danoPoder = tk.Label(framePoderStats,
                             text="Dano",
                             font=('Yu Gothic UI Semibold', infoSize))
        danoPoder_E = tk.Entry(framePoderStats,
                               width=3,
                               font=('Yu Gothic UI Semibold', infoSize))
        
        tipoPoder = tk.Label(framePoderStats,
                             text="Tipo",
                             font=('Yu Gothic UI Semibold', infoSize))
        tipoPoder_CB = tk.Entry(framePoderStats, width=8) #? Combobox
        
        pp = tk.Label(framePoderStats,
                      text="PP",
                      font=('Yu Gothic UI Semibold', infoSize))
        pp_E = tk.Entry(framePoderStats,
                        width=2,
                        font=('Yu Gothic UI Semibold', infoSize))
        
        frameTipoDanoPoder = tk.Frame(insercao, background='green')
        frameTipoDanoPoder.grid(row=7,
                                column=0,
                                sticky='nw',
                                padx=(60, 0))
        tipoDeDano = tk.Label(frameTipoDanoPoder,
                              text="ATK ou SP.ATK",
                              font=('Yu Gothic UI Semibold', infoSize))
        tipoDeDano_CB = tk.Entry(frameTipoDanoPoder, width=6) #* Combobox
        
        frameDescPoder = tk.Frame(insercao, background='blue')
        frameDescPoder.grid(row=8,
                            column=0,
                            rowspan=10,
                            sticky='n',
                            padx=(60, 0))
        descPoder = tk.Label(frameDescPoder,
                             text="Descrição e Observações do Poder",
                             font=('Yu Gothic UI Semibold', infoSize))
        descPoder_Txt = tk.Text(frameDescPoder,
                                width=50,
                                height=9,
                                font=('Yu Gothic UI Semibold', 12)) #? Text entry
        
        frameTags = tk.Frame(insercao, background='pink')
        frameTags.grid(row=18,
                       column=0,
                       sticky='nw',
                       pady=(0, 30),
                       padx=(60, 0))
        tags = tk.Label(frameTags,
                        text="Tags",
                        font=('Yu Gothic UI Semibold', infoSize))
        tags_CB = tk.Entry(frameTags, width=30)
        
        
        frameStats = tk.Frame(insercao, background='pink')
        frameStats.grid(row=4,
                        column=1,
                        rowspan=19,
                        sticky='',
                        pady=(0, 30),
                        padx=(0, 60))
        frameStats.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
        frameStats.columnconfigure([0, 1], weight=3)
        frameStats.columnconfigure([2, 3], weight=2)
        
        statsLabelSize = 25
        statsEntrySize = 30
        
        iv = tk.Label(frameStats,
                      text="IV's",
                      font=('Yu Gothic UI Semibold', statsLabelSize))
        ev = tk.Label(frameStats,
                      text="EV's",
                      font=('Yu Gothic UI Semibold', statsLabelSize))
        
        
        hp = tk.Label(frameStats,
                      text="Pontos de Vida",
                      font=('Yu Gothic UI Semibold', statsLabelSize))
        hp_E = tk.Entry(frameStats,
                        highlightthickness=1,
                        font=('Yu Gothic UI Semibold', statsEntrySize),
                        width=4)
        hp_E.configure(highlightbackground="red",
                       highlightcolor="red")
        hpIV_E = tk.Entry(frameStats,
                          highlightthickness=1,
                          font=('Yu Gothic UI Semibold', statsEntrySize),
                          width=4)
        hpIV_E.configure(highlightbackground="red",
                         highlightcolor="red")
        hpEV_E = tk.Entry(frameStats,
                          highlightthickness=1,
                          font=('Yu Gothic UI Semibold', statsEntrySize),
                          width=4)
        hpEV_E.configure(highlightbackground="red",
                         highlightcolor="red")
        
        atk = tk.Label(frameStats,
                       text="Ataque",
                       font=('Yu Gothic UI Semibold', statsLabelSize))
        atk_E = tk.Entry(frameStats,
                         highlightthickness=1,
                         font=('Yu Gothic UI Semibold', statsEntrySize),
                         width=4)
        atk_E.configure(highlightbackground="red",
                        highlightcolor="red")
        atkIV_E = tk.Entry(frameStats,
                           highlightthickness=1,
                           font=('Yu Gothic UI Semibold', statsEntrySize),
                           width=4)
        atkIV_E.configure(highlightbackground="red",
                          highlightcolor="red")
        atkEV_E = tk.Entry(frameStats,
                           highlightthickness=1,
                           font=('Yu Gothic UI Semibold', statsEntrySize),
                           width=4)
        atkEV_E.configure(highlightbackground="red",
                          highlightcolor="red")
        
        defs = tk.Label(frameStats,
                        text="Defesa",
                        font=('Yu Gothic UI Semibold', statsLabelSize))
        defs_E = tk.Entry(frameStats,
                          highlightthickness=1,
                          font=('Yu Gothic UI Semibold', statsEntrySize),
                          width=4)
        defs_E.configure(highlightbackground="red",
                         highlightcolor="red")
        defsIV_E = tk.Entry(frameStats,
                            highlightthickness=1,
                            font=('Yu Gothic UI Semibold', statsEntrySize),
                            width=4)
        defsIV_E.configure(highlightbackground="red",
                           highlightcolor="red")
        defsEV_E = tk.Entry(frameStats,
                            highlightthickness=1,
                            font=('Yu Gothic UI Semibold', statsEntrySize),
                            width=4)
        defsEV_E.configure(highlightbackground="red",
                           highlightcolor="red")
        
        spAtk = tk.Label(frameStats,
                         text="Ataque Especial",
                         font=('Yu Gothic UI Semibold', statsLabelSize))
        spAtk_E = tk.Entry(frameStats,
                           highlightthickness=1,
                           font=('Yu Gothic UI Semibold', statsEntrySize),
                           width=4)
        spAtk_E.configure(highlightbackground="red",
                          highlightcolor="red")
        spAtkIV_E = tk.Entry(frameStats,
                             highlightthickness=1,
                             font=('Yu Gothic UI Semibold', statsEntrySize),
                             width=4)
        spAtkIV_E.configure(highlightbackground="red",
                            highlightcolor="red")
        spAtkEV_E = tk.Entry(frameStats,
                             highlightthickness=1,
                             font=('Yu Gothic UI Semibold', statsEntrySize),
                             width=4)
        spAtkEV_E.configure(highlightbackground="red",
                            highlightcolor="red")
        
        spDefs = tk.Label(frameStats,
                          text="Defesa Especial",
                          font=('Yu Gothic UI Semibold', statsLabelSize))
        spDefs_E = tk.Entry(frameStats,
                            highlightthickness=1,
                            font=('Yu Gothic UI Semibold', statsEntrySize),
                            width=4)
        spDefs_E.configure(highlightbackground="red",
                        highlightcolor="red")
        spDefsIV_E = tk.Entry(frameStats,
                           highlightthickness=1,
                           font=('Yu Gothic UI Semibold', statsEntrySize),
                           width=4)
        spDefsIV_E.configure(highlightbackground="red",
                          highlightcolor="red")
        spDefsEV_E = tk.Entry(frameStats,
                           highlightthickness=1,
                           font=('Yu Gothic UI Semibold', statsEntrySize),
                           width=4)
        spDefsEV_E.configure(highlightbackground="red",
                          highlightcolor="red")
        
        spd = tk.Label(frameStats,
                       text="Velocidade",
                       font=('Yu Gothic UI Semibold', statsLabelSize))
        spd_E = tk.Entry(frameStats,
                         highlightthickness=1,
                         font=('Yu Gothic UI Semibold', statsEntrySize),
                         width=4)
        spd_E.configure(highlightbackground="red",
                        highlightcolor="red")
        spdIV_E = tk.Entry(frameStats,
                           highlightthickness=1,
                           font=('Yu Gothic UI Semibold', statsEntrySize),
                           width=4)
        spdIV_E.configure(highlightbackground="red",
                          highlightcolor="red")
        spdEV_E = tk.Entry(frameStats,
                           highlightthickness=1,
                           font=('Yu Gothic UI Semibold', statsEntrySize),
                           width=4)
        spdEV_E.configure(highlightbackground="red",
                          highlightcolor="red")
        
        frameSalvar = tk.Frame(insercao, background='yellow')
        frameSalvar.grid(row=19,
                        column=0,
                        sticky='nw',
                        padx=(60, 0),
                        pady=(0, 30))
        salvarInfo = tk.Button(frameSalvar,
                               text="Salvar Informações")
        
        voltarMenu.grid(row=0,
                        column=0,
                        sticky='nsw',
                        padx=(60, 0),
                        pady=(30, 0))
        
        apelido.pack(side='left', anchor='nw')
        apelido_E.pack(side='left', anchor='nw')
        
        nivel.pack(side='left', anchor='ne')
        nivel_E.pack(side='left', anchor='ne')
        
        nome.pack(side='left', anchor='ne')
        nome_E.pack(side='left', anchor='ne')
        
        tipoUm.pack(side='left', anchor='w')
        tipoUm_CB.pack(side='left', anchor='w')
        tipoDois.pack(side='left', anchor='w')
        tipoDois_CB.pack(side='left', anchor='w')
        
        genero.pack(side='left', anchor='nw')
        genero_CB.pack(side='left', anchor='nw')
        
        nomeHabilidade.pack(side='left', anchor='ne')
        nomeHabilidade_E.pack(side='left', anchor='ne')
        
        item.pack(side='left', anchor='w')
        item_E.pack(side='left', anchor='w')
        
        natureza.pack(side='left', anchor='w')
        natureza_CB.pack(side='left', anchor='w')
        
        descHabilidade.pack(side='top', anchor='center')
        descHabilidade_Txt.pack(side='top', anchor='center')
        
        nomePoder.pack(side='left', anchor='nw')
        nomePoder_E.pack(side='left', anchor='nw')
        
        danoPoder.pack(side='left', anchor='nw')
        danoPoder_E.pack(side='left', anchor='nw')
        
        tipoPoder.pack(side='left', anchor='nw')
        tipoPoder_CB.pack(side='left', anchor='nw')
        
        pp.pack(side='left', anchor='nw')
        pp_E.pack(side='left', anchor='nw')
        
        tipoDeDano.pack(side='left', anchor='nw')
        tipoDeDano_CB.pack(side='left', anchor='nw')
        
        descPoder.pack(side='top', anchor='center')
        descPoder_Txt.pack(side='top', anchor='center')
        
        tags.pack(side='left', anchor='nw')
        tags_CB.pack(side='left', anchor='nw')
        
        iv.grid(row=0,
                column=2,
                sticky='sew')
        ev.grid(row=0,
                column=3,
                sticky='sew')
        
        hp.grid(row=1,
                column=0,
                sticky='nsew')
        hp_E.grid(row=1,
                  column=1,
                  sticky='nsew')
        hpIV_E.grid(row=1,
                    column=2,
                    sticky='nsew')
        hpEV_E.grid(row=1,
                    column=3,
                    sticky='nsew')
        
        atk.grid(row=2,
                column=0,
                sticky='nsew')
        atk_E.grid(row=2,
                  column=1,
                  sticky='nsew')
        atkIV_E.grid(row=2,
                    column=2,
                    sticky='nsew')
        atkEV_E.grid(row=2,
                    column=3,
                    sticky='nsew')
        
        defs.grid(row=3,
                column=0,
                sticky='nsew')
        defs_E.grid(row=3,
                  column=1,
                  sticky='nsew')
        defsIV_E.grid(row=3,
                    column=2,
                    sticky='nsew')
        defsEV_E.grid(row=3,
                    column=3,
                    sticky='nsew')
        
        spAtk.grid(row=4,
                column=0,
                sticky='nsew')
        spAtk_E.grid(row=4,
                  column=1,
                  sticky='nsew')
        spAtkIV_E.grid(row=4,
                    column=2,
                    sticky='nsew')
        spAtkEV_E.grid(row=4,
                    column=3,
                    sticky='nsew')
        
        spDefs.grid(row=5,
                column=0,
                sticky='nsew')
        spDefs_E.grid(row=5,
                  column=1,
                  sticky='nsew')
        spDefsIV_E.grid(row=5,
                    column=2,
                    sticky='nsew')
        spDefsEV_E.grid(row=5,
                    column=3,
                    sticky='nsew')
        
        spd.grid(row=6,
                column=0,
                sticky='nsew')
        spd_E.grid(row=6,
                  column=1,
                  sticky='nsew')
        spdIV_E.grid(row=6,
                    column=2,
                    sticky='nsew')
        spdEV_E.grid(row=6,
                    column=3,
                    sticky='nsew')
        
        salvarInfo.pack(anchor='se')
        
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