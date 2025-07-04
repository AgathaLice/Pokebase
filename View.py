
from Controller import Controller

from PIL import ImageTk, Image

import tkinter as tk
from tkinter import ttk
#TODO -> Chamar uma tela limpa os dados anteriores. chamando duas funções no lambda, uma limpando a tela e a outra dando raise

class View():

    def __init__(self):
        self.root = tk.Tk()

        self.controller = Controller(self)

        self.backgroundStr = "Imagens\\Backgrounds\\BackgroundClaro.png"
        self.background = Image.open(self.backgroundStr)
        self.tkBg = ImageTk.PhotoImage(self.background)

        pokebola = "Imagens\\Icones\\IconeNormal.png"
        self.icone = ImageTk.PhotoImage(Image.open(pokebola))
        self.root.iconphoto(True, self.icone)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)


        self.inicia()

        self.root.bind("<Escape>", self.sair)

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
                  sticky="nsew")

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
                      sticky="n")
        ultimoPoke.grid(row=1,
                      column=1,
                      sticky="s",
                      pady=125)
        listaPoke.grid(row=2,
                      column=1,
                      sticky="n",
                      pady=125)
        tutorial.grid(row=2,
                      column=1,
                      sticky="s")

        return menu

    #todo -> Personalizar os botões
    #TODO -> Pronto em relação ao model. Ainda precisa adicionar a funcionalidade de salvar, etc.
    #TODO -> Adicionar mais de uma ação
    def telaInsercao(self, root):
        insercao = tk.Frame(self.root)
        insercao.grid(row=0,
                      column=0,
                      sticky="nsew")

        self.bgLabel = tk.Label(insercao,
                                image=self.tkBg)
        self.bgLabel.place(x=0,
                           y=0,
                           relwidth=1,
                           relheight=1)

        corLabel = "white"
        argsPadraoInsercao = {
              "font": ('Yu Gothic UI Semibold', 20),
              "highlightthickness": 2,
              "highlightbackground": "red",
              "highlightcolor": "red",
        }
        argsFonte = {"font": ('Yu Gothic UI Semibold', 20)}

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
                          sticky="nw",
                          pady=(30, 0))
        apelido = tk.Label(frameApelido,
                           text="Apelido",
                           **argsPadraoInsercao,
                           background=corLabel)
        apelido_E = tk.Entry(frameApelido,
                             width=33,
                             **argsPadraoInsercao)

        frameNivel = tk.Frame(insercao,
                              background=corLabel)
        frameNivel.grid(row=0,
                        column=1,
                        sticky="ne",
                        padx=(0, 60),
                        pady=(30, 0))
        nivel = tk.Label(frameNivel,
                         text="Nível",
                         **argsPadraoInsercao,
                         background=corLabel)
        nivel_E = tk.Entry(frameNivel,
                           width=3,
                           **argsPadraoInsercao)
        
        generos = ["Agênero", "Feminino", "Masculino"]
        frameGenero = tk.Frame(insercao,
                               background="red",
                               padx=1)
        frameGenero.grid(row=2,
                         column=0,
                         sticky="ne",
                         padx=30)
        genero = tk.Label(frameGenero,
                          text="Gênero",
                          **argsPadraoInsercao,
                          background=corLabel)
        genero_CB = ttk.Combobox(frameGenero,
                                 width=9,
                                 **argsFonte,
                                 values=generos,
                                 state="readonly")

        frameNome = tk.Frame(insercao,
                             background=corLabel)
        frameNome.grid(row=1,
                       column=0,
                       sticky="ne",
                       padx=30)
        nome = tk.Label(frameNome,
                        text="Nome",
                        **argsPadraoInsercao,
                        background=corLabel)
        nome_E = tk.Entry(frameNome,
                          width=12,
                          **argsPadraoInsercao)

        tipos = ["Normal", "Fogo", "Água", "Grama", "Voador", "Lutador",
                 "Veneno", "Elétrico", "Terra", "Pedra", "Psíquico", "Gelo",
                 "Inseto", "Fantasma", "Ferro", "Dragão", "Sombrio", "Fada"]
        frameTipoUm = tk.Frame(insercao,
                               background="red",
                               padx=1,
                               pady=1)
        frameTipoUm.grid(row=1,
                         column=0,
                         sticky="nw",
                         padx=(60, 0))
        tipoUm = tk.Label(frameTipoUm,
                          text="Tipo 1",
                          **argsPadraoInsercao,
                          background=corLabel)
        tipoUm_CB = ttk.Combobox(frameTipoUm,
                                 width=8,
                                 **argsFonte,
                                 values=tipos,
                                 state="readonly")

        frameTipoDois = tk.Frame(insercao,
                                 background="red",
                                 padx=1)
        frameTipoDois.grid(row=2,
                           column=0,
                           sticky="nw",
                           padx=(60, 0))
        tipoDois = tk.Label(frameTipoDois,
                            text="Tipo 2",
                            **argsPadraoInsercao,
                            background=corLabel)
        tipoDois_CB = ttk.Combobox(frameTipoDois,
                                   width=8,
                                   **argsFonte,
                                   values=tipos,
                                   state="readonly")

        frameNomeHabilidade = tk.Frame(insercao,
                                       background=corLabel)
        frameNomeHabilidade.grid(row=1,
                                 column=1,
                                 sticky="nw",
                                 padx=(0, 60))
        nomeHabilidade = tk.Label(frameNomeHabilidade,
                                  text="Nome da Habilidade",
                                  **argsPadraoInsercao,
                                  background=corLabel)
        nomeHabilidade_E = tk.Entry(frameNomeHabilidade,
                                    width=30,
                                    **argsPadraoInsercao)

        frameItem = tk.Frame(insercao,
                             background=corLabel)
        frameItem.grid(row=3,
                       column=0,
                       sticky="nw",
                       padx=(60, 0))
        item = tk.Label(frameItem,
                        text="Item",
                        **argsPadraoInsercao,
                        background=corLabel)
        item_E = tk.Entry(frameItem,
                          width=16,
                          **argsPadraoInsercao)

        naturezas = ["Neutra",
                     "Lonely: +ATK   -DEF", "Adamant: +ATK   -SP.ATK",
                     "Naughty: +ATK   -SP.DEF", "Brave: +ATK   -SPEED",
                     "Bold: +DEF   -ATK", "Impish: +DEF   -SP.ATK",
                     "Lax: +DEF   -SP.DEF", "Relaxed: +DEF   -SPEED",
                     "Modest: +SP.ATK   -ATK", "Mild: +SP.ATK    -DEF",
                     "Rash: +SP.ATK    -SP.DEF", "Quiet: +SP.ATK    -SPEED",
                     "Calm: +SP.DEF   -ATK", "Gentle: +SP.DEF   -DEF",
                     "Careful: +SP.DEF   -SP.ATK", "Sassy: +SP.DEF   -SPEED",
                     "Timid: +SPEED   -ATK", "Hasty: +SPEED   -DEF",
                     "Jolly: +SPEED   -SP.ATK", "Naive: +SPEED   -SP.DEF"]
        frameNatureza = tk.Frame(insercao,
                                 background="red",
                                 padx=1)
        frameNatureza.grid(row=4,
                           column=0,
                           sticky="nw",
                           padx=(60, 0))
        natureza = tk.Label(frameNatureza,
                            text="Natureza",
                            **argsPadraoInsercao,
                            background=corLabel)
        natureza_CB = ttk.Combobox(frameNatureza,
                                   width=30,
                                   **argsFonte,
                                   values=naturezas,
                                   state="readonly")
        argsDescHab = {
              "font": ('Yu Gothic UI Semibold', 10),
              "highlightthickness": 2,
              "highlightbackground": "red",
              "highlightcolor": "red",
        }
        frameDescHabilidade = tk.Frame(insercao,
                                       background=corLabel)
        frameDescHabilidade.grid(row=2,
                                 column=1,
                                 rowspan=3,
                                 padx=(0, 60))
        descHabilidade = tk.Label(frameDescHabilidade,
                                  text="Descrição da Habilidade",
                                  **argsPadraoInsercao,
                                  background=corLabel)
        descHabilidade_Txt = tk.Text(frameDescHabilidade,
                                     width=110,
                                     height=8,
                                     **argsDescHab)

        frameAcao = tk.Frame(insercao,
                              background="red",
                              padx=2,
                              pady=1)
        frameAcao.grid(row=5,
                       column=0,
                       sticky="nw",
                       padx=(60, 0))
        nomeAcao = tk.Label(frameAcao,
                             text="Nome da Ação",
                             **argsPadraoInsercao,
                             background=corLabel)
        nomeAcao_CB = ttk.Combobox(frameAcao,
                                   width=16,
                                   **argsFonte)

        frameAcaoStats = tk.Frame(insercao,
                                  background="red",
                                  padx=2,
                                  pady=1)
        frameAcaoStats.grid(row=6,
                            column=0,
                            sticky="nw",
                            padx=(60, 0))

        tipoAcao = tk.Label(frameAcaoStats,
                             text="Tipo",
                             **argsPadraoInsercao,
                             background=corLabel)
        tipoAcao_CB = ttk.Combobox(frameAcaoStats,
                                    width=8,
                                    **argsFonte,
                                    values=tipos,
                                    state="readonly")

        pp = tk.Label(frameAcaoStats,
                      text="PP",
                      **argsPadraoInsercao,
                      background=corLabel)
        pp_E = tk.Entry(frameAcaoStats,
                        width=2,
                        **argsPadraoInsercao)
        
        precisao = tk.Label(frameAcaoStats,
                            text="Precisão",
                            **argsPadraoInsercao,
                            background=corLabel)
        precisao_E = tk.Entry(frameAcaoStats,
                              width=3,
                              **argsPadraoInsercao)

        categorias = ["Atk", "Sp.Atk", "Status"]
        frameTipoDanoAcao = tk.Frame(insercao,
                                      background="red",
                                      padx=1)
        frameTipoDanoAcao.grid(row=7,
                               column=0,
                               sticky="nw",
                               padx=(60, 0))
        tipoDeDano = tk.Label(frameTipoDanoAcao,
                              text="Categoria",
                              **argsPadraoInsercao,
                              background=corLabel)
        tipoDeDano_CB = ttk.Combobox(frameTipoDanoAcao,
                                     width=6,
                                     **argsFonte,
                                     values=categorias,
                                     state="readonly")
                
        danoAcao = tk.Label(frameTipoDanoAcao,
                            text="Dano",
                            **argsPadraoInsercao,
                            background=corLabel)
        danoAcao_E = tk.Entry(frameTipoDanoAcao,
                              width=3,
                              **argsPadraoInsercao)
        
        argsDescPod = {
              "font": ('Yu Gothic UI Semibold', 12),
              "highlightthickness": 2,
              "highlightbackground": "red",
              "highlightcolor": "red"}
        frameDescAcao = tk.Frame(insercao,
                                  background=corLabel)
        frameDescAcao.grid(row=8,
                           column=0,
                           rowspan=10,
                           sticky="n",
                           padx=(60, 0))
        descAcao = tk.Label(frameDescAcao,
                            text="Descrição e Observações da Ação",
                            **argsPadraoInsercao,
                            background=corLabel)
        descAcao_Txt = tk.Text(frameDescAcao,
                               width=50,
                               height=9,
                               **argsDescPod)

        frameTags = tk.Frame(insercao,
                             background="red",
                             padx=2,
                             pady=2)
        frameTags.grid(row=18,
                       column=0,
                       sticky="nw",
                       pady=(0, 30),
                       padx=(60, 0))
        tags = tk.Label(frameTags,
                        text="Tags",
                        **argsPadraoInsercao,
                        background=corLabel)
        tags_CB = ttk.Combobox(frameTags,
                               width=30,
                               **argsFonte,
                               values=tipos,
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

        iv = tk.Label(frameStats,
                      text="IV's",
                      **argsPadraoInsercao,
                      background=corLabel)
        ev = tk.Label(frameStats,
                      text="EV's",
                      **argsPadraoInsercao,
                      background=corLabel)

        hp = tk.Label(frameStats,
                      text="Pontos de Vida",
                      **argsPadraoInsercao,
                      background=corLabel)
        hp_E = tk.Entry(frameStats,
                        **argsPadraoInsercao,
                        width=4)
        hpIV_E = tk.Entry(frameStats,
                          **argsPadraoInsercao,
                          width=4)

        hpEV_E = tk.Entry(frameStats,
                          **argsPadraoInsercao,
                          width=4)

        atk = tk.Label(frameStats,
                       text="Ataque",
                       **argsPadraoInsercao,
                       background=corLabel)
        atk_E = tk.Entry(frameStats,
                         **argsPadraoInsercao,
                         width=4)

        atkIV_E = tk.Entry(frameStats,
                           **argsPadraoInsercao,
                           width=4)

        atkEV_E = tk.Entry(frameStats,
                           **argsPadraoInsercao,
                           width=4)

        defs = tk.Label(frameStats,
                        text="Defesa",
                        **argsPadraoInsercao,
                        background=corLabel)
        defs_E = tk.Entry(frameStats,
                          **argsPadraoInsercao,
                          width=4)

        defsIV_E = tk.Entry(frameStats,
                            **argsPadraoInsercao,
                            width=4)

        defsEV_E = tk.Entry(frameStats,
                            **argsPadraoInsercao,
                            width=4)

        spAtk = tk.Label(frameStats,
                         text="Ataque Especial",
                         **argsPadraoInsercao,
                         background=corLabel)
        spAtk_E = tk.Entry(frameStats,
                           **argsPadraoInsercao,
                           width=4)

        spAtkIV_E = tk.Entry(frameStats,
                             **argsPadraoInsercao,
                             width=4)

        spAtkEV_E = tk.Entry(frameStats,
                             **argsPadraoInsercao,
                             width=4)

        spDefs = tk.Label(frameStats,
                          text="Defesa Especial",
                          **argsPadraoInsercao,
                          background=corLabel)
        spDefs_E = tk.Entry(frameStats,
                            **argsPadraoInsercao,
                            width=4)

        spDefsIV_E = tk.Entry(frameStats,
                              **argsPadraoInsercao,
                              width=4)

        spDefsEV_E = tk.Entry(frameStats,
                              **argsPadraoInsercao,
                              width=4)

        spd = tk.Label(frameStats,
                       text="Velocidade",
                       **argsPadraoInsercao,
                       background=corLabel)
        spd_E = tk.Entry(frameStats,
                         **argsPadraoInsercao,
                         width=4)

        spdIV_E = tk.Entry(frameStats,
                           **argsPadraoInsercao,
                           width=4)

        spdEV_E = tk.Entry(frameStats,
                           **argsPadraoInsercao,
                           width=4)

        frameSalvar = tk.Frame(insercao,
                               background=corLabel)
        frameSalvar.grid(row=19,
                         column=0,
                         sticky="nw",
                         padx=(60, 0),
                         pady=(0, 30))
        salvarInfo = tk.Button(frameSalvar,
                               text="Salvar Informações",
                               command=lambda: self.salvar(apelido_E,
                                                           nivel_E,
                                                           genero_CB,
                                                           nome_E,
                                                           tipoUm_CB,
                                                           tipoDois_CB,
                                                           nomeHabilidade_E,
                                                           item_E,
                                                           natureza_CB,
                                                           descHabilidade_Txt,
                                                           nomeAcao_CB, #! Terá muito tratamento pra cada ação
                                                           tipoAcao_CB,
                                                           pp_E,
                                                           precisao_E,
                                                           tipoDeDano_CB,
                                                           danoAcao_E,
                                                           descAcao_Txt,
                                                           tags_CB,
                                                           hp_E,
                                                           hpIV_E,
                                                           hpEV_E,
                                                           atk_E,
                                                           atkIV_E,
                                                           atkEV_E,
                                                           defs_E,
                                                           defsIV_E,
                                                           defsEV_E,
                                                           spAtk_E,
                                                           spAtkIV_E,
                                                           spAtkEV_E,
                                                           spDefs_E,
                                                           spDefsIV_E,
                                                           spDefsEV_E,
                                                           spd_E,
                                                           spdIV_E,
                                                           spdEV_E,))

        voltarMenu.grid(row=0,
                        column=0,
                        sticky="nw",
                        padx=(60, 0),
                        pady=(30, 0))

        apelido.pack(side="left",
                     anchor="nw")
        apelido_E.pack(side="left",
                       anchor="nw")

        nivel.pack(side="left",
                   anchor="ne")
        nivel_E.pack(side="left",
                     anchor="ne")

        nome.pack(side="left",
                  anchor="ne")
        nome_E.pack(side="left",
                    anchor="ne")

        tipoUm.pack(side="left",
                    anchor="w")
        tipoUm_CB.pack(side="left",
                       anchor="w")
        tipoDois.pack(side="left",
                      anchor="w")
        tipoDois_CB.pack(side="left",
                         anchor="w")

        genero.pack(side="left",
                    anchor="nw")
        genero_CB.pack(side="left",
                       anchor="nw")

        nomeHabilidade.pack(side="left",
                            anchor="ne")
        nomeHabilidade_E.pack(side="left",
                              anchor="ne")

        item.pack(side="left",
                  anchor="w")
        item_E.pack(side="left",
                    anchor="w")

        natureza.pack(side="left",
                      anchor="w")
        natureza_CB.pack(side="left",
                         anchor="w")

        descHabilidade.pack(side="top",
                            anchor="center")
        descHabilidade_Txt.pack(side="top",
                                anchor="center")

        nomeAcao.pack(side="left",
                       anchor="nw")
        nomeAcao_CB.pack(side="left",
                         anchor="nw")

        tipoAcao.pack(side="left",
                       anchor="nw")
        tipoAcao_CB.pack(side="left",
                          anchor="nw")

        pp.pack(side="left",
                anchor="nw")
        pp_E.pack(side="left",
                  anchor="nw")
        
        precisao.pack(side="left",
                      anchor="nw")
        precisao_E.pack(side="left",
                        anchor="nw")

        tipoDeDano.pack(side="left",
                        anchor="nw")
        tipoDeDano_CB.pack(side="left",
                           anchor="nw")
        
        danoAcao.pack(side="left",
                       anchor="nw")
        danoAcao_E.pack(side="left",
                         anchor="nw")

        descAcao.pack(side="top",
                       anchor="center")
        descAcao_Txt.pack(side="top",
                           anchor="center")

        tags.pack(side="left",
                  anchor="nw")
        tags_CB.pack(side="left",
                     anchor="nw")

        iv.grid(row=0,
                column=2,
                sticky="sew")
        ev.grid(row=0,
                column=3,
                sticky="sew")

        hp.grid(row=1,
                column=0,
                sticky="nsew")
        hp_E.grid(row=1,
                  column=1,
                  sticky="nsew")
        hpIV_E.grid(row=1,
                    column=2,
                    sticky="nsew")
        hpEV_E.grid(row=1,
                    column=3,
                    sticky="nsew")

        atk.grid(row=2,
                 column=0,
                 sticky="nsew")
        atk_E.grid(row=2,
                   column=1,
                   sticky="nsew")
        atkIV_E.grid(row=2,
                     column=2,
                     sticky="nsew")
        atkEV_E.grid(row=2,
                     column=3,
                     sticky="nsew")

        defs.grid(row=3,
                  column=0,
                  sticky="nsew")
        defs_E.grid(row=3,
                    column=1,
                    sticky="nsew")
        defsIV_E.grid(row=3,
                      column=2,
                      sticky="nsew")
        defsEV_E.grid(row=3,
                      column=3,
                      sticky="nsew")

        spAtk.grid(row=4,
                   column=0,
                   sticky="nsew")
        spAtk_E.grid(row=4,
                     column=1,
                     sticky="nsew")
        spAtkIV_E.grid(row=4,
                       column=2,
                       sticky="nsew")
        spAtkEV_E.grid(row=4,
                       column=3,
                       sticky="nsew")

        spDefs.grid(row=5,
                    column=0,
                    sticky="nsew")
        spDefs_E.grid(row=5,
                      column=1,
                      sticky="nsew")
        spDefsIV_E.grid(row=5,
                        column=2,
                        sticky="nsew")
        spDefsEV_E.grid(row=5,
                        column=3,
                        sticky="nsew")

        spd.grid(row=6,
                 column=0,
                 sticky="nsew")
        spd_E.grid(row=6,
                   column=1,
                   sticky="nsew")
        spdIV_E.grid(row=6,
                     column=2,
                     sticky="nsew")
        spdEV_E.grid(row=6,
                     column=3,
                     sticky="nsew")

        salvarInfo.pack(anchor="se")

        return insercao


    def telaListagem(self, root):
        listagem = tk.Frame(self.root)
        listagem.grid(row=0,
                  column=0,
                  sticky="nsew")

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
        labelFont = "Yu Gothic UI Semibold"
        labelBg = "white"

        nomePokeFrame = tk.Frame(listagem,
                                 background=labelBg)
        nomePokeFrame.grid(row=0,
                           column=0,
                           sticky="nsew")
        nomePokeLabel = tk.Label(nomePokeFrame,
                                 text="Nome do Pokémon",
                                 font=(labelFont,
                                       labelFontSize),
                                 background=labelBg,
                                 justify="center")
        nomePokeEntry = tk.Entry(nomePokeFrame,
                                 width=12,
                                 font=(labelFont,
                                       labelFontSize),
                                 justify="center")
        nomePokeLabel.pack(side="top")
        nomePokeEntry.pack(side="top")

        apelidoPokeFrame = tk.Frame(listagem,
                                    background=labelBg)
        apelidoPokeFrame.grid(row=0,
                              column=1,
                              sticky="nsew")
        apelidoPokeLabel = tk.Label(apelidoPokeFrame,
                                    text="Apelido do Pokémon",
                                    font=(labelFont,
                                          labelFontSize),
                                    background=labelBg,
                                    justify="center")
        apelidoPokeEntry = tk.Entry(apelidoPokeFrame,
                                    width=40,
                                    font=(labelFont,
                                          labelFontSize),
                                    justify="center")
        apelidoPokeLabel.pack(side="top")
        apelidoPokeEntry.pack(side="top")

        tagsPoke = ttk.Combobox(listagem,
                                font=(labelFont,
                                      labelFontSize),
                                state="readonly",
                                justify="center")
        tagsPoke.set(value="Tags")
        tagsPoke.grid(row=0,
                      column=2,
                      sticky="nsew")
        #! Listagem dos Pokémons
        listaPokes = tk.Frame(listagem,
                              background="black")
        listaPokes.grid(row=1,
                        column=0,
                        columnspan=3,
                        sticky="nsew")

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
                                     justify="center",
                                     font=(labelFont,
                                           20))
            nomePokeLista.grid(row=rowAtual,
                               column=0,
                               sticky="nsew")
            apelidoPokeLista = tk.Label(listaPokes,
                                        text=pokemon[1],
                                        justify="center",
                                        font=(labelFont,
                                           20))
            apelidoPokeLista.grid(row=rowAtual,
                                  column=1,
                                  sticky="nsew")
            tagsPokeLista = tk.Label(listaPokes,
                                     text=pokemon[2],
                                     justify="center",
                                     font=(labelFont,
                                           20))
            tagsPokeLista.grid(row=rowAtual,
                               column=2,
                               sticky="nsew")

            radiosPokeLista = tk.Radiobutton(listaPokes)
            radiosPokeLista.grid(row=rowAtual,
                                 column=3,
                                 sticky="nsew")
            rowAtual += 1
