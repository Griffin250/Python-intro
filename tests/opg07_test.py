import oppgaver.opg07
import inspect
import requests

URL = "https://raw.githubusercontent.com/SamEydeITM/demodata/main/people.json"

def test_hentPersoner():
  assert hasattr(oppgaver.opg07, "hentPersoner"), "Funksjonen hentPersoner eksisterer ikke"
  func = getattr(oppgaver.opg07, "hentPersoner")
  assert len(inspect.signature(func).parameters) == 0, "Funksjonen skal ikke ha noen parametere"
  res = func()
  wres = sorted([d['email'] for d in requests.get(URL).json()["users"]])
  assert type(res) == list, "Funksjonen hentPersoner returnerer ikke en liste"
  assert URL == oppgaver.opg07.URL, "URL variablen er ikke den opprinnelige URLen"
  assert len(wres) == len(res), "Antallet returnerte e-post adresser stemmer ikke"
  assert sorted([d['email'] for d in requests.get(URL).json()["users"]]) == sorted(res), "Funksjonen returnerer ikke en liste med e-post adressene"
