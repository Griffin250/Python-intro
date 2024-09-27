# Oppgave 10
# 
# Lag en klasse som heter Kalkulator
#
# Klassen skal ha en variabel som heter resultat og skal ha standardverdi som 0,
# eller kan settes til noe annet i konstruktøren / __init__
#
# resultat variablen skal være av typen flyttall.
#
# Det skal lages funksjoner i klassen for de 4 vanlige matematiske operasjonene;
# pluss(), minus(), gange() og dele()
# hver av disse funskjonene skal ha 1 parameter som er ett flyttall (i tillegg til self).
# I tillegg en funksjon som returnerer variablen resultat som heter giResultat()
#
# De matematiske operasjonene skal ikke returnere noe, men de skal oppdatere
# resultat variablen ved å plusse, trekke fra, gange eller dele.
#
# Slik at for eksempel:
# 
# Kalkulator(5).pluss(5).dele(2).gange(5).minus(20).giResultat() skal ende med å returnere
# flyttallet 5.0
#
#
# Legg til funksjonen giHistorikk()
# Denne funksjonen skal returnere en liste med strenger som viser regnestykkene underveis
# og vise daværende resultat.
#
# F.eks
# [
#   "2 + 5 = 7",
#   "7 * 2 = 14",
#   "14 / 2 = 7"
# ]
#
# Legg dermed til en variabel i konstruktøren som heter historikk som er en tom liste
# denne listen skal da suppleres underveis med nye elementer etterhvert som det blir 
# gjort operasjoner matematiske operasjoner.
#
# Lag en privat funksjon i klassen __loggHistorikk() som tar inn en streng parameter
# som legger denne strengen til i historikk lista.
#
#
# I hver matematiske operasjon funksjon, legg til funksjonen __loggHistorikk hvor man gir
# __loggHistorikk det gjeldende resultatet og den nye operasjonen som skal legges til og
# det nye resultatet:
#
# For eksempel:
# __loggHistorikk("5 + 6 = 7")
#
# Men bruk variablene for å hente verdiene som faktisk skal stå i strengen man gir __loggHistorikk
#
#
# Les mer om python og klasser:
# https://www.w3schools.com/python/python_classes.asp
#
# Les mer om python og listemetoder:
# https://www.w3schools.com/python/python_lists_methods.asp
# 
# --- Skriv koden under her ---
class Kalkulator:
    def __init__(self, resultat=0.0):
        self.resultat = float(resultat)
        self.historikk = []

    def pluss(self, tall):
        gammelt_resultat = self.resultat
        self.resultat += tall
        self.__loggHistorikk(f"{gammelt_resultat} + {tall} = {self.resultat}")
        return self

    def minus(self, tall):
        gammelt_resultat = self.resultat
        self.resultat -= tall
        self.__loggHistorikk(f"{gammelt_resultat} - {tall} = {self.resultat}")
        return self

    def gange(self, tall):
        gammelt_resultat = self.resultat
        self.resultat *= tall
        self.__loggHistorikk(f"{gammelt_resultat} * {tall} = {self.resultat}")
        return self

    def dele(self, tall):
        gammelt_resultat = self.resultat
        if tall != 0:
            self.resultat /= tall
            self.__loggHistorikk(f"{gammelt_resultat} / {tall} = {self.resultat}")
        else:
            self.__loggHistorikk(f"Kan ikke dele med 0")
        return self

    def giResultat(self):
        return self.resultat

    def giHistorikk(self):
        return self.historikk

    def __loggHistorikk(self, tekst):
        self.historikk.append(tekst)


kalkulator = Kalkulator(5)
kalkulator.pluss(5).dele(2).gange(5).minus(20)
print(kalkulator.giResultat())  # Forventet: 5.0
print(kalkulator.giHistorikk())  # Viser historikken over operasjonene
