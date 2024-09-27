# Repetisjonsoppgaver i Python

Løs oppgavene i mappen `oppgaver/`


## Unit Testing i utvikling

1. "Fork" dette repoet til deg selv.
2. Klon det "Fork"-ede repoet
3. Kjør en `pip install -r requirements.txt` i mappen
4. Kjør `pytest` kommandoen for å se om kode-testene "PASS"-er
5. Fullfør scriptene i `app/` slik at testene "PASS"-er
6. Gå til 4. helt til alle testene "PASS"-er


## Utfyllende feilede tester
For å få mer utfyllende feilmelding på testene, kjør:

`pytest --tb=short` eller `pytest --tb=long`


## Pytest kommandoen fungerer ikke

1. Skriv `pip show pytest`, og gå til mappen på maskinen som verdien `Location: ` peker mot.

   Oftest noe som slutter på `\Lib\site-packages`

2. Gå ut 2 mapper til du ser mappen `Scripts`
3. Gå inn i `Scripts` og sjekk at `pytest.exe` ligger der
4. Kopier hele/absolutt banen/path til `Scripts` mappen
5. Trykk <kbd>Win</kbd>+<kbd>R</kbd> og fyll inn `"C:\Windows\system32\rundll32.exe" sysdm.cpl,EditEnvironmentVariables` i Åpne feltet, deretter klikk <kbd>OK</kbd>
6. På listen `Brukervariabler for ...`, dobbeltklikk på variablen `Path`.
7. Klikk på <kbd>Ny</kbd>, og legg inn banen/path til den `Scripts` mappen som kopiert over.
8. Klikk <kbd>OK</kbd>, og lukk alt.
9. Start VSCode etc. på nytt for at endringen skal tre i kraft.# Python-intro
