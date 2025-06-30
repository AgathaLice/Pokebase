import tkinter as tk

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
                                 seeSize))
        apelido_I = tk.Label(frameApelido,
                             text="<<Apelido>>"
                             font=(seeFont,
                                   seeSize))

        frameNivel = tk.Frame(visualizacao)
        frameNivel.grid(row=0,
                        column=1,
                        sticky='ne',
                        padx=(0, 60),
                        pady=(30, 0))
        nivel = tk.Label(frameNivel,
                         text="Nível",
                         font=(seeFont,
                               seeSize))
        nivel_I = tk.Label(frameNivel,
                           text="<00>"
                           font=(seeFont,
                                 seeSize))

        frameGenero = tk.Frame(visualizacao)
        frameGenero.grid(row=2,
                         column=0,
                         sticky='ne',
                         padx=30)
        genero = tk.Label(frameGenero,
                          text="Gênero",
                          font=(seeFont,
                                seeSize))
        genero_I = tk.Label(frameGenero,
                                 text="<<Gênero>>",
                                 font=(seeFont,
                                       seeSize))

        frameNome = tk.Frame(visualizacao)
        frameNome.grid(row=1,
                       column=0,
                       sticky='ne',
                       padx=30)
        nome = tk.Label(frameNome,
                        text="Nome",
                        font=(seeFont,
                              seeSize))
        nome_I = tk.Label(frameNome,
                          text="<<Nome>>",
                          font=(seeFont,
                                seeSize))

        frameTipoUm = tk.Frame(visualizacao)
        frameTipoUm.grid(row=1,
                         column=0,
                         sticky='nw',
                         padx=(60, 0))
        tipoUm = tk.Label(frameTipoUm,
                          text="Tipo 1",
                          font=(seeFont,
                                seeSize))
        tipoUm_I = tk.Label(frameTipoUm,
                             text="<<Tipo Um>>",
                             font=(seeFont,
                                   seeSize))

        frameTipoDois = tk.Frame(visualizacao)
        frameTipoDois.grid(row=2,
                           column=0,
                           sticky='nw',
                           padx=(60, 0))
        tipoDois = tk.Label(frameTipoDois,
                            text="Tipo 2",
                            font=(seeFont,
                                  seeSize))
        tipoDois_I = tk.Label(frameTipoDois,
                                   text="<<Tipo Dois>>",
                                   font=(seeFont,
                                         seeSize))

        frameNomeHabilidade = tk.Frame(visualizacao)
        frameNomeHabilidade.grid(row=1,
                                 column=1,
                                 sticky='nw',
                                 padx=(0, 60))
        nomeHabilidade = tk.Label(frameNomeHabilidade,
                                  text="Nome da Habilidade",
                                  font=(seeFont,
                                        seeSize))
        nomeHabilidade_I = tk.Label(frameNomeHabilidade,
                                    text="<<Nome da Habilidade>>",
                                    font=(seeFont,
                                          seeSize))

        frameItem = tk.Frame(visualizacao)
        frameItem.grid(row=3,
                       column=0,
                       sticky='nw',
                       padx=(60, 0))
        item = tk.Label(frameItem,
                        text="Item",
                        font=(seeFont,
                              seeSize))
        item_I = tk.Label(frameItem,
                          text="<<Item>>",
                          font=(seeFont,
                                seeSize))

        frameNatureza = tk.Frame(visualizacao)
        frameNatureza.grid(row=4,
                           column=0,
                           sticky='nw',
                           padx=(60, 0))
        natureza = tk.Label(frameNatureza,
                            text="Natureza",
                            font=(seeFont,
                                  seeSize))
        natureza_I = tk.Label(frameNatureza,
                              text="<<Natureza>>",
                              font=(seeFont,
                                  seeSize))

        frameDescHabilidade = tk.Frame(visualizacao)
        frameDescHabilidade.grid(row=2,
                                 column=1,
                                 rowspan=3,
                                 padx=(0, 60))
        descHabilidade = tk.Label(frameDescHabilidade,
                                  text="Descrição da Habilidade",
                                  font=(seeFont,
                                        seeSize))
        descHabilidade_I = tk.Label(frameDescHabilidade,
                                     text="<<Descrição da Habilidade>>",
                                     height=8,
                                     font=(seeFont, 10)) #TODO -> label de múltiplas linhas

        framePoder = tk.Frame(visualizacao)
        framePoder.grid(row=5,
                        column=0,
                        sticky='nw',
                        padx=(60, 0))
        nomePoder = tk.Label(framePoder,
                             text="Nome do Poder",
                             font=(seeFont,
                                   seeSize))
        nomePoder_I = tk.Label(framePoder,
                               text="<<Nome do Poder>>",
                               font=(seeFont,
                                     seeSize))

        framePoderStats = tk.Frame(visualizacao)
        framePoderStats.grid(row=6,
                             column=0,
                             sticky='nw',
                             padx=(60, 0))
        danoPoder = tk.Label(framePoderStats,
                             text="Dano",
                             font=(seeFont,
                                   seeSize))
        danoPoder_I = tk.Label(framePoderStats,
                               text="<<Dano do Poder>>",
                               font=(seeFont,
                                     seeSize))

        tipoPoder = tk.Label(framePoderStats,
                             text="Tipo",
                             font=(seeFont,
                                   seeSize))
        tipoPoder_I = tk.Label(framePoderStats,
                               text="<<Tipo do Poder>>",
                               font=(seeFont,
                                     seeSize))

        pp = tk.Label(framePoderStats,
                      text="PP",
                      font=(seeFont,
                            seeSize))
        pp_I = tk.Label(framePoderStats,
                        text="<<PP>>",
                        font=(seeFont,
                              seeSize))

        frameTipoDanoPoder = tk.Frame(visualizacao)
        frameTipoDanoPoder.grid(row=7,
                                column=0,
                                sticky='nw',
                                padx=(60, 0))
        tipoDeDano = tk.Label(frameTipoDanoPoder,
                              text="ATK ou SP.ATK",
                              font=(seeFont,
                                    seeSize))
        tipoDeDano_I = tk.Label(frameTipoDanoPoder,
                                text="<<Escalamento de Dano>>",
                                font=(seeFont,
                                      seeSize))

        frameDescPoder = tk.Frame(visualizacao)
        frameDescPoder.grid(row=8,
                            column=0,
                            rowspan=10,
                            sticky='n',
                            padx=(60, 0))
        descPoder = tk.Label(frameDescPoder,
                             text="Descrição e Observações do Poder",
                             font=(seeFont,
                                   seeSize))
        descPoder_I = tk.Label(frameDescPoder,
                               text="<<Nome>>",
                               height=9,
                               font=(seeFont, 12))

        frameTags = tk.Frame(visualizacao)
        frameTags.grid(row=18,
                       column=0,
                       sticky='nw',
                       pady=(0, 30),
                       padx=(60, 0))
        tags = tk.Label(frameTags,
                        text="Tags",
                        font=(seeFont,
                              seeSize))
        tags_I = tk.Label(frameTags,
                          text="<<Nome>>",
                          font=(seeFont,
                                seeSize))


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
                      statsLabelSize))
        ev = tk.Label(frameStats,
                      text="EV's",
                      font=(seeFont,
                      statsLabelSize))


        hp = tk.Label(frameStats,
                      text="Pontos de Vida",
                      font=(seeFont,
                      statsLabelSize))
        hp_I = tk.Label(frameStats,
                        highlightthickness=1,
                        text="<<HP>>",
                        font=(seeFont,
                              statsLabelSize),
                        width=4)
        hp_I.configure(highlightbackground="red",
                       highlightcolor="red")
        hpIV_I = tk.Label(frameStats,
                          highlightthickness=1,
                          text="<<HP IV>>",
                          font=(seeFont,
                                statsLabelSize),
                          width=4)
        hpIV_I.configure(highlightbackground="red",
                         highlightcolor="red")
        hpEV_I = tk.Label(frameStats,
                          highlightthickness=1,
                          text="<<HP EV>>",
                          font=(seeFont,
                                statsLabelSize),
                          width=4)
        hpEV_I.configure(highlightbackground="red",
                         highlightcolor="red")

        atk = tk.Label(frameStats,
                       text="Ataque",
                       font=(seeFont,
                             statsLabelSize))
        atk_I = tk.Label(frameStats,
                         highlightthickness=1,
                         text="<<ATK>>",
                         font=(seeFont,
                               statsLabelSize),
                         width=4)
        atk_I.configure(highlightbackground="red",
                        highlightcolor="red")
        atkIV_I = tk.Label(frameStats,
                           highlightthickness=1,
                           text="<<ATK IV>>",
                           font=(seeFont,
                                 statsLabelSize),
                           width=4)
        atkIV_I.configure(highlightbackground="red",
                          highlightcolor="red")
        atkEV_I = tk.Label(frameStats,
                           highlightthickness=1,
                           text="<<ATK EV>>",
                           font=(seeFont,
                                 statsLabelSize),
                           width=4)
        atkEV_I.configure(highlightbackground="red",
                          highlightcolor="red")

        defs = tk.Label(frameStats,
                        text="Defesa",
                        font=(seeFont,
                              statsLabelSize))
        defs_I = tk.Label(frameStats,
                          highlightthickness=1,
                          text="<<DEFS>>",
                          font=(seeFont,
                                statsLabelSize),
                          width=4)
        defs_I.configure(highlightbackground="red",
                         highlightcolor="red")
        defsIV_I = tk.Label(frameStats,
                            highlightthickness=1,
                            text="<<DEFS IV>>",
                            font=(seeFont,
                                  statsLabelSize),
                            width=4)
        defsIV_I.configure(highlightbackground="red",
                           highlightcolor="red")
        defsEV_I = tk.Label(frameStats,
                            highlightthickness=1,
                            text="<<DEFS EV>>",
                            font=(seeFont,
                                  statsLabelSize),
                            width=4)
        defsEV_I.configure(highlightbackground="red",
                           highlightcolor="red")

        spAtk = tk.Label(frameStats,
                         text="Ataque Especial",
                         font=(seeFont,
                               statsLabelSize))
        spAtk_I = tk.Label(frameStats,
                           highlightthickness=1,
                           text="<<SP.ATK>>",
                           font=(seeFont,
                                 statsLabelSize),
                           width=4)
        spAtk_I.configure(highlightbackground="red",
                          highlightcolor="red")
        spAtkIV_I = tk.Label(frameStats,
                             highlightthickness=1,
                             text="<<SP.ATK IV>>",
                             font=(seeFont,
                                   statsLabelSize),
                             width=4)
        spAtkIV_I.configure(highlightbackground="red",
                            highlightcolor="red")
        spAtkEV_I = tk.Label(frameStats,
                             highlightthickness=1,
                             text="<<SP.ATK EV>>",
                             font=(seeFont,
                                   statsLabelSize),
                             width=4)
        spAtkEV_I.configure(highlightbackground="red",
                            highlightcolor="red")

        spDefs = tk.Label(frameStats,
                          text="Defesa Especial",
                          font=(seeFont,
                                statsLabelSize))
        spDefs_I = tk.Label(frameStats,
                            highlightthickness=1,
                            text="<<SP.DEFS>>",
                            font=(seeFont,
                                  statsLabelSize),
                            width=4)
        spDefs_I.configure(highlightbackground="red",
                           highlightcolor="red")
        spDefsIV_I = tk.Label(frameStats,
                              highlightthickness=1,
                              text="<<SP.DEFS IV>>",
                              font=(seeFont,
                                    statsLabelSize),
                              width=4)
        spDefsIV_I.configure(highlightbackground="red",
                             highlightcolor="red")
        spDefsEV_I = tk.Label(frameStats,
                              highlightthickness=1,
                              text="<<SP.DEFS EV>>",
                              font=(seeFont,
                                    statsLabelSize),
                              width=4)
        spDefsEV_I.configure(highlightbackground="red",
                             highlightcolor="red")

        spd = tk.Label(frameStats,
                       text="Velocidade",
                       font=(seeFont,
                             statsLabelSize))
        spd_I = tk.Label(frameStats,
                         highlightthickness=1,
                         text="<<SPD>>",
                         font=(seeFont,
                               statsLabelSize),
                         width=4)
        spd_I.configure(highlightbackground="red",
                        highlightcolor="red")
        spdIV_I = tk.Label(frameStats,
                           highlightthickness=1,
                           text="<<SPD IV>>",
                           font=(seeFont,
                                 statsLabelSize),
                           width=4)
        spdIV_I.configure(highlightbackground="red",
                          highlightcolor="red")
        spdEV_I = tk.Label(frameStats,
                           highlightthickness=1,
                           text="<<SPD EV>>",
                           font=(seeFont,
                                 statsLabelSize),
                           width=4)
        spdEV_I.configure(highlightbackground="red",
                          highlightcolor="red")

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