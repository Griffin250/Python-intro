import oppgaver.opg10
import inspect
import random

def test_Kalkulator():
  assert hasattr(oppgaver.opg10, "Kalkulator"), "Klassen Kalkulator eksisterer ikke"
  calcclass:oppgaver.opg10.Kalkulator = getattr(oppgaver.opg10, "Kalkulator")
  assert len(inspect.signature(calcclass).parameters) == 1, "Klassen Kalkulator skal ha en konstruktør med 1 parameter"

  assert type(inspect.signature(calcclass).parameters.get('resultat').default) == float, "Parameteren resultat i konstruktøren er ikke ett flyttall"
  assert inspect.signature(calcclass).parameters.get('resultat').default == 0.0, "Parameteren resultat i konstruktøren har ikke standardverdi 0.0"
  
  assert hasattr(calcclass, "pluss"), "Klassen Kalkulator har ikke funksjonen pluss"
  assert hasattr(calcclass, "minus"), "Klassen Kalkulator har ikke funksjonen minus"
  assert hasattr(calcclass, "gange"), "Klassen Kalkulator har ikke funksjonen gange"
  assert hasattr(calcclass, "dele"), "Klassen Kalkulator har ikke funksjonen dele"

  #assert hasattr(calcclass, "__loggHistorikk"), "Klassen Kalkulator har ikke funksjonen __loggHistorikk"  

  assert hasattr(calcclass, "giResultat"), "Klassen Kalkulator har ikke funksjonen giResultat"
  assert hasattr(calcclass, "giHistorikk"), "Klassen Kalkulator har ikke funksjonen giHistorikk"

  assert len(inspect.signature(calcclass.pluss).parameters) == 2, "Funksjonen pluss i klassen Kalkulator har ikke en parameter og self"
  assert len(inspect.signature(calcclass.minus).parameters) == 2, "Funksjonen minus i klassen Kalkulator har ikke en parameter og self"
  assert len(inspect.signature(calcclass.gange).parameters) == 2, "Funksjonen gange i klassen Kalkulator har ikke en parameter og self"
  assert len(inspect.signature(calcclass.dele).parameters) == 2, "Funksjonen dele i klassen Kalkulator har ikke en parameter og self"

  for _ in range(20):
    result:float = 0.0
    hist:list = []
    inst = oppgaver.opg10.Kalkulator()
    for _ in range(random.randint(5, 20)):
      num = random.randint(1, 100)
      pre = inst.giResultat()
      oper = random.randint(0,4)
      match oper:
        case 0:
          hist.append(f"{result} + {num} = {result+num}")
          inst.pluss(num)
          result += num
          assert inst.giResultat() == result, f"Kalkulatorens pluss funksjon regner ikke riktig. {pre} + {num} = {inst.giResultat()} | Forventet svar: {result}"
        case 1:
          hist.append(f"{result} - {num} = {result-num}")
          inst.minus(num)
          result -= num
          assert inst.giResultat() == result, f"Kalkulatorens minus funksjon regner ikke riktig. {pre} - {num} = {inst.giResultat()} | Forventet svar: {result}"
        case 2:
          hist.append(f"{result} * {num} = {result*num}")
          inst.gange(num)
          result *= num
          assert inst.giResultat() == result, f"Kalkulatorens gange funksjon regner ikke riktig. {pre} * {num} = {inst.giResultat()} | Forventet svar: {result}"
        case 3:
          hist.append(f"{result} / {num} = {result/num}")
          inst.dele(num)
          result /= num
          assert inst.giResultat() == result, f"Kalkulatorens dele funksjon regner ikke riktig. {pre} / {num} = {inst.giResultat()} | Forventet svar: {result}"
        case _:
          pass
    assert inst.giResultat() == result, f"Kalkulatoren regner feil. Svaret var: {inst.giResultat()} | Forventet svar: {result}"
    assert hist == inst.giHistorikk(), f"Kalkulatoren gir feil historikk: Svar: {inst.giHistorikk()} | Forventet: {hist}"

  for _ in range(20):
    result:float = random.randint(10,99999) + (random.randint(10,99)/10)
    hist:list = []
    inst = oppgaver.opg10.Kalkulator(result)
    for _ in range(random.randint(5, 20)):
      num = random.randint(1, 100)
      pre = inst.giResultat()
      oper = random.randint(0,4)
      match oper:
        case 0:
          hist.append(f"{result} + {num} = {result+num}")
          inst.pluss(num)
          result += num
          assert inst.giResultat() == result, f"Kalkulatorens pluss funksjon regner ikke riktig. {pre} + {num} = {inst.giResultat()} | Forventet svar: {result}"
        case 1:
          hist.append(f"{result} - {num} = {result-num}")
          inst.minus(num)
          result -= num
          assert inst.giResultat() == result, f"Kalkulatorens minus funksjon regner ikke riktig. {pre} - {num} = {inst.giResultat()} | Forventet svar: {result}"
        case 2:
          hist.append(f"{result} * {num} = {result*num}")
          inst.gange(num)
          result *= num
          assert inst.giResultat() == result, f"Kalkulatorens gange funksjon regner ikke riktig. {pre} * {num} = {inst.giResultat()} | Forventet svar: {result}"
        case 3:
          hist.append(f"{result} / {num} = {result/num}")
          inst.dele(num)
          result /= num
          assert inst.giResultat() == result, f"Kalkulatorens dele funksjon regner ikke riktig. {pre} / {num} = {inst.giResultat()} | Forventet svar: {result}"
        case _:
          pass
    assert inst.giResultat() == result, f"Kalkulatoren regner feil. Svaret var: {inst.giResultat()} | Forventet svar: {result}"
    assert hist == inst.giHistorikk(), f"Kalkulatoren gir feil historikk: Svar: {inst.giHistorikk()} | Forventet: {hist}"


    assert oppgaver.opg10.Kalkulator(5).pluss(5).dele(2).gange(5).minus(20).giResultat() == 5, "Kalkulatoren ser ikke ut til å regne riktig når man tar flere operasjoner i serie."
        