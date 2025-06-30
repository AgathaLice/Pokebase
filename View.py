
from Controller import Controller

from PIL import ImageTk, Image

import tkinter as tk
from tkinter import ttk
#TODO -> Chamar uma tela limpa os dados anteriores. chamando duas funções no lambda, uma limpando a tela e a outra dando raise

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

        self.levantarTela(self.menu) #! Estou trabalhando nessa tela atualmente.
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

        menu.columnconfigure([0, 2],
                             weight=1)
        menu.columnconfigure(1,
                             weight=1)
        menu.rowconfigure([0, 3],
                          weight=3)
        menu.rowconfigure([1, 2],
                          weight=1)

        novoPoke = tk.Button(menu,
                             text="Novo Pokémon",
                             command=lambda: self.chamarRaise(self.insercao))
        ultimoPoke = tk.Button(menu,
                               text="Último Pokémon",
                               command=lambda: self.chamarRaise(self.visualizacao))
        listaPoke = tk.Button(menu,
                              text="Lista dos Pokémons",
                              command=lambda: self.chamarRaise(self.listagem))
        tutorial = tk.Button(menu,
                             text="Tutorial",
                             command=lambda: self.chamarRaise(self.tutorial))

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

    #todo -> Personalizar as entrys e labels para coincidir com as cores do programa
    #TODO -> Pronto em relação ao model. Ainda precisa adicionar a funcionalidade de salvar, etc.
    #TODO -> Adicionar mais de um poder
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

        infoSize = 20
        universalFont = 'Yu Gothic UI Semibold'
        corHighlight = "red"
        corLabel = "white"

        insercao.rowconfigure([0, 1, 2, 3, 4,
                               5, 6, 7, 8, 9,
                               10, 11, 12, 13,
                               14, 15, 16, 17,
                               18],
                              weight=1)
        insercao.rowconfigure(19,
                              weight=2)
        insercao.columnconfigure(0,
                                 weight=9)
        insercao.columnconfigure(1,
                                 weight=11)

        voltarMenu = tk.Button(insercao,
                               text="Voltar ao Menu",
                               command=lambda: self.chamarRaise(self.menu))

        frameApelido = tk.Frame(insercao,
                                background=corLabel)
        frameApelido.grid(row=0,
                          column=1,
                          sticky='nw',
                          pady=(30, 0))
        apelido = tk.Label(frameApelido,
                           text="Apelido",
                           font=(universalFont,
                                 infoSize),
                           highlightthickness=2,
                           highlightbackground=corHighlight,
                           highlightcolor=corHighlight,
                           background=corLabel)
        apelido_E = tk.Entry(frameApelido,
                             width=40,
                             font=(universalFont,
                                   infoSize),
                             highlightthickness=2,
                             highlightbackground=corHighlight,
                             highlightcolor=corHighlight)

        frameNivel = tk.Frame(insercao,
                              background=corLabel)
        frameNivel.grid(row=0,
                        column=1,
                        sticky='ne',
                        padx=(0, 60),
                        pady=(30, 0))
        nivel = tk.Label(frameNivel,
                         text="Nível",
                         font=(universalFont,
                               infoSize),
                         highlightthickness=2,
                         highlightbackground=corHighlight,
                         highlightcolor=corHighlight,
                         background=corLabel)
        nivel_E = tk.Entry(frameNivel,
                           width=3,
                           font=(universalFont,
                                 infoSize),
                           highlightthickness=2,
                           highlightbackground=corHighlight,
                           highlightcolor=corHighlight)

        frameGenero = tk.Frame(insercao,
                               background=corLabel)
        frameGenero.grid(row=2,
                         column=0,
                         sticky='ne',
                         padx=30)
        genero = tk.Label(frameGenero,
                          text="Gênero",
                          font=(universalFont,
                                infoSize),
                          highlightthickness=2,
                          highlightbackground=corHighlight,
                          highlightcolor=corHighlight,
                          background=corLabel)
        genero_CB = ttk.Combobox(frameGenero,
                                 width=9,
                                 font=(universalFont,
                                       infoSize),
                                 state="readonly")

        frameNome = tk.Frame(insercao,
                             background=corLabel)
        frameNome.grid(row=1,
                       column=0,
                       sticky='ne',
                       padx=30)
        nome = tk.Label(frameNome,
                        text="Nome",
                        font=(universalFont,
                              infoSize),
                        highlightthickness=2,
                        highlightbackground=corHighlight,
                        highlightcolor=corHighlight,
                        background=corLabel)
        nome_E = tk.Entry(frameNome,
                          width=12,
                          font=(universalFont,
                                infoSize),
                          highlightthickness=2,
                          highlightbackground=corHighlight,
                          highlightcolor=corHighlight)

        frameTipoUm = tk.Frame(insercao,
                               background=corLabel)
        frameTipoUm.grid(row=1,
                         column=0,
                         sticky='nw',
                         padx=(60, 0))
        tipoUm = tk.Label(frameTipoUm,
                          text="Tipo 1",
                          font=(universalFont,
                                infoSize),
                          highlightthickness=2,
                          highlightbackground=corHighlight,
                          highlightcolor=corHighlight,
                          background=corLabel)
        tipoUm_CB = ttk.Combobox(frameTipoUm,
                                 width=8,
                                 font=(universalFont,
                                       infoSize),
                                 state="readonly")

        frameTipoDois = tk.Frame(insercao,
                                 background=corLabel)
        frameTipoDois.grid(row=2,
                           column=0,
                           sticky='nw',
                           padx=(60, 0))
        tipoDois = tk.Label(frameTipoDois,
                            text="Tipo 2",
                            font=(universalFont,
                                  infoSize),
                            highlightthickness=2,
                            highlightbackground=corHighlight,
                            highlightcolor=corHighlight,
                            background=corLabel)
        tipoDois_CB = ttk.Combobox(frameTipoDois,
                                   width=8,
                                   font=(universalFont,
                                         infoSize),
                                   state="readonly")

        frameNomeHabilidade = tk.Frame(insercao,
                                       background=corLabel)
        frameNomeHabilidade.grid(row=1,
                                 column=1,
                                 sticky='nw',
                                 padx=(0, 60))
        nomeHabilidade = tk.Label(frameNomeHabilidade,
                                  text="Nome da Habilidade",
                                  font=(universalFont,
                                        infoSize),
                                  highlightthickness=2,
                                  highlightbackground=corHighlight,
                                  highlightcolor=corHighlight,
                                  background=corLabel)
        nomeHabilidade_E = tk.Entry(frameNomeHabilidade,
                                    width=30,
                                    font=(universalFont,
                                          infoSize),
                                    highlightthickness=2,
                                    highlightbackground=corHighlight,
                                    highlightcolor=corHighlight)

        frameItem = tk.Frame(insercao,
                             background=corLabel)
        frameItem.grid(row=3,
                       column=0,
                       sticky='nw',
                       padx=(60, 0))
        item = tk.Label(frameItem,
                        text="Item",
                        font=(universalFont,
                              infoSize),
                        highlightthickness=2,
                        highlightbackground=corHighlight,
                        highlightcolor=corHighlight,
                        background=corLabel)
        item_E = tk.Entry(frameItem,
                          width=16,
                          font=(universalFont,
                                infoSize),
                          highlightthickness=2,
                          highlightbackground=corHighlight,
                          highlightcolor=corHighlight)

        frameNatureza = tk.Frame(insercao,
                                 background=corLabel)
        frameNatureza.grid(row=4,
                           column=0,
                           sticky='nw',
                           padx=(60, 0))
        natureza = tk.Label(frameNatureza,
                            text="Natureza",
                            font=(universalFont,
                                  infoSize),
                            highlightthickness=2,
                            highlightbackground=corHighlight,
                            highlightcolor=corHighlight,
                            background=corLabel)
        natureza_CB = ttk.Combobox(frameNatureza,
                                   width=30,
                                   font=(universalFont,
                                         infoSize),
                                   state="readonly")

        frameDescHabilidade = tk.Frame(insercao,
                                       background=corLabel)
        frameDescHabilidade.grid(row=2,
                                 column=1,
                                 rowspan=3,
                                 padx=(0, 60))
        descHabilidade = tk.Label(frameDescHabilidade,
                                  text="Descrição da Habilidade",
                                  font=(universalFont,
                                        infoSize),
                                  highlightthickness=2,
                                  highlightbackground=corHighlight,
                                  highlightcolor=corHighlight,
                                  background=corLabel)
        descHabilidade_Txt = tk.Text(frameDescHabilidade,
                                     width=110,
                                     height=8,
                                     font=(universalFont, 10),
                                     highlightthickness=2,
                                     highlightbackground=corHighlight,
                                     highlightcolor=corHighlight)

        framePoder = tk.Frame(insercao,
                              background=corLabel)
        framePoder.grid(row=5,
                        column=0,
                        sticky='nw',
                        padx=(60, 0))
        nomePoder = tk.Label(framePoder,
                             text="Nome do Poder",
                             font=(universalFont,
                                   infoSize),
                             highlightthickness=2,
                             highlightbackground=corHighlight,
                             highlightcolor=corHighlight,
                             background=corLabel)
        nomePoder_E = tk.Entry(framePoder,
                               width=16,
                               font=(universalFont,
                                     infoSize),
                               highlightthickness=2,
                               highlightbackground=corHighlight,
                               highlightcolor=corHighlight)

        framePoderStats = tk.Frame(insercao,
                                   background=corLabel)
        framePoderStats.grid(row=6,
                             column=0,
                             sticky='nw',
                             padx=(60, 0))
        danoPoder = tk.Label(framePoderStats,
                             text="Dano",
                             font=(universalFont,
                                   infoSize),
                             highlightthickness=2,
                             highlightbackground=corHighlight,
                             highlightcolor=corHighlight,
                             background=corLabel)
        danoPoder_E = tk.Entry(framePoderStats,
                               width=3,
                               font=(universalFont,
                                     infoSize),
                               highlightthickness=2,
                               highlightbackground=corHighlight,
                               highlightcolor=corHighlight)

        tipoPoder = tk.Label(framePoderStats,
                             text="Tipo",
                             font=(universalFont,
                                   infoSize),
                             highlightthickness=2,
                             highlightbackground=corHighlight,
                             highlightcolor=corHighlight,
                             background=corLabel)
        tipoPoder_CB = ttk.Combobox(framePoderStats,
                                    width=8,
                                    font=(universalFont,
                                          infoSize),
                                    state="readonly")

        pp = tk.Label(framePoderStats,
                      text="PP",
                      font=(universalFont,
                            infoSize),
                      highlightthickness=2,
                      highlightbackground=corHighlight,
                      highlightcolor=corHighlight,
                      background=corLabel)
        pp_E = tk.Entry(framePoderStats,
                        width=2,
                        font=(universalFont,
                              infoSize),
                        highlightthickness=2,
                        highlightbackground=corHighlight,
                        highlightcolor=corHighlight)

        frameTipoDanoPoder = tk.Frame(insercao,
                                      background=corLabel)
        frameTipoDanoPoder.grid(row=7,
                                column=0,
                                sticky='nw',
                                padx=(60, 0))
        tipoDeDano = tk.Label(frameTipoDanoPoder,
                              text="ATK ou SP.ATK",
                              font=(universalFont,
                                    infoSize),
                              highlightthickness=2,
                              highlightbackground=corHighlight,
                              highlightcolor=corHighlight,
                              background=corLabel)
        tipoDeDano_CB = ttk.Combobox(frameTipoDanoPoder,
                                     width=6,
                                     font=(universalFont,
                                           infoSize),
                                     state="readonly")

        frameDescPoder = tk.Frame(insercao,
                                  background=corLabel)
        frameDescPoder.grid(row=8,
                            column=0,
                            rowspan=10,
                            sticky='n',
                            padx=(60, 0))
        descPoder = tk.Label(frameDescPoder,
                             text="Descrição e Observações do Poder",
                             font=(universalFont,
                                   infoSize),
                             highlightthickness=2,
                             highlightbackground=corHighlight,
                             highlightcolor=corHighlight,
                             background=corLabel)
        descPoder_Txt = tk.Text(frameDescPoder,
                                width=50,
                                height=9,
                                font=(universalFont, 12),
                                highlightthickness=2,
                                highlightbackground=corHighlight,
                                highlightcolor=corHighlight)

        frameTags = tk.Frame(insercao,
                             background=corLabel)
        frameTags.grid(row=18,
                       column=0,
                       sticky='nw',
                       pady=(0, 30),
                       padx=(60, 0))
        tags = tk.Label(frameTags,
                        text="Tags",
                        font=(universalFont,
                              infoSize),
                        highlightthickness=2,
                        highlightbackground=corHighlight,
                        highlightcolor=corHighlight,
                        background=corLabel)
        tags_CB = ttk.Combobox(frameTags,
                               width=30,
                               font=(universalFont,
                                     infoSize),
                               state="readonly")


        frameStats = tk.Frame(insercao,
                              background=corLabel)
        frameStats.grid(row=4,
                        column=1,
                        rowspan=19,
                        pady=(0, 30),
                        padx=(0, 60))
        frameStats.rowconfigure([0, 1, 2, 3, 4, 5, 6],
                                weight=1)
        frameStats.columnconfigure([0, 1],
                                   weight=3)
        frameStats.columnconfigure([2, 3],
                                   weight=2)

        statsLabelSize = 25
        statsEntrySize = 30

        iv = tk.Label(frameStats,
                      text="IV's",
                      font=(universalFont,
                      statsLabelSize),
                      background=corLabel)
        ev = tk.Label(frameStats,
                      text="EV's",
                      font=(universalFont,
                      statsLabelSize),
                      background=corLabel)

        hp = tk.Label(frameStats,
                      text="Pontos de Vida",
                      font=(universalFont,
                      statsLabelSize),
                      background=corLabel)
        hp_E = tk.Entry(frameStats,
                        highlightthickness=1,
                        font=(universalFont,
                              statsEntrySize),
                        width=4,
                        highlightbackground=corHighlight,
                        highlightcolor=corHighlight)
        hpIV_E = tk.Entry(frameStats,
                          highlightthickness=1,
                          font=(universalFont,
                                statsEntrySize),
                          width=4,
                          highlightbackground=corHighlight,
                          highlightcolor=corHighlight)

        hpEV_E = tk.Entry(frameStats,
                          highlightthickness=1,
                          font=(universalFont,
                                statsEntrySize),
                          width=4,
                          highlightbackground=corHighlight,
                          highlightcolor=corHighlight)

        atk = tk.Label(frameStats,
                       text="Ataque",
                       font=(universalFont,
                             statsLabelSize),
                       background=corLabel)
        atk_E = tk.Entry(frameStats,
                         highlightthickness=1,
                         font=(universalFont,
                               statsEntrySize),
                         width=4,
                         highlightbackground=corHighlight,
                         highlightcolor=corHighlight)

        atkIV_E = tk.Entry(frameStats,
                           highlightthickness=1,
                           font=(universalFont,
                                 statsEntrySize),
                           width=4,
                           highlightbackground=corHighlight,
                           highlightcolor=corHighlight)

        atkEV_E = tk.Entry(frameStats,
                           highlightthickness=1,
                           font=(universalFont,
                                 statsEntrySize),
                           width=4,
                           highlightbackground=corHighlight,
                           highlightcolor=corHighlight)

        defs = tk.Label(frameStats,
                        text="Defesa",
                        font=(universalFont,
                              statsLabelSize),
                        background=corLabel)
        defs_E = tk.Entry(frameStats,
                          highlightthickness=1,
                          font=(universalFont,
                                statsEntrySize),
                          width=4,
                          highlightbackground=corHighlight,
                          highlightcolor=corHighlight)

        defsIV_E = tk.Entry(frameStats,
                            highlightthickness=1,
                            font=(universalFont,
                                  statsEntrySize),
                            width=4,
                            highlightbackground=corHighlight,
                            highlightcolor=corHighlight)

        defsEV_E = tk.Entry(frameStats,
                            highlightthickness=1,
                            font=(universalFont,
                                  statsEntrySize),
                            width=4,
                            highlightbackground=corHighlight,
                            highlightcolor=corHighlight)

        spAtk = tk.Label(frameStats,
                         text="Ataque Especial",
                         font=(universalFont,
                               statsLabelSize),
                         background=corLabel)
        spAtk_E = tk.Entry(frameStats,
                           highlightthickness=1,
                           font=(universalFont,
                                 statsEntrySize),
                           width=4,
                           highlightbackground=corHighlight,
                           highlightcolor=corHighlight)

        spAtkIV_E = tk.Entry(frameStats,
                             highlightthickness=1,
                             font=(universalFont,
                                   statsEntrySize),
                             width=4,
                             highlightbackground=corHighlight,
                             highlightcolor=corHighlight)

        spAtkEV_E = tk.Entry(frameStats,
                             highlightthickness=1,
                             font=(universalFont,
                                   statsEntrySize),
                             width=4,
                             highlightbackground=corHighlight,
                             highlightcolor=corHighlight)

        spDefs = tk.Label(frameStats,
                          text="Defesa Especial",
                          font=(universalFont,
                                statsLabelSize),
                          background=corLabel)
        spDefs_E = tk.Entry(frameStats,
                            highlightthickness=1,
                            font=(universalFont,
                                  statsEntrySize),
                            width=4,
                            highlightbackground=corHighlight,
                            highlightcolor=corHighlight)

        spDefsIV_E = tk.Entry(frameStats,
                              highlightthickness=1,
                              font=(universalFont,
                                    statsEntrySize),
                              width=4,
                              highlightbackground=corHighlight,
                              highlightcolor=corHighlight)

        spDefsEV_E = tk.Entry(frameStats,
                              highlightthickness=1,
                              font=(universalFont,
                                    statsEntrySize),
                              width=4,
                              highlightbackground=corHighlight,
                              highlightcolor=corHighlight)

        spd = tk.Label(frameStats,
                       text="Velocidade",
                       font=(universalFont,
                             statsLabelSize),
                       background=corLabel)
        spd_E = tk.Entry(frameStats,
                         highlightthickness=1,
                         font=(universalFont,
                               statsEntrySize),
                         width=4,
                         highlightbackground=corHighlight,
                         highlightcolor=corHighlight)

        spdIV_E = tk.Entry(frameStats,
                           highlightthickness=1,
                           font=(universalFont,
                                 statsEntrySize),
                           width=4,
                           highlightbackground=corHighlight,
                           highlightcolor=corHighlight)

        spdEV_E = tk.Entry(frameStats,
                           highlightthickness=1,
                           font=(universalFont,
                                 statsEntrySize),
                           width=4,
                           highlightbackground=corHighlight,
                           highlightcolor=corHighlight)

        frameSalvar = tk.Frame(insercao,
                               background=corLabel)
        frameSalvar.grid(row=19,
                         column=0,
                         sticky='nw',
                         padx=(60, 0),
                         pady=(0, 30))
        salvarInfo = tk.Button(frameSalvar,
                               text="Salvar Informações")

        voltarMenu.grid(row=0,
                        column=0,
                        sticky='nw',
                        padx=(60, 0),
                        pady=(30, 0))

        apelido.pack(side='left',
                     anchor='nw')
        apelido_E.pack(side='left',
                       anchor='nw')

        nivel.pack(side='left',
                   anchor='ne')
        nivel_E.pack(side='left',
                     anchor='ne')

        nome.pack(side='left',
                  anchor='ne')
        nome_E.pack(side='left',
                    anchor='ne')

        tipoUm.pack(side='left',
                    anchor='w')
        tipoUm_CB.pack(side='left',
                       anchor='w')
        tipoDois.pack(side='left',
                      anchor='w')
        tipoDois_CB.pack(side='left',
                         anchor='w')

        genero.pack(side='left',
                    anchor='nw')
        genero_CB.pack(side='left',
                       anchor='nw')

        nomeHabilidade.pack(side='left',
                            anchor='ne')
        nomeHabilidade_E.pack(side='left',
                              anchor='ne')

        item.pack(side='left',
                  anchor='w')
        item_E.pack(side='left',
                    anchor='w')

        natureza.pack(side='left',
                      anchor='w')
        natureza_CB.pack(side='left',
                         anchor='w')

        descHabilidade.pack(side='top',
                            anchor='center')
        descHabilidade_Txt.pack(side='top',
                                anchor='center')

        nomePoder.pack(side='left',
                       anchor='nw')
        nomePoder_E.pack(side='left',
                         anchor='nw')

        danoPoder.pack(side='left',
                       anchor='nw')
        danoPoder_E.pack(side='left',
                         anchor='nw')

        tipoPoder.pack(side='left',
                       anchor='nw')
        tipoPoder_CB.pack(side='left',
                          anchor='nw')

        pp.pack(side='left',
                anchor='nw')
        pp_E.pack(side='left',
                  anchor='nw')

        tipoDeDano.pack(side='left',
                        anchor='nw')
        tipoDeDano_CB.pack(side='left',
                           anchor='nw')

        descPoder.pack(side='top',
                       anchor='center')
        descPoder_Txt.pack(side='top',
                           anchor='center')

        tags.pack(side='left',
                  anchor='nw')
        tags_CB.pack(side='left',
                     anchor='nw')

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

        pokemonsExemplo = [["Charmander", "João", "Fogo"],
                           ["Pikachu", "Jonas", "Amarelo"],
                           ["Rayquasa", "Jamaica", "Lendário"]]

        listagem.rowconfigure(0,
                              weight=1)
        listagem.rowconfigure(1,
                              weight=100)
        listagem.rowconfigure(2,
                              weight=10)
        listagem.columnconfigure(0,
                                 weight=1)
        listagem.columnconfigure([1, 2],
                                 weight=3)

        labelFontSize = 20
        labelFont = 'Yu Gothic UI Semibold'
        labelBg = 'white'

        nomePokeFrame = tk.Frame(listagem,
                                 background=labelBg)
        nomePokeFrame.grid(row=0,
                           column=0,
                           sticky='nsew')
        nomePokeLabel = tk.Label(nomePokeFrame,
                                 text="Nome do Pokémon",
                                 font=(labelFont,
                                       labelFontSize),
                                 background=labelBg,
                                 justify='center')
        nomePokeEntry = tk.Entry(nomePokeFrame,
                                 width=12,
                                 font=(labelFont,
                                       labelFontSize),
                                 justify='center')
        nomePokeLabel.pack(side='top')
        nomePokeEntry.pack(side='top')

        apelidoPokeFrame = tk.Frame(listagem,
                                    background=labelBg)
        apelidoPokeFrame.grid(row=0,
                              column=1,
                              sticky='nsew')
        apelidoPokeLabel = tk.Label(apelidoPokeFrame,
                                    text="Apelido do Pokémon",
                                    font=(labelFont,
                                          labelFontSize),
                                    background=labelBg,
                                    justify='center')
        apelidoPokeEntry = tk.Entry(apelidoPokeFrame,
                                    width=40,
                                    font=(labelFont,
                                          labelFontSize),
                                    justify='center')
        apelidoPokeLabel.pack(side='top')
        apelidoPokeEntry.pack(side='top')

        tagsPoke = ttk.Combobox(listagem,
                                font=(labelFont,
                                      labelFontSize),
                                state="readonly",
                                justify='center')
        tagsPoke.set(value="Tags")
        tagsPoke.grid(row=0,
                      column=2,
                      sticky='nsew')
        #! Listagem dos Pokémons
        listaPokes = tk.Frame(listagem,
                              background='black')
        listaPokes.grid(row=1,
                        column=0,
                        columnspan=3,
                        sticky='nsew')

        listaPokes.columnconfigure(0,
                                   weight=13)
        listaPokes.columnconfigure(1,
                                   weight=48)
        listaPokes.columnconfigure(2,
                                   weight=21)
        listaPokes.columnconfigure(3,
                                   weight=3)

        rowAtual = 0
        #! EXEMPLO
        #TODO -> Modificar para relacionar com o BD o mais rápido possível
        #TODO -> Modificar a aparência, a funcionalidade sem o Model está ok
        for pokemon in pokemonsExemplo:
            nomePokeLista = tk.Label(listaPokes,
                                     text=pokemon[0],
                                     justify='center',
                                     font=(labelFont,
                                           20))
            nomePokeLista.grid(row=rowAtual,
                               column=0,
                               sticky='nsew')
            apelidoPokeLista = tk.Label(listaPokes,
                                        text=pokemon[1],
                                        justify='center',
                                        font=(labelFont,
                                           20))
            apelidoPokeLista.grid(row=rowAtual,
                                  column=1,
                                  sticky='nsew')
            tagsPokeLista = tk.Label(listaPokes,
                                     text=pokemon[2],
                                     justify='center',
                                     font=(labelFont,
                                           20))
            tagsPokeLista.grid(row=rowAtual,
                               column=2,
                               sticky='nsew')

            radiosPokeLista = tk.Radiobutton(listaPokes)
            radiosPokeLista.grid(row=rowAtual,
                                 column=3,
                                 sticky='nsew')
            rowAtual += 1
