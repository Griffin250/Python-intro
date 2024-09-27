import oppgaver.opg04
import string
import inspect
import random

def test_settSammen():
  assert hasattr(oppgaver.opg04, "settSammen"), "Funksjonen settSammen() eksisterer ikke"
  func = getattr(oppgaver.opg04, "settSammen")
  assert len(inspect.signature(func).parameters) == 1, "Funksjonen har ikke riktig antall parametere"
  for _ in range(0, 10):
    letters = string.ascii_lowercase
    wgen = [''.join(random.choice(letters) for i in range(random.randint(2, 10))) for _ in range(random.randint(4, 10))]
    wout = " ".join(wgen)
    result = func(wgen)
    assert result != None, "Funksjonen returnerer ingenting"
    assert type(result) == str, "Funksjonen returnerer ikke riktig data-type"
    assert result == wout, f"Funksjonen returnerer ikke riktig verdi: {result} | Forventet: {wout}"