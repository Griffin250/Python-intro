import oppgaver.opg02
import inspect
import random

def test_leggSammen():
  assert hasattr(oppgaver.opg02, "leggSammen"), "Funksjonen leggSammen() eksisterer ikke"
  func = getattr(oppgaver.opg02, "leggSammen")
  assert len(inspect.signature(func).parameters) == 2, "Funksjonen har ikke riktig antall parametere"
  for _ in range(0, 10):
    num1 = random.randint(0,9999) + (random.randint(10,100)/10)
    num2 = random.randint(0,9999) + (random.randint(10,100)/10)
    result = func(num1, num2)
    assert result != None, "Funksjonen returnerer ingenting"
    assert type(result) == float, "Funksjonen returnerer ikke riktig data-type"
    assert result == num1 + num2, "Funksjonen regner ikke riktig sum av tallene"
