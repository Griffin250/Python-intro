# Oppgave 5
#
# Lag en variabel med navn brukere som er en liste med ordbokselementer
# Ordbøkene skal inneholde nøkklene navn og alder
# navn skal være en streng
# alder skal være en integer
# lag listen med ordbøker slik at den inneholder 3 vilkårlige personer med navn og alder
# 
# --- Skriv koden under her ---
#
brukere = [
    {"navn": "Isiah", "alder": 24},
    {"navn": "John", "alder": 18},
    {"navn": "Kevin", "alder": 36}
]
brukere_str = ["navn: " + person["navn"] + ", alder: " + str(person["alder"]) for person in brukere]

x = "\n".join(brukere_str)
print(x)
