# Oppgave 3
#
# Lag en funksjon som heter erPartall()
# Funksjonen skal ta inn 1 integer parameter 
# og returnere en boolsk verdi på om tallet er ett partall eller ikke
#
# Lag så en funksjon i tillegg som heter erOddetall()
# Funksjonen skal da gjøre det motsatte ved å returnere en boolsk verdi på om
# tallet er ett oddetall
# 
# --- Skriv koden under her ---
def erPartall(tall):
    return tall % 2 == 0

tall = 24
if erPartall(tall):
    print(f"{tall} er ett partall.")

else:
    print(f"{tall} er ett oddtall.")


def erOddetall(tall):
    return tall % 2 != 0
tall = 23
if erOddetall(tall):
    print(f"{tall} er ett odd tall.")

else: 
    print(f"{tall} er ett partall.")