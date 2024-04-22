import _mysql_connector
from database.DB_connect import DBConnect
from model.corso import Corso
class Corso_Dao:
    def __init__(self):
        pass
    @staticmethod#classe statica
    def get_corsi_periodo(pd):
        cnx=DBConnect.get_connection()
        if cnx is None:
            print("ERrrore connessione")
            return
        else:
            cursor=cnx.cursor(dictionary=True)
            query="""  SELECT *
                    FROM corso c 
                        WHERE c.pd =%s"""
            cursor.execute(query,(pd,))
            result=[]
            for row in cursor:
                result.append(Corso(row["codins"],
                                    row["crediti"],
                                    row["nome"],
                                    row["pd"]))
            cursor.close()
            cnx.close()
            return result
    @staticmethod
    def get_studenti_periodo(pd):
        cnx=DBConnect.get_connection()
        if cnx is None:
            print("ERrrore connessione")
            return
        else:
            cursor=cnx.cursor(dictionary=True)
            query="""  SELECT  DISTINCT i.matricola
FROM corso c , iscrizione i 
WHERE c.pd =%s AND c.codins =i.codins """
            cursor.execute(query,(pd,))
            rows=cursor.fetchall()
            cursor.close()
            cnx.close()
            return rows
    @staticmethod
    def get_corsi(corsi_map):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("ERrrore connessione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """  SELECT  c.*
                    FROM corso c  """
            cursor.execute(query,)
            rows = cursor.fetchall()
            for row in rows:
                corso=Corso(row["codins"],row["crediti"],row["nome"],row["pd"])
                corsi_map[corso.codins]=corso
            cursor.close()
            cnx.close()
            # print(corsi_map)
            # for key, value in corsi_map.items():
            #     print(f"la chiave {key}")
            #     print(value)
