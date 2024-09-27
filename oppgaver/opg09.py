# Oppgave 9
# 
# Lag en klasse med navn User
# Klassen User skal ha 2 variabler; username og email
# som settes i konstruktøren / __init__()
#
# Lag en funksjon etter/utenfor klassen med navn lagBruker()
# Denne funksjonen tar inn 2 parametere; brukernavn og epost
#
# Funksjonen skal så returnere et objekt/instans av klassen User med informasjonen
# fra parameterene til funksjonen.
#
# Les mer om python og klasser:
# https://www.w3schools.com/python/python_classes.asp
# 
# --- Skriv koden under her ---
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
#funksjon som lager lagBruker.
def lagBruker(brukernavn, epost):
    return User(brukernavn, epost) #... det skal returnere en user med gitt verdier.

ny_brukere = lagBruker("Isiah", "isiah.sameyde@gamil.com") #Laget ny_brukere.

print(ny_brukere.username)
print(ny_brukere.email)



