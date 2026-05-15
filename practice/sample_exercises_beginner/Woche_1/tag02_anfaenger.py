# tag02_anfaenger.py
# Lerntag 2 - Kontrollstrukturen und Funktionen (Anfaenger)
# Thema: if/elif/else, for, while, def, return
# Ausfuehren in Spyder: F5

print("=" * 60)
print("LERNTAG 2 - Kontrollstrukturen und Funktionen (Anfaenger)")
print("=" * 60)

# AUFGABE 1: if / elif / else
print("\nAUFGABE 1: if/elif/else")
for note in [1, 2, 3, 4, 5, 6]:
    if note == 1:
        bewertung = "Sehr gut"
    elif note == 2:
        bewertung = "Gut"
    elif note == 3:
        bewertung = "Befriedigend"
    elif note == 4:
        bewertung = "Ausreichend"
    elif note == 5:
        bewertung = "Mangelhaft"
    else:
        bewertung = "Ungenuegend"
    print(f"  Note {note}: {bewertung}")
# LOESUNG: if prueft erste Bedingung, elif folgebedingungen, else alles andere.

# AUFGABE 2: for-Schleife mit range
print("\nAUFGABE 2: for + range")
print("Ungerade Zahlen 1-20:")
ungerade = [x for x in range(1, 21, 2)]
print(f"  {ungerade}")
summe = 0
for i in range(1, 101):
    summe += i
print(f"Summe 1 bis 100: {summe}")
# LOESUNG: range(start, stop, step). Summe 1..100 = 5050 (Gauss).

# AUFGABE 3: for ueber Listen und Dicts
print("\nAUFGABE 3: for ueber Listen/Dicts")
einkauf = {"Milch":1.29, "Brot":2.49, "Butter":1.89, "Kaffee":4.99}
gesamt = 0
for artikel, preis in einkauf.items():
    gesamt += preis
    print(f"  {artikel:<10} {preis:>5.2f} EUR")
print(f"  {'GESAMT':<10} {gesamt:>5.2f} EUR")
# LOESUNG: .items() gibt (schluessel, wert)-Tupel. :> rechtsbündig formatieren.

# AUFGABE 4: while-Schleife
print("\nAUFGABE 4: while")
n = 1
while n <= 512:
    print(f"  {n}", end=" ")
    n *= 2
print()
# LOESUNG: while laeuft solange Bedingung True. Hier: Potenzen von 2.

# AUFGABE 5: break und continue
print("\nAUFGABE 5: break / continue")
print("Zahlen 1-20, gerade ueberspringen, bei 15 stoppen:")
for i in range(1, 21):
    if i % 2 == 0:
        continue    # gerade Zahlen ueberspringen
    if i > 15:
        break       # bei >15 aufhoeren
    print(f"  {i}", end=" ")
print()
# LOESUNG: continue springt zur naechsten Iteration, break verlasst die Schleife.

# AUFGABE 6: Einfache Funktion definieren
print("\nAUFGABE 6: Einfache Funktion")
def begruessung(name, uhrzeit=12):
    if uhrzeit < 12:
        gruss = "Guten Morgen"
    elif uhrzeit < 18:
        gruss = "Guten Tag"
    else:
        gruss = "Guten Abend"
    return f"{gruss}, {name}!"

print(begruessung("Anna", 9))
print(begruessung("Bob", 14))
print(begruessung("Cara"))       # Standardwert uhrzeit=12
# LOESUNG: def name(param, param=standard): body. return gibt Wert zurueck.

# AUFGABE 7: Funktion mit mehreren Rueckgabewerten
print("\nAUFGABE 7: Mehrere Rueckgabewerte")
def statistik(zahlen):
    return min(zahlen), max(zahlen), sum(zahlen)/len(zahlen)

daten = [23, 45, 12, 67, 34, 89, 11, 56]
minimum, maximum, mittel = statistik(daten)
print(f"Daten:       {daten}")
print(f"Min:         {minimum}")
print(f"Max:         {maximum}")
print(f"Mittelwert:  {mittel:.2f}")
# LOESUNG: return a, b, c gibt Tupel zurueck. Unpacking bei Zuweisung.

# AUFGABE 8: Rekursion
print("\nAUFGABE 8: Rekursion (Fakultaet)")
def fakultaet(n):
    if n <= 1:
        return 1
    return n * fakultaet(n-1)

for i in range(1, 8):
    print(f"  {i}! = {fakultaet(i)}")
# LOESUNG: Rekursion = Funktion ruft sich selbst auf. Basisfall (n<=1) stoppt sie.

# AUFGABE 9: Verschachtelte Schleifen
print("\nAUFGABE 9: Verschachtelte Schleifen")
print("Kleines Einmaleins (1-5):")
print("    ", end="")
for j in range(1,6): print(f"{j:4}", end="")
print()
for i in range(1,6):
    print(f"{i:3}:", end="")
    for j in range(1,6):
        print(f"{i*j:4}", end="")
    print()
# LOESUNG: Aeussere Schleife = Zeilen, innere Schleife = Spalten.

# AUFGABE 10: Kombiniert - Primzahlen
print("\nAUFGABE 10: Primzahlen bis 50")
def ist_primzahl(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primzahlen = [n for n in range(2, 51) if ist_primzahl(n)]
print(f"Primzahlen bis 50: {primzahlen}")
print(f"Anzahl: {len(primzahlen)}")
# LOESUNG: Nur bis Wurzel(n) pruefen reicht. List Comprehension mit Funktion.

print("\n" + "=" * 60)
print("Tag 2 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
