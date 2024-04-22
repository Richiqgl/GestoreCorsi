from database.DB_connect import DBConnect
from model.studente import Studente
class Studente_Dao:
    def __init__(self):
        pass
    @staticmethod
    def get_studenti_corso(codice):
        cnx=DBConnect.get_connection()
        if cnx is None:
            print("Errore connessione")
            return
        else:
            cursor=cnx.cursor(dictionary=True)
            query="""  SELECT s.*
                        FROM studente s  ,iscrizione i 
                        WHERE i.codins =%s AND s.matricola  =i.matricola """
            cursor.execute(query,(codice,))
            result=[]
            for row in cursor:
                result.append(Studente(row["matricola"],
                                    row["nome"],
                                    row["cognome"],
                                    row["CDS"]))
            cursor.close()
            cnx.close()
            return result

