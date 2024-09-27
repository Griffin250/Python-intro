import oppgaver.opg08
import pytest
import inspect
import random
import string

def test_constants():
  assert hasattr(oppgaver.opg08, "PASSORD"), "Variablen PASSORD eksisterer ikke"
  assert hasattr(oppgaver.opg08, "SUCCESS_MSG"), "Variablen SUCCESS_MSG eksisterer ikke"
  assert hasattr(oppgaver.opg08, "FAILED_MSG"), "Variablen FAILED_MSG eksisterer ikke"

def test_sjekkPassord():
  assert hasattr(oppgaver.opg08, "sjekkPassord"), "Funksjonen sjekkPassord eksisterer ikke"
  func = getattr(oppgaver.opg08, "sjekkPassord")
  assert len(inspect.signature(func).parameters) == 1, "Funksjonen sjekkPassord skal ha 1 parameter"
  for _ in range(5):
    with pytest.raises(Exception):
      func("".join([d for d in random.choices(string.ascii_letters, k=random.randint(20,30))]))
  assert func(oppgaver.opg08.PASSORD), "Funksjonen returnerer ikke True ved riktig passord"

def test_passordRespons():
  assert hasattr(oppgaver.opg08, "passordRespons"), "Funksjonen passordRespons eksisterer ikke"
  func = getattr(oppgaver.opg08, "passordRespons")
  assert len(inspect.signature(func).parameters) == 1, "Funksjonen passordRespons skal ha 1 parameter"
  for _ in range(5):
    wpass = "".join([d for d in random.choices(string.ascii_letters, k=random.randint(20,30))])
    assert func(wpass) == oppgaver.opg08.FAILED_MSG, f"Passordet {wpass} fikk ikke responsen {oppgaver.opg08.FAILED_MSG}"
  assert func(oppgaver.opg08.PASSORD) == oppgaver.opg08.SUCCESS_MSG, f"Passordet {oppgaver.opg08.PASSORD} fikk ikke responsen {oppgaver.opg08.SUCCESS_MSG}"