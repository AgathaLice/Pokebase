
import pymongo
import sys
from math import floor

class Model():
    
    def __init__(self):
        dbMain = pymongo.MongoClient("mongodb://localhost:27017/")
        pokeBase = dbMain["PokeBase"]
        pokemons = pokeBase["Pokemons"]
        tags = pokeBase["Tags"]
        
    
    
    def salvar(self,
               apelido,
               nivel,
               genero,
               nome,
               tipoUm,
               tipoDois,
               nomeHabilidade,
               item,
               natureza,
               descHabilidade,
               nomeAcao,
               tipoAcao,
               pp,
               precisao,
               categoria,
               danoAcao,
               descAcao,
               tags,
               hp,
               hpIV,
               hpEV,
               atk,
               atkIV,
               atkEV,
               defs,
               defsIV,
               defsEV,
               spAtk,
               spAtkIV,
               spAtkEV,
               spDefs,
               spDefsIV,
               spDefsEV,
               spd,
               spdIV,
               spdEV):
        pokemon = {
            "Apelido": apelido,
    "Nome": nome,
    "Nível": nivel,
    "Gênero": genero,
    "Tipo Um": tipoUm,
    "Tipo Dois": tipoDois,
    "Nome Habilidade": nomeHabilidade,
    "Descrição Habilidade": descHabilidade,
    "Item": item,
    "Natureza": natureza,
    "Ação 1": {
        "Nome": nomeAcao,
        "Dano": danoAcao,
        "Tipo": tipoAcao,
        "Precisão": precisao,
        "PP": pp,
        "Categoria": categoria,
        "Descrição Da Ação": descAcao
        },
    "Tags": tags,
    "hp": hp,
    "hpIV": hpIV,
    "hpEV": hpEV,
    "hpTotal": self.calcularHp(hp, hpIV, hpEV, nivel),
    "atk": atk,
    "atkIV": atkIV,
    "atkEV": atkEV,
    "atkTotal": self.calcularStat(atk, atkIV, atkEV, nivel, natureza),
    "def": defs,
    "defIV": defsIV,
    "defEV": defsEV,
    "defsTotal": self.calcularStat(defs, defsIV, defsEV, nivel, natureza),
    "sp.atk": spAtk,
    "sp.atkIV": spAtkIV,
    "sp.atkEV": spAtkEV,
    "sp.atkTotal": self.calcularStat(spAtk, spAtkIV, spAtkEV, nivel, natureza),
    "sp.def": spDefs,
    "sp.defIV": spDefsIV,
    "sp.defEV": spDefsEV,
    "sp.defsTotal": self.calcularStat(spDefs, spDefsIV, spDefsEV, nivel, natureza),
    "spd": spd,
    "spdIV": spdIV,
    "spdEV": spdEV,
    "spdTotal": self.calcularStat(spd, spdIV, spdEV, nivel, natureza)
        }
    
        print(pokemon)
    
    def calcularHp(self,
                   hp,
                   hpIV,
                   hpEV,
                   nivel) -> int:
        hpEV = floor(hpEV / 4)
        hp *= 2
        hp = hp + hpIV + hpEV
        hp *= nivel
        nivel += 10
        hp = floor(hp / 100)
        hp += nivel
        return hp

    def calcularStat(self,
                     stat,
                     statIV,
                     statEV,
                     nivel,
                     natureza) -> int:
        pass
    
    def addTagInsercao(self,
                       valor,
                       tagsCB,
                       tagsAtuais, 
                       salvar: bool
                       ) -> None | dict:
        if valor == "":
            #todo
            print("Valor Vazio, arrumar depois")
            novosValoresTags = {
                "tagsCB": tagsCB,
                "tagsAtuais": tagsAtuais}
            return novosValoresTags
        if valor in tagsAtuais and salvar == False: #! testando caso salvar chame cm um valor nas atuais
            #todo
            print("Adicionar aviso e não fazer nada")
            novosValoresTags = {
                "tagsCB": tagsCB,
                "tagsAtuais": tagsAtuais}
            return novosValoresTags
        if valor in tagsCB and valor in tagsAtuais:
            #todo
            print("Valor repetido, avisar ao user")
            return novosValoresTags
        if valor not in tagsCB:
            tagsCB.append(valor)
            tagsAtuais.append(valor)
            novosValoresTags = {
                "tagsCB": tagsCB,
                "tagsAtuais": tagsAtuais}
            return novosValoresTags
        elif valor in tagsCB:
            tagsAtuais.append(valor)
            novosValoresTags = {
                "tagsCB": tagsCB,
                "tagsAtuais": tagsAtuais}
            return novosValoresTags
        else: 
            print("ERRO")
            return None

    def criarListaMoves(self,
                        valorCB,
                        movesCB,
                        contador) -> None | dict:
        if contador <= 4:
            # todo: Adicionar regex para verificar se não começa com "1- "
            movesCB[contador - 1] += valorCB
            contador += 1
        dictValores = {
            "valorCB": valorCB,
            "movesCB": movesCB,
            "contador": contador,
            "readonly": False
        }
        if contador > 4:
            dictValores["readonly"] = True
            
        return dictValores

    def editarMoves(self,
                    dadosPokemonMoves,
                    contador,
                    movesCB,
                    acaoEdicao,
                    opcoes):
        contador = contador
        movesCB[opcoes - 1] = f"{opcoes}- "
        contador = opcoes



    def sair():
        sys.exit()