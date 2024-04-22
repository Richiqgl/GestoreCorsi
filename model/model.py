from database.corso_dao import Corso_Dao
from model.corso import Corso
class Model:
    def __init__(self):
        self._corsi = {}

    def get_corsi_periodo(self,pd):
        return Corso_Dao.get_corsi_periodo(pd)

    def get_studenti_periodo(self,pd):
        matricole= Corso_Dao.get_studenti_periodo(pd)
        return len(matricole)
        #matricole=set()
    def carica_corsi(self):
        Corso_Dao.get_corsi(self._corsi)

    def restituisci_corso(self,codice):
        if self._corsi =={}:
            self.carica_corsi()
            return self._corsi[codice]
        else:
            return self._corsi[codice]


