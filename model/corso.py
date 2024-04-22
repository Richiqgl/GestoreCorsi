from dataclasses import dataclass
from database.studenti_dao import Studente_Dao

@dataclass
class Corso:
    codins:str
    crediti:int
    nome:str
    pd:int

    studenti=None

    def __eq__(self, other):
        return self.codins==other.codins
    def __hash__(self):
        return hash(self.codins)

    def __str__(self):
        return (f"il codice {self.codins} il nome {self.nome} i crediti{self.crediti} pd {self.pd}")

    def get_studenti(self):
        if self.studenti is None:
            #leggere dao
            self.studenti=Studente_Dao.get_studenti_corso(self.codins)
            return self.studenti
        else:
            return self.studenti