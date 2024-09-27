# Oppgave 7
#
# NB: Krever internett!
# NB: Her må man importere biblioteket requests
#
# Lag en funksjon som henter eksterne data som heter hentPersoner()
#
# Funksjonen skal benytte requests biblioteket for å utføre en HTTP GET.
# Funksjonen skal parse JSON filen med requests innebygde .json()
# Funksjonen skal returnere en liste med alle e-post adressene til alle personene.
# 
# Bruk variablen URL for hvor man skal hente data fra
# 
#
# Les mer om python og requests biblioteket på:
# https://www.w3schools.com/python/module_requests.asp
# 

URL = "https://raw.githubusercontent.com/SamEydeITM/demodata/main/people.json"
#----------------------------------------------------------------------------------------
import requests

URL = "https://raw.githubusercontent.com/SamEydeITM/demodata/main/people.json"

def hentPersoner():
    
    respons = requests.get(URL)
    
    if respons.status_code == 200:
        data = respons.json()
        
        if isinstance(data, dict) and 'users' in data:
            epost_liste = [person.get("email") for person in data['users']]
            return epost_liste
        else:
            print("Uventet JSON-struktur")
            return []
    else:
        print(f"Feil ved henting av data: {respons.status_code}")
        return []

emails = hentPersoner()
if emails:
    for emails in emails:
        print(emails)
else: 
    print("Ingen email addresser funnet!")




