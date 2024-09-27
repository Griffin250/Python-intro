import oppgaver.opg03
import inspect
import random

def test_erPartall():
  assert hasattr(oppgaver.opg03, "erPartall"), "Funksjonen erPartall() eksisterer ikke"
  func = getattr(oppgaver.opg03, "erPartall")
  assert len(inspect.signature(func).parameters) == 1, "Funksjonen har ikke riktig antall parametere"
  for _ in range(0, 10):
    num = random.randint(0,9999)
    result = func(num)
    assert result != None, "Funksjonen returnerer ingenting"
    assert type(result) == bool, "Funksjonen returnerer ikke riktig data-type"
    assert result == (num % 2 == 0), "Svarer ikke riktig på om ett tall er partall"

def test_erOddetall():
  assert hasattr(oppgaver.opg03, "erOddetall"), "Funksjonen erOddetall() eksisterer ikke"
  func = getattr(oppgaver.opg03, "erOddetall")
  assert len(inspect.signature(func).parameters) == 1, "Funksjonen har ikke riktig antall parametere"
  for _ in range(0, 10):
    num = random.randint(0,9999)
    result = func(num)
    assert result != None, "Funksjonen returnerer ingenting"
    assert type(result) == bool, "Funksjonen returnerer ikke riktig data-type"
    assert result != (num % 2 == 0), "Svarer ikke riktig på om ett tall er oddetall"