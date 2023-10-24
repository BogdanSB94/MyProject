import datetime

class Factura:

    SERIE = None

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        data_azi = datetime.date.today()
        total = self.cantitate * self.pret_buc

        print(f"Factura seria {Factura.SERIE} număr {self.numar}")
        print(f"Data: {data_azi}")
        print("Produs | cantitate | preț bucată | Total")
        print(f"{self.nume_produs} |    {self.cantitate}    | {self.pret_buc}          | {total}")



factura1 = Factura(1, "Telefon", 7, 700)
factura1.genereaza_factura()



