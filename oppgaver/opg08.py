# Oppgave 8
# 
# ::: DEL 1 :::
#
# Lag en funksjon som heter sjekkPassord()
# Funksjonen skal ta inn 1 parameter som er en streng med navn passord
# Funksjonen skal ha en try-except som sjekker om passordet er riktig
# Hvis passordet er feil skal funksjonen kaste en Exception()
# Hvis passordet er riktig skal funksjonen returnere True
#
# Du kan velge ditt eget passord på variablen PASSORD.
# PASSORD variablen brukes av testene, så det er den verdien som er det
# riktige passordet.
#
# ::: DEL 2 :::
#
# Lag en enda en funksjon med navn passordRespons()
# Denne tar også inn 1 parameter med navn passord.
# Funksjonen skal ha en try-except med funksjonen fra DEL 1.
# Hvis passordet er riktig skal den returnere strengen fra variablen SUCCESS_MSG, 
# hvis en feil/exception skal den returnere strengen fra variablen FAILED_MSG.
#
#
# Les mer om python og unntak/feilhåndtering/exceptions:
# https://www.w3schools.com/python/gloss_python_raise.asp
# 

PASSORD = "passord123"

SUCCESS_MSG = "Passordet er riktig!"
FAILED_MSG = "Passordet er feil!"

def sjekkPassord(passord):
    if passord != PASSORD:
        raise Exception("Feil passord")
    return True

def passordRespons(passord):
    try:
        sjekkPassord(passord) 
        return SUCCESS_MSG
    except Exception:
        return FAILED_MSG

# Test av funksjonen
print(passordRespons("passord123"))  
print(passordRespons("feilpassord"))  