#?________________________________________________________________________________________

        botoesFrame = tk.Frame(listagem,
                               background=labelBg)
        botoesFrame.grid(row=2,
                         column=0,
                         columnspan=3,
                         sticky="nsew")
        delTag = tk.Button(botoesFrame,
                               text="- Tag")
        delTag.pack(side="left",
                    padx=(30, 15))
        addTag = tk.Button(botoesFrame,
                           text="+ Tag")
        addTag.pack(side="left",
                    padx=15)

        novoPoke = tk.Button(botoesFrame,
                             text="Novo Pokémon",
                             command=lambda: self.chamarRaise(self.insercao))
        novoPoke.pack(side="left",
                      padx=15)

        voltarMenu = tk.Button(botoesFrame,
                               text="Voltar ao Menu",
                               command=lambda: self.chamarRaise(self.menu))
        voltarMenu.pack(side="left",
                        padx=15)

        verPoke = tk.Button(botoesFrame,
                            text="Vizualizar Pokémon",
                            command=lambda: self.chamarRaise(self.visualizacao))
        verPoke.pack(side="left",
                     padx=15)

        return listagem


    def telaVisualizacao(self, root):
        visualizacao = tk.Frame(self.root)
        visualizacao.grid(row=0,
                          column=0,
                          sticky="nsew")

        self.bgLabel = tk.Label(visualizacao,
                                image=self.tkBg)
        self.bgLabel.place(x=0,
                           y=0,
                           relwidth=1,
                           relheight=1)

        argsPadraoVisualizacao = {
              "font": ('Yu Gothic UI Semibold', 20),
              "highlightthickness": 2,
              "highlightbackground": "red",
              "highlightcolor": "red",
              "background": "white"
        }

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

        voltarMenu = tk.Button(visualizacao,
                               text="Voltar ao Menu",
                               command=lambda: self.chamarRaise(self.menu))

        frameApelido = tk.Frame(visualizacao)
        frameApelido.grid(row=0,
                          column=1,
                          sticky="nw",
                          pady=(30, 0))
        apelido = tk.Label(frameApelido,
                           text="Apelido",
                           **argsPadraoVisualizacao)
        apelido_I = tk.Label(frameApelido,
                             text="<<Apelido>>",
                             **argsPadraoVisualizacao)

        frameNivel = tk.Frame(visualizacao)
        frameNivel.grid(row=0,
                        column=1,
                        sticky="ne",
                        padx=(0, 60),
                        pady=(30, 0))
        nivel = tk.Label(frameNivel,
                         text="Nível",
                         **argsPadraoVisualizacao)
        nivel_I = tk.Label(frameNivel,
                           text="<00>",
                           **argsPadraoVisualizacao)

        frameGenero = tk.Frame(visualizacao)
        frameGenero.grid(row=2,
                         column=0,
                         sticky="ne",
                         padx=30)
        genero = tk.Label(frameGenero,
                          text="Gênero",
                          **argsPadraoVisualizacao)
        genero_I = tk.Label(frameGenero,
                                 text="<<Gênero>>",
                                 **argsPadraoVisualizacao)

        frameNome = tk.Frame(visualizacao)
        frameNome.grid(row=1,
                       column=0,
                       sticky="ne",
                       padx=30)
        nome = tk.Label(frameNome,
                        text="Nome",
                        **argsPadraoVisualizacao)
        nome_I = tk.Label(frameNome,
                          text="<<Nome>>",
                          **argsPadraoVisualizacao)

        frameTipoUm = tk.Frame(visualizacao)
        frameTipoUm.grid(row=1,
                         column=0,
                         sticky="nw",
                         padx=(60, 0))
        tipoUm = tk.Label(frameTipoUm,
                          text="Tipo 1",
                          **argsPadraoVisualizacao)
        tipoUm_I = tk.Label(frameTipoUm,
                             text="<Tipo Um>",
                             **argsPadraoVisualizacao)

        frameTipoDois = tk.Frame(visualizacao)
        frameTipoDois.grid(row=2,
                           column=0,
                           sticky="nw",
                           padx=(60, 0))
        tipoDois = tk.Label(frameTipoDois,
                            text="Tipo 2",
                            **argsPadraoVisualizacao)
        tipoDois_I = tk.Label(frameTipoDois,
                                   text="<Tipo Dois>",
                                   **argsPadraoVisualizacao)

        frameNomeHabilidade = tk.Frame(visualizacao)
        frameNomeHabilidade.grid(row=1,
                                 column=1,
                                 sticky="nw",
                                 padx=(0, 60))
        nomeHabilidade = tk.Label(frameNomeHabilidade,
                                  text="Nome da Habilidade",
                                  **argsPadraoVisualizacao)
        nomeHabilidade_I = tk.Label(frameNomeHabilidade,
                                    text="<<Nome da Habilidade>>",
                                    **argsPadraoVisualizacao)

        frameItem = tk.Frame(visualizacao)
        frameItem.grid(row=3,
                       column=0,
                       sticky="nw",
                       padx=(60, 0))
        item = tk.Label(frameItem,
                        text="Item",
                        **argsPadraoVisualizacao)
        item_I = tk.Label(frameItem,
                          text="<<Item>>",
                          **argsPadraoVisualizacao)

        frameNatureza = tk.Frame(visualizacao)
        frameNatureza.grid(row=4,
                           column=0,
                           sticky="nw",
                           padx=(60, 0))
        natureza = tk.Label(frameNatureza,
                            text="Natureza",
                            **argsPadraoVisualizacao)
        natureza_I = tk.Label(frameNatureza,
                              text="<<Natureza>>",
                              **argsPadraoVisualizacao)

        argsDescVisualizacao = {
                "font": ('Yu Gothic UI Semibold', 10),
                "highlightthickness": 2,
                "highlightbackground": "red",
                "highlightcolor": "red",
                "background": "white"
        }
        frameDescHabilidade = tk.Frame(visualizacao)
        frameDescHabilidade.grid(row=2,
                                 column=1,
                                 rowspan=3,
                                 padx=(0, 60))
        descHabilidade = tk.Label(frameDescHabilidade,
                                  text="Descrição da Habilidade",
                                  **argsPadraoVisualizacao)
        descHabilidade_I = tk.Label(frameDescHabilidade,
                                     text="<<Descrição da Habilidade>>",
                                     height=8,
                                     **argsDescVisualizacao) #TODO -> label de múltiplas linhas

        frameAcao = tk.Frame(visualizacao)
        frameAcao.grid(row=5,
                        column=0,
                        sticky="nw",
                        padx=(60, 0))
        nomeAcao = tk.Label(frameAcao,
                             text="Nome da Ação",
                             **argsPadraoVisualizacao)
        nomeAcao_I = tk.Label(frameAcao,
                               text="<<Nome da Ação>>",
                               **argsPadraoVisualizacao)

        frameAcaoStats = tk.Frame(visualizacao)
        frameAcaoStats.grid(row=6,
                             column=0,
                             sticky="nw",
                             padx=(60, 0))

        tipoAcao = tk.Label(frameAcaoStats,
                             text="Tipo",
                             **argsPadraoVisualizacao)
        tipoAcao_I = tk.Label(frameAcaoStats,
                               text="<Tipo>",
                               **argsPadraoVisualizacao)

        pp = tk.Label(frameAcaoStats,
                      text="PP",
                      **argsPadraoVisualizacao)
        pp_I = tk.Label(frameAcaoStats,
                        text="<PP>",
                        **argsPadraoVisualizacao)
        
        precisao = tk.Label(frameAcaoStats,
                            text="Precisão",
                            **argsPadraoVisualizacao)
        precisao_I = tk.Label(frameAcaoStats,
                            text="<00>",
                            **argsPadraoVisualizacao)

        frameTipoDanoAcao = tk.Frame(visualizacao)
        frameTipoDanoAcao.grid(row=7,
                               column=0,
                               sticky="nw",
                               padx=(60, 0))
        tipoDeDano = tk.Label(frameTipoDanoAcao,
                              text="Categoria",
                              **argsPadraoVisualizacao)
        tipoDeDano_I = tk.Label(frameTipoDanoAcao,
                                text="<<Categoria>>",
                                **argsPadraoVisualizacao)

        danoAcao = tk.Label(frameTipoDanoAcao,
                            text="Dano",
                            **argsPadraoVisualizacao)
        danoAcao_I = tk.Label(frameTipoDanoAcao,
                              text="<00>",
                              **argsPadraoVisualizacao)
        
        frameDescAcao = tk.Frame(visualizacao)
        frameDescAcao.grid(row=8,
                           column=0,
                           rowspan=10,
                           sticky="n",
                           padx=(60, 0))
        descAcao = tk.Label(frameDescAcao,
                            text="Descrição e Observações da Ação",
                            **argsPadraoVisualizacao)
        descAcao_I = tk.Label(frameDescAcao,
                              text="<<Nome>>",
                              height=9,
                              **argsPadraoVisualizacao)

        frameTags = tk.Frame(visualizacao)
        frameTags.grid(row=18,
                       column=0,
                       sticky="nw",
                       pady=(0, 30),
                       padx=(60, 0))
        tags = tk.Label(frameTags,
                        text="Tags",
                        **argsPadraoVisualizacao)
        tags_I = tk.Label(frameTags,
                          text="<<Tags>>",
                          **argsPadraoVisualizacao)


        frameStats = tk.Frame(visualizacao)
        frameStats.grid(row=5,
                        column=1,
                        rowspan=19,
                        pady=(0, 30),
                        padx=(0, 60))
        frameStats.rowconfigure([0, 1, 2, 3, 4, 5, 6],
                                weight=1)
        frameStats.columnconfigure([0, 1],
                                   weight=7)
        frameStats.columnconfigure([2, 3],
                                   weight=3)
        frameStats.columnconfigure(4,
                                   weight=9)

        argsStatsVisualizacao = {
              "font": ('Yu Gothic UI Semibold', 22),
              "highlightthickness": 1,
              "highlightbackground": "red",
              "highlightcolor": "red",
              "background": "white"
        }
        argsIvEvVisualizacao = {
              "font": ('Yu Gothic UI Semibold', 22),
              "background": "white"
        }
        iv = tk.Label(frameStats,
                      text="IV's",
                      **argsIvEvVisualizacao)
        ev = tk.Label(frameStats,
                      text="EV's",
                      **argsIvEvVisualizacao)

        hp = tk.Label(frameStats,
                      text="Pontos de Vida",
                      **argsIvEvVisualizacao)
        hp_I = tk.Label(frameStats,
                        text="<<HP>>",
                        **argsStatsVisualizacao,
                        width=4)
        hpIV_I = tk.Label(frameStats,
                          text="<<HP IV>>",
                          **argsStatsVisualizacao,
                          width=4)
        hpEV_I = tk.Label(frameStats,
                          text="<<HP EV>>",
                          **argsStatsVisualizacao,
                          width=4)
        hpTotal = tk.Label(frameStats,
                           text="<TOTAL>",
                           **argsStatsVisualizacao,
                           width=6)

        atk = tk.Label(frameStats,
                       text="Ataque",
                       **argsIvEvVisualizacao)
        atk_I = tk.Label(frameStats,
                         text="<<ATK>>",
                         **argsStatsVisualizacao,
                         width=4)
        
        atkIV_I = tk.Label(frameStats,
                           text="<<ATK IV>>",
                           **argsStatsVisualizacao,
                           width=4)

        atkEV_I = tk.Label(frameStats,
                           text="<<ATK EV>>",
                           **argsStatsVisualizacao,
                           width=4)
        
        atkTotal = tk.Label(frameStats,
                            text="<TOTAL>",
                            **argsStatsVisualizacao,
                            width=4)

        defs = tk.Label(frameStats,
                        text="Defesa",
                        **argsIvEvVisualizacao)
        defs_I = tk.Label(frameStats,
                          text="<<DEFS>>",
                          **argsStatsVisualizacao,
                          width=4)

        defsIV_I = tk.Label(frameStats,
                            text="<<DEFS IV>>",
                            **argsStatsVisualizacao,
                            width=4)

        defsEV_I = tk.Label(frameStats,
                            text="<<DEFS EV>>",
                            **argsStatsVisualizacao,
                            width=4)
        
        defsTotal = tk.Label(frameStats,
                             text="<TOTAL>",
                             **argsStatsVisualizacao,
                             width=6)

        spAtk = tk.Label(frameStats,
                         text="Ataque Especial",
                         **argsIvEvVisualizacao)
        spAtk_I = tk.Label(frameStats,
                           text="<<SP.ATK>>",
                           **argsStatsVisualizacao,
                           width=4)

        spAtkIV_I = tk.Label(frameStats,
                             text="<<SP.ATK IV>>",
                             **argsStatsVisualizacao,
                             width=4)

        spAtkEV_I = tk.Label(frameStats,
                             text="<<SP.ATK EV>>",
                             **argsStatsVisualizacao,
                             width=4)
        
        spAtkTotal = tk.Label(frameStats,
                              text="<TOTAL>",
                              **argsStatsVisualizacao,
                              width=6)

        spDefs = tk.Label(frameStats,
                          text="Defesa Especial",
                          **argsIvEvVisualizacao)
        spDefs_I = tk.Label(frameStats,
                            text="<<SP.DEFS>>",
                            **argsStatsVisualizacao,
                            width=4)

        spDefsIV_I = tk.Label(frameStats,
                              text="<<SP.DEFS IV>>",
                              **argsStatsVisualizacao,
                              width=4)

        spDefsEV_I = tk.Label(frameStats,
                              text="<<SP.DEFS EV>>",
                              **argsStatsVisualizacao,
                              width=4)
        
        spDefsTotal = tk.Label(frameStats,
                               text="<TOTAL>",
                               **argsStatsVisualizacao,
                               width=4)

        spd = tk.Label(frameStats,
                       text="Velocidade",
                       **argsIvEvVisualizacao)
        spd_I = tk.Label(frameStats,
                         text="<<SPD>>",
                         **argsStatsVisualizacao,
                         width=4)

        spdIV_I = tk.Label(frameStats,
                           text="<<SPD IV>>",
                           **argsStatsVisualizacao,
                           width=4)

        spdEV_I = tk.Label(frameStats,
                           text="<<SPD EV>>",
                           **argsStatsVisualizacao,
                           width=4)
        
        spdTotal = tk.Label(frameStats,
                            text="<TOTAL>",
                            **argsStatsVisualizacao,
                            width=6)

        frameSalvar = tk.Frame(visualizacao)
        frameSalvar.grid(row=19,
                         column=0,
                         sticky="nw",
                         padx=(60, 0),
                         pady=(0, 30))
        salvarInfo = tk.Button(frameSalvar,
                               text="Salvar Informações")

        voltarMenu.grid(row=0,
                        column=0,
                        sticky="nw",
                        padx=(60, 0),
                        pady=(30, 0))

        apelido.pack(side="left",
                     anchor="nw")
        apelido_I.pack(side="left",
                       anchor="nw")

        nivel.pack(side="left",
                   anchor="ne")
        nivel_I.pack(side="left",
                     anchor="ne")

        nome.pack(side="left",
                  anchor="ne")
        nome_I.pack(side="left",
                    anchor="ne")

        tipoUm.pack(side="left",
                    anchor="w")
        tipoUm_I.pack(side="left",
                       anchor="w")
        tipoDois.pack(side="left",
                      anchor="w")
        tipoDois_I.pack(side="left",
                         anchor="w")

        genero.pack(side="left",
                    anchor="nw")
        genero_I.pack(side="left",
                       anchor="nw")

        nomeHabilidade.pack(side="left",
                            anchor="ne")
        nomeHabilidade_I.pack(side="left",
                              anchor="ne")

        item.pack(side="left",
                  anchor="w")
        item_I.pack(side="left",
                    anchor="w")

        natureza.pack(side="left",
                      anchor="w")
        natureza_I.pack(side="left",
                         anchor="w")

        descHabilidade.pack(side="top",
                            anchor="center")
        descHabilidade_I.pack(side="top",
                                anchor="center")

        nomeAcao.pack(side="left",
                       anchor="nw")
        nomeAcao_I.pack(side="left",
                         anchor="nw")

        tipoAcao.pack(side="left",
                       anchor="nw")
        tipoAcao_I.pack(side="left",
                          anchor="nw")

        pp.pack(side="left",
                anchor="nw")
        pp_I.pack(side="left",
                  anchor="nw")
        
        precisao.pack(side="left",
                      anchor="nw")
        precisao_I.pack(side="left",
                        anchor="nw")

        tipoDeDano.pack(side="left",
                        anchor="nw")
        tipoDeDano_I.pack(side="left",
                           anchor="nw")
        
        danoAcao.pack(side="left",
                       anchor="nw")
        danoAcao_I.pack(side="left",
                         anchor="nw")

        descAcao.pack(side="top",
                       anchor="center")
        descAcao_I.pack(side="top",
                           anchor="center")

        tags.pack(side="left",
                  anchor="nw")
        tags_I.pack(side="left",
                     anchor="nw")

        iv.grid(row=0,
                column=2,
                sticky="sew")
        ev.grid(row=0,
                column=3,
                sticky="sew")

        hp.grid(row=1,
                column=0,
                sticky="nsew")
        hp_I.grid(row=1,
                  column=1,
                  sticky="nsew")
        hpIV_I.grid(row=1,
                    column=2,
                    sticky="nsew")
        hpEV_I.grid(row=1,
                    column=3,
                    sticky="nsew")
        hpTotal.grid(row=1,
                     column=4,
                     sticky="nsew")

        atk.grid(row=2,
                 column=0,
                 sticky="nsew")
        atk_I.grid(row=2,
                   column=1,
                   sticky="nsew")
        atkIV_I.grid(row=2,
                     column=2,
                     sticky="nsew")
        atkEV_I.grid(row=2,
                     column=3,
                     sticky="nsew")
        atkTotal.grid(row=2,
                      column=4,
                      sticky="nsew")

        defs.grid(row=3,
                  column=0,
                  sticky="nsew")
        defs_I.grid(row=3,
                    column=1,
                    sticky="nsew")
        defsIV_I.grid(row=3,
                      column=2,
                      sticky="nsew")
        defsEV_I.grid(row=3,
                      column=3,
                      sticky="nsew")
        defsTotal.grid(row=3,
                       column=4,
                       sticky="nsew")

        spAtk.grid(row=4,
                   column=0,
                   sticky="nsew")
        spAtk_I.grid(row=4,
                     column=1,
                     sticky="nsew")
        spAtkIV_I.grid(row=4,
                       column=2,
                       sticky="nsew")
        spAtkEV_I.grid(row=4,
                       column=3,
                       sticky="nsew")
        spAtkTotal.grid(row=4,
                        column=4,
                        sticky="nsew")

        spDefs.grid(row=5,
                    column=0,
                    sticky="nsew")
        spDefs_I.grid(row=5,
                      column=1,
                      sticky="nsew")
        spDefsIV_I.grid(row=5,
                        column=2,
                        sticky="nsew")
        spDefsEV_I.grid(row=5,
                        column=3,
                        sticky="nsew")
        spDefsTotal.grid(row=5,
                         column=4,
                         sticky="nsew")

        spd.grid(row=6,
                 column=0,
                 sticky="nsew")
        spd_I.grid(row=6,
                   column=1,
                   sticky="nsew")
        spdIV_I.grid(row=6,
                     column=2,
                     sticky="nsew")
        spdEV_I.grid(row=6,
                     column=3,
                     sticky="nsew")
        spdTotal.grid(row=6,
                      column=4,
                      sticky="nsew")

        salvarInfo.pack(anchor="se")

        return visualizacao


    def telaTutorial(self, root):
        tutorial = tk.Frame(self.root)
        tutorial.grid(row=0,
                  column=0,
                  sticky="nsew")

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
    
    def salvar(self,
               apelido_E,
               nivel_E,
               genero_CB,
               nome_E,
               tipoUm_CB,
               tipoDois_CB,
               nomeHabilidade_E,
               item_E,
               natureza_CB,
               descHabilidade_Txt,
               nomeAcao_CB,
               tipoAcao_CB,
               pp_E,
               precisao_E,
               tipoDeDano_CB,
               danoAcao_E,
               descAcao_Txt,
               tags_CB,
               hp_E,
               hpIV_E,
               hpEV_E,
               atk_E,
               atkIV_E,
               atkEV_E,
               defs_E,
               defsIV_E,
               defsEV_E,
               spAtk_E,
               spAtkIV_E,
               spAtkEV_E,
               spDefs_E,
               spDefsIV_E,
               spDefsEV_E,
               spd_E,
               spdIV_E,
               spdEV_E):
        
        apelido = apelido_E.get()
        nivel = nivel_E.get()
        genero = genero_CB.get()
        nome = nome_E.get()
        tipoUm = tipoUm_CB.get()
        tipoDois = tipoDois_CB.get()
        nomeHabilidade = nomeHabilidade_E.get()
        item = item_E.get()
        natureza = natureza_CB.get()
        descHabilidade = descHabilidade_Txt.get("1.0", "end")
        nomeAcao = nomeAcao_CB.get()
        tipoAcao = tipoAcao_CB.get()
        pp = pp_E.get()
        precisao = precisao_E.get()
        tipoDeDano = tipoDeDano_CB.get()
        danoAcao = danoAcao_E.get()
        descAcao = descAcao_Txt.get("1.0", "end")
        tags = tags_CB.get()
        hp = hp_E.get()
        hp = hpIV_E.get()
        hp = hpEV_E.get()
        atk = atk_E.get()
        atk = atkIV_E.get()
        atk = atkEV_E.get()
        defs = defs_E.get()
        defs = defsIV_E.get()
        defs = defsEV_E.get()
        spAtk = spAtk_E.get()
        spAtk = spAtkIV_E.get()
        spAtk = spAtkEV_E.get()
        spDefs = spDefs_E.get()
        spDefs = spDefsIV_E.get()
        spDefs = spDefsEV_E.get()
        spd = spd_E.get()
        spd = spdIV_E.get()
        spd = spdEV_E.get()