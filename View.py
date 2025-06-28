
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
        
        insercao.rowconfigure([1, 11], weight=1)
        insercao.rowconfigure([0, 2, 4, 3, 5, 6, 7, 8], weight=2)
        insercao.rowconfigure(10, weight=4)
        insercao.rowconfigure(9, weight=11)
        insercao.columnconfigure([1, 7], weight=1)
        insercao.columnconfigure(3, weight=2)
        insercao.columnconfigure([2, 4, 5], weight=3)
        insercao.columnconfigure([0, 6], weight=4)

        
        voltarMenu = tk.Button(insercao,
                               text="Voltar ao Menu")
    
        frameApelido = tk.Frame(insercao, background='pink')
        frameApelido.grid(row=0,
                        column=2,
                        columnspan=5,
                        sticky='ns',
                        pady=(30, 0))
        apelido = tk.Label(frameApelido,
                           text="Apelido",
                           font=('Yu Gothic UI Semibold', 16))
        apelido_E = tk.Entry(frameApelido,
                             width=40,
                             font=('Yu Gothic UI Semibold', 16))
        
        frameNivel = tk.Frame(insercao, background='darkblue')
        frameNivel.grid(row=0,
                        column=7,
                        sticky='nse',
                        padx=(0, 60),
                        pady=(30, 0))
        nivel = tk.Label(frameNivel,
                         text="Nível",
                         font=('Yu Gothic UI Semibold', 16))
        nivel_E = tk.Entry(frameNivel,
                           width=3,
                           font=('Yu Gothic UI Semibold', 16))
        
        frameNome = tk.Frame(insercao, background='yellow')
        frameNome.grid(row=1,
                        column=4,
                        columnspan=6,
                        sticky='nse',
                        padx=(0, 60))
        nome = tk.Label(frameNome,
                        text="Nome",
                        font=('Yu Gothic UI Semibold', 16))
        nome_E = tk.Entry(frameNome,
                          width=12,
                          font=('Yu Gothic UI Semibold', 16))
        
        frameTipoUm = tk.Frame(insercao, background='blue')
        frameTipoUm.grid(row=2,
                        column=0,
                        sticky='nw',
                        padx=(60, 0))
        tipoUm = tk.Label(frameTipoUm,
                          text="Tipo 1",
                          font=('Yu Gothic UI Semibold', 16))
        tipoUm_CB = tk.Entry(frameTipoUm, width=8) #* Combobox
        
        frameTipoDois = tk.Frame(insercao, background='darkblue')
        
        tipoDois = tk.Label(frameTipoDois,
                            text="Tipo 2",
                            font=('Yu Gothic UI Semibold', 16))
        tipoDois_CB = tk.Entry(frameTipoDois, width=8) #* Combobox
        frameTipoDois.grid(row=3,
                        column=0,
                        sticky='nw',
                        padx=(60, 0))
        frameGenero = tk.Frame(insercao, background='red')
        frameGenero.grid(row=2,
                         column=1, #!funciona com a coluna 1
                         rowspan=3,
                         columnspan=2,
                         sticky='nw')
        genero = tk.Label(frameGenero,
                          text="Gênero",
                          font=('Yu Gothic UI Semibold', 16))
        genero_CB = tk.Entry(frameGenero, width=9) #* Combobox
        
        frameNomeHabilidade = tk.Frame(insercao, background='grey')
        frameNomeHabilidade.grid(row=2,
                        column=4,
                        columnspan=6,
                        sticky='nsew',
                        padx=(0, 60))
        nomeHabilidade = tk.Label(frameNomeHabilidade,
                                  text="Nome da Habilidade",
                                  font=('Yu Gothic UI Semibold', 16))
        nomeHabilidade_E = tk.Entry(frameNomeHabilidade,
                                    width=30,
                                    font=('Yu Gothic UI Semibold', 16))
        
        frameItem = tk.Frame(insercao, background='pink')
        frameItem.grid(row=4,
                    column=0,
                    columnspan=2,
                    sticky='nwe',
                    padx=(60, 0))
        item = tk.Label(frameItem,
                        text="Item",
                        font=('Yu Gothic UI Semibold', 16))
        item_E = tk.Entry(frameItem,
                          width=16,
                          font=('Yu Gothic UI Semibold', 16))
        
        frameNatureza = tk.Frame(insercao, background='grey')
        frameNatureza.grid(row=5,
                        column=0,
                        columnspan=2,
                        sticky='nwe',
                        padx=(60, 0))
        natureza = tk.Label(frameNatureza,
                            text="Natureza",
                            font=('Yu Gothic UI Semibold', 16))
        natureza_CB = tk.Entry(frameNatureza, width=30) #* Combobox
        
        frameDescHabilidade = tk.Frame(insercao, background='lightgreen')
        frameDescHabilidade.grid(row=3,
                                 column=4,
                                 rowspan=4,
                                 columnspan=6,
                                 sticky='nsew',
                                 padx=(0, 60))
        descHabilidade = tk.Label(frameDescHabilidade,
                                  text="Descrição da Habilidade",
                                  font=('Yu Gothic UI Semibold', 16))
        descHabilidade_Txt = tk.Text(frameDescHabilidade,
                                     width=64,
                                     height=4,
                                     font=('Yu Gothic UI Semibold', 15)) #? Text entry
        
        framePoder = tk.Frame(insercao, background='yellow')
        framePoder.grid(row=6,
                        column=0,
                        columnspan=2,
                        sticky='nwe',
                        padx=(60, 0))
        nomePoder = tk.Label(framePoder,
                             text="Nome do Poder",
                             font=('Yu Gothic UI Semibold', 16))
        nomePoder_E = tk.Entry(framePoder,
                               width=16,
                               font=('Yu Gothic UI Semibold', 16))
        
        framePoderStats = tk.Frame(insercao, background='red')
        framePoderStats.grid(row=7,
                        column=0,
                        columnspan=2,
                        sticky='nsew',
                        padx=(60, 0))
        danoPoder = tk.Label(framePoderStats,
                             text="Dano",
                             font=('Yu Gothic UI Semibold', 16))
        danoPoder_E = tk.Entry(framePoderStats,
                               width=3,
                               font=('Yu Gothic UI Semibold', 16))
        '''
        frameTipoPoder = tk.Frame(insercao, background='grey')
        frameTipoPoder.grid(row=7,
                        column=1,
                        sticky='nsew')'''
        tipoPoder = tk.Label(framePoderStats,
                             text="Tipo",
                             font=('Yu Gothic UI Semibold', 16))
        tipoPoder_CB = tk.Entry(framePoderStats, width=8) #? Combobox
        
        '''framePoderPP = tk.Frame(insercao, background='black')
        framePoderPP.grid(row=7,
                        column=2,
                        sticky='nsew')'''
        pp = tk.Label(framePoderStats,
                      text="PP",
                      font=('Yu Gothic UI Semibold', 16))
        pp_E = tk.Entry(framePoderStats,
                        width=2,
                        font=('Yu Gothic UI Semibold', 16))
        
        frameTipoDanoPoder = tk.Frame(insercao, background='green')
        frameTipoDanoPoder.grid(row=8,
                        column=0,
                        columnspan=2,
                        sticky='nsew',
                        padx=(60, 0))
        tipoDeDano = tk.Label(frameTipoDanoPoder,
                              text="ATK ou SP.ATK",
                              font=('Yu Gothic UI Semibold', 16))
        tipoDeDano_CB = tk.Entry(frameTipoDanoPoder, width=6) #* Combobox
        
        frameDescPoder = tk.Frame(insercao, background='blue')
        frameDescPoder.grid(row=9,
                        column=0,
                        columnspan=2,
                        sticky='nsew',
                        padx=(60, 0))
        descPoder = tk.Label(frameDescPoder,
                             text="Descrição e Observações do Poder",
                             font=('Yu Gothic UI Semibold', 16))
        descPoder_Txt = tk.Text(frameDescPoder,
                                width=50,
                                height=7,
                                font=('Yu Gothic UI Semibold', 15)) #? Text entry
        
        frameTags = tk.Frame(insercao, background='pink')
        frameTags.grid(row=10,
                       column=0,
                       columnspan=1,
                       sticky='nse',
                       pady=(0, 30))
        tags = tk.Label(frameTags,
                        text="Tags",
                        font=('Yu Gothic UI Semibold', 16))
        tags_CB = tk.Entry(frameTags, width=30)
        
        
        frameStats = tk.Frame(insercao, background='pink')
        frameStats.grid(row=5,
                        column=3,
                        rowspan=9,
                        columnspan=6,
                        sticky='nw')
        
        iv = tk.Label(insercao, text="IV's")
        ev = tk.Label(insercao, text="EV's")
        
        hp = tk.Label(insercao, text="Pontos de Vida")
        hp_E = tk.Entry(insercao)
        hpIV_E = tk.Entry(insercao)
        hpEV_E = tk.Entry(insercao)
        
        atk = tk.Label(insercao, text="Ataque")
        atk_E = tk.Entry(insercao)
        atkIV_E = tk.Entry(insercao)
        atkEV_E = tk.Entry(insercao)
        
        defs = tk.Label(insercao, text="Defesa")
        defs_E = tk.Entry(insercao)
        defsIV_E = tk.Entry(insercao)
        defsEV_E = tk.Entry(insercao)
        
        spAtk = tk.Label(insercao, text="Ataque Especial")
        spAtk_E = tk.Entry(insercao)
        spAtkIV_E = tk.Entry(insercao)
        spAtkEV_E = tk.Entry(insercao)
        
        spDefs = tk.Label(insercao, text="Defesa Especial")
        spDefs_E = tk.Entry(insercao)
        spDefsIV_E = tk.Entry(insercao)
        spDefsEV_E = tk.Entry(insercao)
        
        spd = tk.Label(insercao, text="Velocidade")
        spd_E = tk.Entry(insercao)
        spdIV_E = tk.Entry(insercao)
        spdEV_E = tk.Entry(insercao)
        
        frameSalvar = tk.Frame(insercao, background='yellow')
        frameSalvar.grid(row=10,
                        column=5,
                        columnspan=6,
                        sticky='nsw',
                        pady=(0, 30))
        salvarInfo = tk.Button(frameSalvar,
                               text="Salvar Informações")
        
        voltarMenu.grid(row=0,
                        column=0,
                        columnspan=1,
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
        
        genero.pack(side='top', anchor='nw')
        genero_CB.pack(side='top', anchor='nw')
        
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