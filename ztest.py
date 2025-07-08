'''

pikachuExemplo = {
    "Apelido": "Matheus",
    "Nome": "Pikachu",
    "Nível": 50,
    "Gênero": "Masculino",
    "Tipo Um": "Elétrico",
    "Tipo Dois": "---",
    "Nome Habilidade": "Para-raios",
    "Descrição Habilidade": """Lightning Rod força todos os movimentos do tipo Elétrico de alvo único — usados ​​por qualquer outro Pokémon no campo — a atingirem este Pokémon,  com 100% de precisão. Isso inclui o movimento de status Thunder Wave. Ao ser atingido pelo movimento, ele não causa dano ao portador da habilidade, mas aumenta seu Ataque Especial em um estágio.""",
    "Item": "Faixa de Foco",
    "Natureza": "Tímido",
    "Ação 1": {
        "Nome": "Fake Out",
        "Dano": 40,
        "Tipo": "Normal",
        "Precisão": 100,
        "PP": 10,
        "Categoria": "Físico",
        "Descrição Da Ação": ""
        },
    "Ação 2": {
        "Nome": "Volt Switch",
        "Dano": 70,
        "Tipo": "Elétrico",
        "Precisão": 100,
        "PP": 20,
        "Categoria": "Especial",
        "Descrição Da Ação": ""
    },
    "Ação 3": {
        "Nome": "",
        "Dano": 0,
        "Tipo": "",
        "Precisão": 0,
        "PP": 0,
        "Categoria": "",
        "Descrição Da Ação": ""
    },
    "Ação 4": {
        "Nome": "",
        "Dano": 0,
        "Tipo": "",
        "Precisão": 0,
        "PP": 0,
        "Categoria": "",
        "Descrição Da Ação": ""
    },
    "Tags": [],
    "hp": 35,
    "hpIV": 31,
    "hpEV": 4,
    "atk": 55,
    "atkIV": 31,
    "atkEV": 0,
    "def": 40,
    "defIV": 31,
    "defEV": 0,
    "sp.atk": 50,
    "sp.atkIV": 31,
    "sp.atkEV": 252,
    "sp.def": 50,
    "sp.defIV": 31,
    "sp.defEV": 0,
    "spd": 90,
    "spdIV": 31,
    "spdEV": 252
        }

tagsExemplo1 = {
    "nome": "Elétrico"
}

'''

'''
nomeAcao_E = tk.Entry(frameAcao,
                              **argsPadraoInsercao,
                              width=16)
        frameAcaoEdicao = tk.Frame(frameAcao,
                                   background="red")
        editarAcao = tk.Button(frameAcaoEdicao,
                               text="Editar Ação")
                               command=lambda:
                                   self.chamarEditarMoves(movesPokemonDb,
                                                          acaoEdicao_CB,
                                                          opcoesCB))
        opcoesCB: list[int] = [1, 2, 3, 4]
        acaoEdicao_CB = ttk.Combobox(frameAcaoEdicao,
                                  width=5,
                                  justify="center",
                                  state="readonly",
                                  font=('Yu Gothic UI Semibold', 11),
                                  values=opcoesCB)
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
'''

'''self.nomeAcao_CB.pack(side="left",
                         anchor="nw")'''