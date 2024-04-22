import flet as ft

from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view:View, model:Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._CDS=set()

    def get_corsi_periodo(self,e):
        if self._pd is None:
            self._view.create_alert("Selezionare il periodo didattico")
            return
        corsi=self._model.get_corsi_periodo(self._pd)
        self._view.list_risulatati.controls.clear()
        for corso in corsi:
            self._view.list_risulatati.controls.append(ft.Text(corso.__str__()))
        self._view.update_page()


    def get_studenti_periodo(self,e):
        if self._pd is None:
            self._view.create_alert("selezionare un periodo didattico")
            return
        numero=self._model.get_studenti_periodo(self._pd)
        print(numero)
        self._view.list_risulatati.controls.clear()
        self._view.list_risulatati.controls.append(ft.Text(f"Il numero di studenti per il periodo didattico {self._pd} è {numero}"))
        self._view.update_page()

    def get_dettaglio_corso(self,e):
        self._view.list_risulatati.controls.clear()
        codice_corso = self._view.txt_codice_corso.value
        if codice_corso == "":
            self._view.create_alert("codice_corso errato")
            return
        else:
            corso_cercato = self._model.restituisci_corso(codice_corso)
            studenti = corso_cercato.get_studenti()
            for studente in studenti:
                self._CDS.add(studente.CDS)
            for elemento in self._CDS:
                self._view.list_risulatati.controls.append(ft.Text(f"CDS: {elemento}",color="red"))
                for studente in studenti:
                    if studente.CDS==elemento:
                        self._view.list_risulatati.controls.append(ft.Text(studente.__str__()))
            self._view.update_page()
            return

    def get_studenti_corso(self,e):
        self._view.list_risulatati.controls.clear()
        codice_corso=self._view.txt_codice_corso.value
        if codice_corso =="":
            self._view.create_alert("codice_corso errato")
            return
        else:
            corso_cercato=self._model.restituisci_corso(codice_corso)
            studenti=corso_cercato.get_studenti()
            for studente in studenti:
                self._view.list_risulatati.controls.append(ft.Text(studente.__str__()))
        self._view.update_page()

    def leggi_tendina(self,e):
        self._pd=self._view.dd_periodo.value
        #oppure e.control.value
        print(self._pd)

