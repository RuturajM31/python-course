# tag10_anfaenger.py
# Lerntag 10 - Regular Expressions: Grundlagen (Anfaenger)
# Thema: search, match, findall, sub, Gruppen, split
# Ausfuehren in Spyder: F5

import re

print("=" * 60)
print("LERNTAG 10 - Regular Expressions fuer Anfaenger")
print("=" * 60)

# AUFGABE 1: re.search
print("\nAUFGABE 1: re.search")
text = "Ich lerne Python und finde es grossartig."
m = re.search(r"Python", text)
if m: print(f"Gefunden: '{m.group()}' an Position {m.start()}")
# LOESUNG: re.search(muster,text) durchsucht ganzen String. Gibt None wenn kein Treffer.

# AUFGABE 2: re.match - nur am Anfang
print("\nAUFGABE 2: re.match")
for s in ["Hallo Welt!", "Welt, Hallo!", "Hallo Python"]:
    print(f"  '{s}' -> match: {bool(re.match(r'Hallo',s))}")
# LOESUNG: match() prueft NUR am Anfang des Strings.

# AUFGABE 3: Grossbuchstaben-Woerter
print("\nAUFGABE 3: findall - Grossbuchstaben")
text = "Anna und Ben wohnen in Berlin und Muenchen."
print("Gross:", re.findall(r"[A-Z][a-z]+", text))
# LOESUNG: [A-Z] = ein Grossbuchstabe, [a-z]+ = ein oder mehr Kleinbuchstaben.

# AUFGABE 4: Zahlen finden
print("\nAUFGABE 4: Zahlen")
text = "Der Kurs kostet 199 Euro, Rabatt 15%, 3 Plaetze."
print("Zahlen:", re.findall(r"\d+", text))
# LOESUNG: \d = Ziffer [0-9]. \d+ = eine oder mehr Ziffern.

# AUFGABE 5: re.sub - ersetzen
print("\nAUFGABE 5: re.sub")
text = "das ist ein test satz"
print("Leerzeichen->Unterstrich:", re.sub(r" ", "_", text))
# LOESUNG: re.sub(muster, ersatz, text) gibt modifizierten String zurueck.

# AUFGABE 6: E-Mail validieren
print("\nAUFGABE 6: E-Mail")
muster = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$"
for e in ["user@example.com","falsch@","test.name@mail.de","@kein.user"]:
    print(f"  {e:<25} -> {'gueltig' if re.match(muster,e) else 'ungueltig'}")

# AUFGABE 7: Gruppen
print("\nAUFGABE 7: Gruppen")
for p in ["Mustermann, Max","Mueller, Anna","Schmidt, Karl"]:
    m = re.match(r"(\w+),\s*(\w+)", p)
    if m: print(f"  Nachname: {m.group(1)}, Vorname: {m.group(2)}")

# AUFGABE 8: Punkt escapen
print("\nAUFGABE 8: Escapen")
text = "Der Preis: 19.99 Euro oder 19X99 Punkte."
print("Ohne Escape (. = alles):", re.findall(r"19.99", text))
print("Mit Escape  (nur .)    :", re.findall(r"19\.99", text))

# AUFGABE 9: Optional mit ?
print("\nAUFGABE 9: Optional")
for w in ["color","colour","colored","coloured"]:
    print(f"  '{w}': {bool(re.match(r'colou?r', w))}")
# LOESUNG: u? bedeutet 'u kommt 0 oder 1 Mal vor'.

# AUFGABE 10: re.split mit mehreren Trennzeichen
print("\nAUFGABE 10: re.split")
zeile = "Berlin,Hamburg;Muenchen\tKoeln,Frankfurt"
print("Aufgeteilt:", re.split(r"[,;\t]", zeile))
# LOESUNG: [,;\t] = Zeichenklasse - Komma, Semikolon oder Tab als Trenner.

print("\n" + "=" * 60)
print("Tag 10 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
