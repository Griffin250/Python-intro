# Oppgave 6
#
# Lag en funksjon som skriver en loggfil med navn loggfil.log.
# Funksjonen skal hete skrivLogg() og tar inn en streng parameter for tekstlinjen den
# skal legge i filen. Loggfilen skal alltid legge til (append) nye linjer, ikke overskrive.
# Funksjonen returnerer ingenting
# 
# Les mer om python og skriving til fil på:
# https://www.w3schools.com/python/python_file_write.asp
# 
# --- Skriv koden under her ---

def skrivLogg(tekstlinjen):
    with open("loggfil.log", "a") as fil:
        fil.write(tekstlinjen + "\n")

skrivLogg("Dette er første linje")
skrivLogg("Dette er andre linjen")
