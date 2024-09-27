import oppgaver.opg06
import inspect
import random
import os
import string

def test_skrivLogg():
  assert hasattr(oppgaver.opg06, "skrivLogg"), "Funksjonen skrivLogg eksisterer ikke"
  func = getattr(oppgaver.opg06, "skrivLogg")
  assert len(inspect.signature(func).parameters) == 1, "Funksjonen har ikke riktig antall parametere"
  for _ in range(random.randint(10,30)):
    if os.path.isfile("loggfil.log"):
      os.remove("loggfil.log")
      assert not os.path.isfile("loggfil.log"), "Klarer ikke slette loggfilen"
    output = ""
    for l in range(random.randint(2,30)):
      output += "".join(random.choices(string.ascii_letters+string.digits, k=random.randint(3, 30)))+"\n"
    assert func(output) == None, "Funksjonen returnerer noe, det skal den ikke"
    f = open("loggfil.log", "r")
    assert f.read() == output
    f.close()
  
  # Cleanup
  if os.path.isfile("loggfil.log"):
    os.remove("loggfil.log")