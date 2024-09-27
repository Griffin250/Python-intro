import oppgaver.opg05

def test_brukere():
  assert hasattr(oppgaver.opg05, "brukere"), "Variablen brukere eksisterer ikke"
  var = getattr(oppgaver.opg05, "brukere")
  assert len(var) == 3, "Variablen inneholder ikke 3 ordbøker"
  for el in range(len(var)):
    assert "navn" in var[el], f"Ordbok {el} har ikke nøkkelen: navn"
    assert "alder" in var[el], f"Ordbok {el} har ikke nøkkelen: alder"
    assert type(var[el]['navn']) == str, f"Ordbok {el} navn er ikke av typen streng"
    assert type(var[el]['alder']) == int, f"Ordbok {el} alder er ikke av typen integer"