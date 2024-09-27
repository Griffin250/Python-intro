import oppgaver.opg09
import inspect
import random
import string

def test_UserClass():
  assert hasattr(oppgaver.opg09, "User"), "Klassen User eksisterer ikke"
  userclass:oppgaver.opg09.User = getattr(oppgaver.opg09, "User")
  assert len(inspect.signature(userclass).parameters) == 2, "Klassen User skal ha en konstruktør med 2 parametere"
  assert "username" in inspect.signature(userclass).parameters.keys(), "Konstruktøren mangler username parameteren"
  assert "email" in inspect.signature(userclass).parameters.keys(), "Konstruktøren mangler email parameteren"
  for _ in range(3):
    instusername = "".join([d for d in random.choices(string.ascii_letters, k=random.randint(10,30))])
    instemail = "".join([d for d in random.choices(string.ascii_letters, k=random.randint(10,30))])
    inst = userclass(instusername, instemail)
    assert hasattr(inst, "username"), "Variablen username i klassen User eksisterer ikke eller blir ikke satt i konstruktøren"
    assert hasattr(inst, "email"), "Variablen email i klassen User eksisterer ikke eller blir ikke satt i konstruktøren"
    assert inst.username == instusername, "Variablen username har ikke samme verdi som gitt med konstruktøren til klassen User"
    assert inst.email == instemail, "Variablen email har ikke samme verdi som gitt med konstruktøren til klassen User"


def test_lagBruker():
  assert hasattr(oppgaver.opg09, "lagBruker"), "Funksjonen lagBruker eksisterer ikke"
  func = getattr(oppgaver.opg09, "lagBruker")
  assert len(inspect.signature(func).parameters) == 2, "Funksjonen lagBruker skal ha 2 parametere"
  assert "brukernavn" in inspect.signature(func).parameters.keys(), "Funksjonen lagBruker mangler parameteren brukernavn"
  assert "epost" in inspect.signature(func).parameters.keys(), "Funksjonen lagBruker mangler parameteren epost"
  for _ in range(3):
    instusername = "".join([d for d in random.choices(string.ascii_letters, k=random.randint(10,30))])
    instemail = "".join([d for d in random.choices(string.ascii_letters, k=random.randint(10,30))])
    assert func(instusername, instemail).username == oppgaver.opg09.User(instusername, instemail).username, "Funksjonen lagBruker returnerer ikke en instans/objekt av klassen User"
    assert func(instusername, instemail).email == oppgaver.opg09.User(instusername, instemail).email, "Funksjonen lagBruker returnerer ikke en gyldig instans/objekt av klassen User"
