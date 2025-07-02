
import pymongo as pmg
import sys

class Model():
    
    def __init__(self):
        dbMain = pmg.MongoClient("mongodb://localhost:27017/")
        
        pokeBase = pmg.myclient["PokeBase"]
    
    def sair():
        sys.exit()