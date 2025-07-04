
import pymongo
import sys

class Model():
    
    def __init__(self):
        dbMain = pymongo.MongoClient("mongodb://localhost:27017/")
        pokeBase = dbMain["PokeBase"]
        pokemons = pokeBase["Pokemons"]
        tags = pokeBase["Tags"]
        
        
        
        
    
    def sair():
        sys.exit()