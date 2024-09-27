# Oppgave 4
#
# Lag en funksjon som heter settSammen() som tar imot 
# en liste med ord, og returnerer en sammensatt
# streng hvor det er mellomrom mellom hvert ord. 
# 
# --- Skriv koden under her ---

def settSammen(ordliste):
    sammensattStreng = " ".join(ordliste)
    return sammensattStreng

ordliste = ["Jeg", " heter", " Isiah"]
resultat = settSammen(ordliste)
print(resultat)


