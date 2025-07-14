
import pymongo
import sys
from math import floor

class Model():
    
    def __init__(self):
        dbMain = pymongo.MongoClient("mongodb://localhost:27017/")
        pokeBase = dbMain["PokeBase"]
        self.pokemons = pokeBase["Pokemons"]
        self.tags = pokeBase["Tags"]
    
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
            "hpTotal": self.calcularHp(hp, hpIV, hpEV, nivel) if nome != "Shedinja" else 1,
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
        
        poke = self.pokemons.insert_one(pokemon)
    
    def getInt(self, valor):
        return int(valor)
    
    def calcularHp(self,
                   hp: int,
                   hpIV: int,
                   hpEV: int,
                   nivel: int) -> int:
        hpEV = floor(hpEV / 4)
        hp *= 2
        hp = hp + hpIV + hpEV
        hp *= nivel
        nivel += 10
        hp = floor(hp / 100)
        hp += nivel
        return hp

    def calcularStat(self: int,
                     stat: int,
                     statIV: int,
                     statEV: int,
                     nivel: int,
                     natureza) -> int:
        statEV = floor(statEV / 4)
        stat *= 2
        stat = stat + statIV + statEV
        stat *= nivel
        stat = floor(stat / 100)
        stat += 5
        #todo: adicionar natureza
        return stat
    
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
        elif valor in tagsAtuais and salvar == True:
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
    
    def pokemonsLista(self) -> None | dict:
        todos = self.pokemons.find({}, {"Nome":1, "Apelido":1, "Tags":1,"_id":0})        
        nomes = [i["Nome"] for i in todos]
        apelidos = [i["Apelido"] for i in todos]
        tags = [i["Tags"] for i in todos]
        dictRetorno: dict = {"Nomes": nomes,
                             "Apelido": apelidos,
                             "Tags": tags}
        
        return dictRetorno
    
    def verPoke(self, valor):
        poke = self.pokemons.find_one({ "Nome":valor })
        print(poke)
        return poke

    def ultimoPoke(self):
        last = self.pokemons.find_one(sort=[('_id', pymongo.DESCENDING)])
        return last
    '''
    def delTag(self, tags, valor):
        print(tags)
        i = 0
        while i < len(tags):
            if tags[i] == valor:
                tags.pop(i)
        else:
            print("ERRO")
        i += 1
        if i >= 100:
            return tags
        return tags'''
    
    def sair():
        sys.exit()