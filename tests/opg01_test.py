import oppgaver.opg01

def variabel_tester(name:str, type, error:str):
  assert hasattr(oppgaver.opg01, name), f"Variablen {name} eksisterer ikke"
  assert isinstance(getattr(oppgaver.opg01, name, None), type), f"{name} {error}"


def test_var1_type():
  variabel_tester("var1", str, "er ikke en streng")

def test_var2_type():
  variabel_tester("var2", int, "er ikke en integer")

def test_var3_type():
  variabel_tester("var3", float, "er ikke ett flyttall")

def test_var4_type():
  variabel_tester("var4", bool, "er ikke en boolsk variabel")

def test_var5_type():
  variabel_tester("var5", list, "er ikke en liste")

def test_var6_type():
  variabel_tester("var6", dict, "er ikke en ordbok")