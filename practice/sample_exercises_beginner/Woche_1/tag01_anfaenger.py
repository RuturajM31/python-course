#tag01_anfaenger.py
#Learning day 1 -Python basics: variables, data types, input/output (beginners)
#Run in Spyder: F5

print("=" * 60)
print("LERNTAG 1 - Python Grundlagen fuer Anfaenger")
print("=" * 60)

#TASK 1: Variables and data types
print("\nAUFGABE 1: Variablen und Datentypen")
name     = "Anna"
alter    = 28
groesse  = 1.72
student  = True
print(f"Name: {name}, Typ: {type(name)}")
print(f"Alter: {alter}, Typ: {type(alter)}")
print(f"Groesse: {groesse}, Typ: {type(groesse)}")
print(f"Student: {student}, Typ: {type(student)}")

#SOLUTION: Variables don't need a type, Python recognizes it automatically.
#TASK 2: Calculating with variables

print("\nAUFGABE 2: Arithmetik")
a, b = 17, 5
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} // {b} = {a//b}  (ganzzahlige Division)")
print(f"{a} % {b} = {a%b}   (Modulo/Rest)")
print(f"{a} ** {b} = {a**b}  (Potenz)")

# LOESUNG: // = ganzzahlige Division, % = Rest, ** = Potenz

# AUFGABE 3: String-Operationen

print("\nAUFGABE 3: Strings")
s = "Python ist toll"
print(f"Gross:      {s.upper()}")
print(f"Klein:      {s.lower()}")
print(f"Laenge:     {len(s)}")
print(f"Ersetzen:   {s.replace('toll','super')}")
print(f"Enthält 'ist': {'ist' in s}")
print(f"Aufteilen:  {s.split()}")

# LOESUNG: Strings haben viele Methoden: .upper(), .lower(), .replace(), .split()

# AUFGABE 4: f-Strings

print("\nAUFGABE 4: f-Strings")
vorname  = "Max"
nachname = "Mustermann"
gehalt   = 3456.789
print(f"Name: {vorname} {nachname}")
print(f"Gehalt: {gehalt:.2f} EUR")
print(f"Gehalt gerundet: {gehalt:,.0f} EUR")
print(f"Gross: {vorname.upper()} {nachname.upper()}")

# LOESUNG: f"Text {variable:.2f}" formatiert Zahlen direkt im String.

# AUFGABE 5: Eingabe vom Benutzer (simuliert)
print("\nAUFGABE 5: input() simuliert")


# In Spyder: input() wuerde warten. Hier simulieren wir:
benutzereingabe = "42"
zahl = int(benutzereingabe)
print(f"Eingabe als Text: '{benutzereingabe}', Typ: {type(benutzereingabe)}")
print(f"Als Zahl: {zahl}, Typ: {type(zahl)}")
print(f"Doppelt: {zahl * 2}")
# LOESUNG: input() gibt immer einen String zurueck -> int() oder float() zum Umwandeln.

# AUFGABE 6: Listen erstellen und nutzen
print("\nAUFGABE 6: Listen")
zahlen = [3, 7, 1, 9, 4, 6, 2, 8, 5]
print(f"Liste:      {zahlen}")
print(f"Laenge:     {len(zahlen)}")
print(f"Erstes:     {zahlen[0]}")
print(f"Letztes:    {zahlen[-1]}")
print(f"Slice [2:5]:{zahlen[2:5]}")
print(f"Sortiert:   {sorted(zahlen)}")
print(f"Maximum:    {max(zahlen)}")
print(f"Summe:      {sum(zahlen)}")
# LOESUNG: Listen mit [] erstellen. Index beginnt bei 0. -1 = letztes Element.

# AUFGABE 7: Listen veraendern
print("\nAUFGABE 7: Listen veraendern")
fruechte = ["Apfel", "Banane", "Kirsche"]
fruechte.append("Mango")
fruechte.insert(1, "Blaubeere")
fruechte.remove("Banane")
print(f"Nach append/insert/remove: {fruechte}")
fruechte.sort()
print(f"Sortiert: {fruechte}")
print(f"Laenge: {len(fruechte)}")
# LOESUNG: .append() anfuegen, .insert(i, x) einsetzen, .remove(x) loeschen.

# AUFGABE 8: Dictionaries
print("\nAUFGABE 8: Dictionaries")
person = {"name": "Lena", "alter": 32, "stadt": "Berlin", "beruf": "Ingenieurin"}
print(f"Name:   {person['name']}")
print(f"Stadt:  {person['stadt']}")
person["email"] = "lena@beispiel.de"
person["alter"] = 33
print(f"Nach Update: {person}")
print(f"Schluessel: {list(person.keys())}")
print(f"'beruf' vorhanden: {'beruf' in person}")
# LOESUNG: Dicts mit {} und key:value Paaren. Zugriff mit dict['key'].

# AUFGABE 9: Tupel und Sets
print("\nAUFGABE 9: Tupel und Sets")
koordinaten = (48.1372, 11.5755)   # Tupel: unveraenderlich
print(f"Koordinaten: Lat={koordinaten[0]}, Lon={koordinaten[1]}")
farben = {"rot", "blau", "gruen", "rot", "blau"}
print(f"Set (keine Duplikate): {farben}")
print(f"Schnittmenge: {farben & {'rot','gelb','gruen'}}")
# LOESUNG: Tupel () = unveraenderlich. Set {} = keine Duplikate, keine Reihenfolge.

# AUFGABE 10: Typumwandlung
print("\nAUFGABE 10: Typumwandlung")
werte = ["3.14", "42", "True", 100, 3.99]
print(f"float('3.14') = {float('3.14')}")
print(f"int('42')     = {int('42')}")
print(f"str(100)      = '{str(100)}'")
print(f"bool(0)       = {bool(0)}")
print(f"bool(42)      = {bool(42)}")
print(f"int(3.99)     = {int(3.99)}  (kein Runden!)")
print(f"list('abc')   = {list('abc')}")
# LOESUNG: int(), float(), str(), bool(), list() wandeln Typen um.

print("\n" + "=" * 60)
print("Tag 1 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
