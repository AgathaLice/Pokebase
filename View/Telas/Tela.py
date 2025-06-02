from abc import ABC
from abc import abstractmethod

class Tela(ABC):
    background: str = ""
    
    def bordas(self):
        #! Deve criar uma grid de 12x12 e reservar as colunas e linhas da borda.
        #? Linhas: 0x0 & 12x12
        #? Colunas: 0x0 & 12x12
        return
    
    @abstractmethod
    def exemplo(self):
        pass