#?________________________________________________________________________________________

        botoesFrame = tk.Frame(listagem,
                               background=labelBg)
        botoesFrame.grid(row=2,
                         column=0,
                         columnspan=3,
                         sticky='nsew')
        delTag = tk.Button(botoesFrame,
                               text="- Tag")
        delTag.pack(side='left',
                    padx=(30, 15))
        addTag = tk.Button(botoesFrame,
                           text="+ Tag")
        addTag.pack(side='left',
                    padx=15)

        novoPoke = tk.Button(botoesFrame,
                             text="Novo Pokémon",
                             command=lambda: self.chamarRaise(self.insercao))
        novoPoke.pack(side='left',
                      padx=15)

        voltarMenu = tk.Button(botoesFrame,
                               text="Voltar ao Menu",
                               command=lambda: self.chamarRaise(self.menu))
        voltarMenu.pack(side='left',
                        padx=15)

        verPoke = tk.Button(botoesFrame,
                            text="Vizualizar Pokémon",
                            command=lambda: self.chamarRaise(self.visualizacao))
        verPoke.pack(side='left',
                     padx=15)

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

        seeSize = 20
        seeFont = 'Yu Gothic UI Semibold'

        visualizacao.rowconfigure([0, 1, 2, 3, 4,
                                   5, 6, 7, 8, 9,
                                   10, 11, 12, 13,
                                   14, 15, 16, 17,
                                   18],
                                   weight=1)
        visualizacao.rowconfigure(19,
                                  weight=2)
        visualizacao.columnconfigure(0,
                                     weight=9)
        visualizacao.columnconfigure(1,
                                     weight=11)

        seeCorHighlight = "red"
        seeCorLabel = "white"

        voltarMenu = tk.Button(visualizacao,
                               text="Voltar ao Menu",
                               command=lambda: self.chamarRaise(self.menu))

        frameApelido = tk.Frame(visualizacao)
        frameApelido.grid(row=0,
                          column=1,
                          sticky='nw',
                          pady=(30, 0))
        apelido = tk.Label(frameApelido,
                           text="Apelido",
                           font=(seeFont,
                                 seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        apelido_I = tk.Label(frameApelido,
                             text="<<Apelido>>",
                             font=(seeFont,
                                   seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        frameNivel = tk.Frame(visualizacao)
        frameNivel.grid(row=0,
                        column=1,
                        sticky='ne',
                        padx=(0, 60),
                        pady=(30, 0))
        nivel = tk.Label(frameNivel,
                         text="Nível",
                         font=(seeFont,
                               seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        nivel_I = tk.Label(frameNivel,
                           text="<00>",
                           font=(seeFont,
                                 seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        frameGenero = tk.Frame(visualizacao)
        frameGenero.grid(row=2,
                         column=0,
                         sticky='ne',
                         padx=30)
        genero = tk.Label(frameGenero,
                          text="Gênero",
                          font=(seeFont,
                                seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        genero_I = tk.Label(frameGenero,
                                 text="<<Gênero>>",
                                 font=(seeFont,
                                       seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        frameNome = tk.Frame(visualizacao)
        frameNome.grid(row=1,
                       column=0,
                       sticky='ne',
                       padx=30)
        nome = tk.Label(frameNome,
                        text="Nome",
                        font=(seeFont,
                              seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        nome_I = tk.Label(frameNome,
                          text="<<Nome>>",
                          font=(seeFont,
                                seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        frameTipoUm = tk.Frame(visualizacao)
        frameTipoUm.grid(row=1,
                         column=0,
                         sticky='nw',
                         padx=(60, 0))
        tipoUm = tk.Label(frameTipoUm,
                          text="Tipo 1",
                          font=(seeFont,
                                seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        tipoUm_I = tk.Label(frameTipoUm,
                             text="<<Tipo Um>>",
                             font=(seeFont,
                                   seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        frameTipoDois = tk.Frame(visualizacao)
        frameTipoDois.grid(row=2,
                           column=0,
                           sticky='nw',
                           padx=(60, 0))
        tipoDois = tk.Label(frameTipoDois,
                            text="Tipo 2",
                            font=(seeFont,
                                  seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        tipoDois_I = tk.Label(frameTipoDois,
                                   text="<<Tipo Dois>>",
                                   font=(seeFont,
                                         seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        frameNomeHabilidade = tk.Frame(visualizacao)
        frameNomeHabilidade.grid(row=1,
                                 column=1,
                                 sticky='nw',
                                 padx=(0, 60))
        nomeHabilidade = tk.Label(frameNomeHabilidade,
                                  text="Nome da Habilidade",
                                  font=(seeFont,
                                        seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        nomeHabilidade_I = tk.Label(frameNomeHabilidade,
                                    text="<<Nome da Habilidade>>",
                                    font=(seeFont,
                                          seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        frameItem = tk.Frame(visualizacao)
        frameItem.grid(row=3,
                       column=0,
                       sticky='nw',
                       padx=(60, 0))
        item = tk.Label(frameItem,
                        text="Item",
                        font=(seeFont,
                              seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        item_I = tk.Label(frameItem,
                          text="<<Item>>",
                          font=(seeFont,
                                seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        frameNatureza = tk.Frame(visualizacao)
        frameNatureza.grid(row=4,
                           column=0,
                           sticky='nw',
                           padx=(60, 0))
        natureza = tk.Label(frameNatureza,
                            text="Natureza",
                            font=(seeFont,
                                  seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        natureza_I = tk.Label(frameNatureza,
                              text="<<Natureza>>",
                              font=(seeFont,
                                  seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        frameDescHabilidade = tk.Frame(visualizacao)
        frameDescHabilidade.grid(row=2,
                                 column=1,
                                 rowspan=3,
                                 padx=(0, 60))
        descHabilidade = tk.Label(frameDescHabilidade,
                                  text="Descrição da Habilidade",
                                  font=(seeFont,
                                        seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        descHabilidade_I = tk.Label(frameDescHabilidade,
                                     text="<<Descrição da Habilidade>>",
                                     height=8,
                                     font=(seeFont, 10),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel) #TODO -> label de múltiplas linhas

        framePoder = tk.Frame(visualizacao)
        framePoder.grid(row=5,
                        column=0,
                        sticky='nw',
                        padx=(60, 0))
        nomePoder = tk.Label(framePoder,
                             text="Nome do Poder",
                             font=(seeFont,
                                   seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        nomePoder_I = tk.Label(framePoder,
                               text="<<Nome do Poder>>",
                               font=(seeFont,
                                     seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        framePoderStats = tk.Frame(visualizacao)
        framePoderStats.grid(row=6,
                             column=0,
                             sticky='nw',
                             padx=(60, 0))
        danoPoder = tk.Label(framePoderStats,
                             text="Dano",
                             font=(seeFont,
                                   seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        danoPoder_I = tk.Label(framePoderStats,
                               text="<00>",
                               font=(seeFont,
                                     seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        tipoPoder = tk.Label(framePoderStats,
                             text="Tipo",
                             font=(seeFont,
                                   seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        tipoPoder_I = tk.Label(framePoderStats,
                               text="<Tipo>",
                               font=(seeFont,
                                     seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        pp = tk.Label(framePoderStats,
                      text="PP",
                      font=(seeFont,
                            seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        pp_I = tk.Label(framePoderStats,
                        text="<PP>",
                        font=(seeFont,
                              seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        frameTipoDanoPoder = tk.Frame(visualizacao)
        frameTipoDanoPoder.grid(row=7,
                                column=0,
                                sticky='nw',
                                padx=(60, 0))
        tipoDeDano = tk.Label(frameTipoDanoPoder,
                              text="ATK ou SP.ATK",
                              font=(seeFont,
                                    seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        tipoDeDano_I = tk.Label(frameTipoDanoPoder,
                                text="<<Escalamento de Dano>>",
                                font=(seeFont,
                                      seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        frameDescPoder = tk.Frame(visualizacao)
        frameDescPoder.grid(row=8,
                            column=0,
                            rowspan=10,
                            sticky='n',
                            padx=(60, 0))
        descPoder = tk.Label(frameDescPoder,
                             text="Descrição e Observações do Poder",
                             font=(seeFont,
                                   seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        descPoder_I = tk.Label(frameDescPoder,
                               text="<<Nome>>",
                               height=9,
                               font=(seeFont, 12),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)

        frameTags = tk.Frame(visualizacao)
        frameTags.grid(row=18,
                       column=0,
                       sticky='nw',
                       pady=(0, 30),
                       padx=(60, 0))
        tags = tk.Label(frameTags,
                        text="Tags",
                        font=(seeFont,
                              seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)
        tags_I = tk.Label(frameTags,
                          text="<<Tags>>",
                          font=(seeFont,
                                seeSize),
                           highlightthickness=2,
                           highlightbackground=seeCorHighlight,
                           highlightcolor=seeCorHighlight,
                           background=seeCorLabel)


        frameStats = tk.Frame(visualizacao)
        frameStats.grid(row=4,
                        column=1,
                        rowspan=19,
                        pady=(0, 30),
                        padx=(0, 60))
        frameStats.rowconfigure([0, 1, 2, 3, 4, 5, 6],
                                weight=1)
        frameStats.columnconfigure([0, 1],
                                   weight=3)
        frameStats.columnconfigure([2, 3],
                                   weight=2)

        statsLabelSize = 25

        iv = tk.Label(frameStats,
                      text="IV's",
                      font=(seeFont,
                      statsLabelSize),
                      background=seeCorLabel)
        ev = tk.Label(frameStats,
                      text="EV's",
                      font=(seeFont,
                      statsLabelSize),
                      background=seeCorLabel)


        hp = tk.Label(frameStats,
                      text="Pontos de Vida",
                      font=(seeFont,
                      statsLabelSize),
                      background=seeCorLabel)
        hp_I = tk.Label(frameStats,
                        highlightthickness=1,
                        text="<<HP>>",
                        font=(seeFont,
                              statsLabelSize),
                        width=4,
                        highlightbackground="red",
                        highlightcolor="red",
                        background=seeCorLabel)
        hpIV_I = tk.Label(frameStats,
                          highlightthickness=1,
                          text="<<HP IV>>",
                          font=(seeFont,
                                statsLabelSize),
                          width=4,
                          highlightbackground="red",
                          highlightcolor="red",
                          background=seeCorLabel)

        hpEV_I = tk.Label(frameStats,
                          highlightthickness=1,
                          text="<<HP EV>>",
                          font=(seeFont,
                                statsLabelSize),
                          width=4,
                          highlightbackground="red",
                          highlightcolor="red",
                          background=seeCorLabel)

        atk = tk.Label(frameStats,
                       text="Ataque",
                       font=(seeFont,
                             statsLabelSize),
                       background=seeCorLabel)
        atk_I = tk.Label(frameStats,
                         highlightthickness=1,
                         text="<<ATK>>",
                         font=(seeFont,
                               statsLabelSize),
                         width=4,
                         highlightbackground="red",
                         highlightcolor="red",
                         background=seeCorLabel)

        atkIV_I = tk.Label(frameStats,
                           highlightthickness=1,
                           text="<<ATK IV>>",
                           font=(seeFont,
                                 statsLabelSize),
                           width=4,
                           highlightbackground="red",
                           highlightcolor="red",
                           background=seeCorLabel)

        atkEV_I = tk.Label(frameStats,
                           highlightthickness=1,
                           text="<<ATK EV>>",
                           font=(seeFont,
                                 statsLabelSize),
                           width=4,
                           highlightbackground="red",
                           highlightcolor="red",
                           background=seeCorLabel)

        defs = tk.Label(frameStats,
                        text="Defesa",
                        font=(seeFont,
                              statsLabelSize),
                        background=seeCorLabel)
        defs_I = tk.Label(frameStats,
                          highlightthickness=1,
                          text="<<DEFS>>",
                          font=(seeFont,
                                statsLabelSize),
                          width=4,
                          highlightbackground="red",
                          highlightcolor="red",
                          background=seeCorLabel)

        defsIV_I = tk.Label(frameStats,
                            highlightthickness=1,
                            text="<<DEFS IV>>",
                            font=(seeFont,
                                  statsLabelSize),
                            width=4,
                            highlightbackground="red",
                            highlightcolor="red",
                            background=seeCorLabel)

        defsEV_I = tk.Label(frameStats,
                            highlightthickness=1,
                            text="<<DEFS EV>>",
                            font=(seeFont,
                                  statsLabelSize),
                            width=4,
                            highlightbackground="red",
                            highlightcolor="red",
                            background=seeCorLabel)

        spAtk = tk.Label(frameStats,
                         text="Ataque Especial",
                         font=(seeFont,
                               statsLabelSize),
                         background=seeCorLabel)
        spAtk_I = tk.Label(frameStats,
                           highlightthickness=1,
                           text="<<SP.ATK>>",
                           font=(seeFont,
                                 statsLabelSize),
                           width=4,
                           highlightbackground="red",
                           highlightcolor="red",
                           background=seeCorLabel)

        spAtkIV_I = tk.Label(frameStats,
                             highlightthickness=1,
                             text="<<SP.ATK IV>>",
                             font=(seeFont,
                                   statsLabelSize),
                             width=4,
                             highlightbackground="red",
                             highlightcolor="red",
                             background=seeCorLabel)

        spAtkEV_I = tk.Label(frameStats,
                             highlightthickness=1,
                             text="<<SP.ATK EV>>",
                             font=(seeFont,
                                   statsLabelSize),
                             width=4,
                             highlightbackground="red",
                             highlightcolor="red",
                             background=seeCorLabel)

        spDefs = tk.Label(frameStats,
                          text="Defesa Especial",
                          font=(seeFont,
                                statsLabelSize),
                          background=seeCorLabel)
        spDefs_I = tk.Label(frameStats,
                            highlightthickness=1,
                            text="<<SP.DEFS>>",
                            font=(seeFont,
                                  statsLabelSize),
                            width=4,
                            highlightbackground="red",
                            highlightcolor="red",
                            background=seeCorLabel)

        spDefsIV_I = tk.Label(frameStats,
                              highlightthickness=1,
                              text="<<SP.DEFS IV>>",
                              font=(seeFont,
                                    statsLabelSize),
                              width=4,
                              highlightbackground="red",
                              highlightcolor="red",
                              background=seeCorLabel)

        spDefsEV_I = tk.Label(frameStats,
                              highlightthickness=1,
                              text="<<SP.DEFS EV>>",
                              font=(seeFont,
                                    statsLabelSize),
                              width=4,
                              highlightbackground="red",
                              highlightcolor="red",
                              background=seeCorLabel)

        spd = tk.Label(frameStats,
                       text="Velocidade",
                       font=(seeFont,
                             statsLabelSize),
                       background=seeCorLabel)
        spd_I = tk.Label(frameStats,
                         highlightthickness=1,
                         text="<<SPD>>",
                         font=(seeFont,
                               statsLabelSize),
                         width=4,
                         highlightbackground="red",
                         highlightcolor="red",
                         background=seeCorLabel)

        spdIV_I = tk.Label(frameStats,
                           highlightthickness=1,
                           text="<<SPD IV>>",
                           font=(seeFont,
                                 statsLabelSize),
                           width=4,
                           highlightbackground="red",
                           highlightcolor="red",
                           background=seeCorLabel)

        spdEV_I = tk.Label(frameStats,
                           highlightthickness=1,
                           text="<<SPD EV>>",
                           font=(seeFont,
                                 statsLabelSize),
                           width=4,
                           highlightbackground="red",
                           highlightcolor="red",
                           background=seeCorLabel)

        frameSalvar = tk.Frame(visualizacao)
        frameSalvar.grid(row=19,
                         column=0,
                         sticky='nw',
                         padx=(60, 0),
                         pady=(0, 30))
        salvarInfo = tk.Button(frameSalvar,
                               text="Salvar Informações")

        voltarMenu.grid(row=0,
                        column=0,
                        sticky='nw',
                        padx=(60, 0),
                        pady=(30, 0))

        apelido.pack(side='left',
                     anchor='nw')
        apelido_I.pack(side='left',
                       anchor='nw')

        nivel.pack(side='left',
                   anchor='ne')
        nivel_I.pack(side='left',
                     anchor='ne')

        nome.pack(side='left',
                  anchor='ne')
        nome_I.pack(side='left',
                    anchor='ne')

        tipoUm.pack(side='left',
                    anchor='w')
        tipoUm_I.pack(side='left',
                       anchor='w')
        tipoDois.pack(side='left',
                      anchor='w')
        tipoDois_I.pack(side='left',
                         anchor='w')

        genero.pack(side='left',
                    anchor='nw')
        genero_I.pack(side='left',
                       anchor='nw')

        nomeHabilidade.pack(side='left',
                            anchor='ne')
        nomeHabilidade_I.pack(side='left',
                              anchor='ne')

        item.pack(side='left',
                  anchor='w')
        item_I.pack(side='left',
                    anchor='w')

        natureza.pack(side='left',
                      anchor='w')
        natureza_I.pack(side='left',
                         anchor='w')

        descHabilidade.pack(side='top',
                            anchor='center')
        descHabilidade_I.pack(side='top',
                                anchor='center')

        nomePoder.pack(side='left',
                       anchor='nw')
        nomePoder_I.pack(side='left',
                         anchor='nw')

        danoPoder.pack(side='left',
                       anchor='nw')
        danoPoder_I.pack(side='left',
                         anchor='nw')

        tipoPoder.pack(side='left',
                       anchor='nw')
        tipoPoder_I.pack(side='left',
                          anchor='nw')

        pp.pack(side='left',
                anchor='nw')
        pp_I.pack(side='left',
                  anchor='nw')

        tipoDeDano.pack(side='left',
                        anchor='nw')
        tipoDeDano_I.pack(side='left',
                           anchor='nw')

        descPoder.pack(side='top',
                       anchor='center')
        descPoder_I.pack(side='top',
                           anchor='center')

        tags.pack(side='left',
                  anchor='nw')
        tags_I.pack(side='left',
                     anchor='nw')

        iv.grid(row=0,
                column=2,
                sticky='sew')
        ev.grid(row=0,
                column=3,
                sticky='sew')

        hp.grid(row=1,
                column=0,
                sticky='nsew')
        hp_I.grid(row=1,
                  column=1,
                  sticky='nsew')
        hpIV_I.grid(row=1,
                    column=2,
                    sticky='nsew')
        hpEV_I.grid(row=1,
                    column=3,
                    sticky='nsew')

        atk.grid(row=2,
                 column=0,
                 sticky='nsew')
        atk_I.grid(row=2,
                   column=1,
                   sticky='nsew')
        atkIV_I.grid(row=2,
                     column=2,
                     sticky='nsew')
        atkEV_I.grid(row=2,
                     column=3,
                     sticky='nsew')

        defs.grid(row=3,
                  column=0,
                  sticky='nsew')
        defs_I.grid(row=3,
                    column=1,
                    sticky='nsew')
        defsIV_I.grid(row=3,
                      column=2,
                      sticky='nsew')
        defsEV_I.grid(row=3,
                      column=3,
                      sticky='nsew')

        spAtk.grid(row=4,
                   column=0,
                   sticky='nsew')
        spAtk_I.grid(row=4,
                     column=1,
                     sticky='nsew')
        spAtkIV_I.grid(row=4,
                       column=2,
                       sticky='nsew')
        spAtkEV_I.grid(row=4,
                       column=3,
                       sticky='nsew')

        spDefs.grid(row=5,
                    column=0,
                    sticky='nsew')
        spDefs_I.grid(row=5,
                      column=1,
                      sticky='nsew')
        spDefsIV_I.grid(row=5,
                        column=2,
                        sticky='nsew')
        spDefsEV_I.grid(row=5,
                        column=3,
                        sticky='nsew')

        spd.grid(row=6,
                 column=0,
                 sticky='nsew')
        spd_I.grid(row=6,
                   column=1,
                   sticky='nsew')
        spdIV_I.grid(row=6,
                     column=2,
                     sticky='nsew')
        spdEV_I.grid(row=6,
                     column=3,
                     sticky='nsew')

        salvarInfo.pack(anchor='se')

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


    def chamarRaise(self, tela):
        self.controller.chamarRaise(tela)

    def levantarTela(self, tela):
        tela.tkraise()
        return None

    def chamarController(self):
        self.controller.responder()