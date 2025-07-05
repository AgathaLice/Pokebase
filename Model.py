
import pymongo
import sys

class Model():
    
    def __init__(self):
        dbMain = pymongo.MongoClient("mongodb://localhost:27017/")
        pokeBase = dbMain["PokeBase"]
        pokemons = pokeBase["Pokemons"]
        tags = pokeBase["Tags"]
        
        
        
        
    """
    #!-> pega o valor
    #!-> verifica se o valor já não é uma das tags na lista de adicionadas 
    #!-> se sim, dá um aviso e não adiciona nada (isso não ocorre qnd a função é chamada pelo botão de salvar)
    #!-> se não:
    #!->   verifica se não está na lista de tags da combobox
    #!->   se sim, adiciona nas tags, mas não o adiciona na lista de opções
    #!->   se não, adiciona em ambas as listas para uso posterior
    #!->   limpa a opção da combobox
    """
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

    
    def sair():
        sys.exit()