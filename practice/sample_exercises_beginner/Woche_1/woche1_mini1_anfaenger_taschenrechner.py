# woche1_mini1_anfaenger_taschenrechner.py
# MINIPROJEKT WOCHE 1 - Anfaenger (1/2)
# Titel: Wissenschaftlicher Taschenrechner mit Verlauf
# Thema: Variablen, Funktionen, Kontrollstrukturen, Dicts, Listen (Lerntage 1-3)
# Ausfuehren in Spyder: F5

import math

print("=" * 60)
print("MINIPROJEKT W1/1 (Anfaenger): Wissenschaftlicher Taschenrechner")
print("=" * 60)

# --- Grundoperationen ---
def addiere(a, b):    return a + b
def subtrahiere(a, b):return a - b
def multipliziere(a, b): return a * b
def dividiere(a, b):
    if b == 0: raise ValueError("Division durch Null nicht erlaubt!")
    return a / b
def potenz(a, b):     return a ** b
def wurzel(a):
    if a < 0: raise ValueError("Keine reelle Wurzel aus negativer Zahl!")
    return math.sqrt(a)
def logarithmus(a, basis=10):
    if a <= 0: raise ValueError("Logarithmus nur fuer positive Zahlen!")
    return math.log(a, basis)
def sinus(grad):      return math.sin(math.radians(grad))
def kosinus(grad):    return math.cos(math.radians(grad))
def tangens(grad):
    if grad % 180 == 90: raise ValueError("tan(90°) nicht definiert!")
    return math.tan(math.radians(grad))

# --- Taschenrechner-Klasse ---
class Taschenrechner:
    OPERATIONEN = {
        "+":  ("addiere",       2, addiere),
        "-":  ("subtrahiere",   2, subtrahiere),
        "*":  ("multipliziere", 2, multipliziere),
        "/":  ("dividiere",     2, dividiere),
        "**": ("Potenz",        2, potenz),
        "√":  ("Wurzel",        1, wurzel),
        "log":("Logarithmus",   1, logarithmus),
        "sin":("Sinus (Grad)",  1, sinus),
        "cos":("Kosinus (Grad)",1, kosinus),
        "tan":("Tangens (Grad)",1, tangens),
    }

    def __init__(self):
        self.verlauf     = []
        self.speicher    = 0.0
        self.letztes_ergebnis = None

    def berechne(self, op, a, b=None):
        if op not in self.OPERATIONEN:
            raise ValueError(f"Unbekannte Operation: {op}")
        name, stellig, func = self.OPERATIONEN[op]
        try:
            if stellig == 1:
                ergebnis = func(a)
                ausdruck = f"{op}({a}) = {ergebnis}"
            else:
                ergebnis = func(a, b)
                ausdruck = f"{a} {op} {b} = {ergebnis}"
            self.verlauf.append({"ausdruck": ausdruck, "ergebnis": ergebnis})
            self.letztes_ergebnis = ergebnis
            return ergebnis
        except Exception as e:
            fehler = f"FEHLER bei {op}: {e}"
            self.verlauf.append({"ausdruck": fehler, "ergebnis": None})
            return None

    def speichern(self):
        if self.letztes_ergebnis is not None:
            self.speicher = self.letztes_ergebnis
            print(f"   Im Speicher: {self.speicher}")

    def speicher_laden(self):
        return self.speicher

    def verlauf_anzeigen(self):
        print("\n--- Berechnungsverlauf ---")
        for i, v in enumerate(self.verlauf, 1):
            print(f"  {i:2}. {v['ausdruck']}")

    def statistik(self):
        ergebnisse = [v["ergebnis"] for v in self.verlauf if v["ergebnis"] is not None]
        if not ergebnisse: return
        print(f"\n--- Statistik ({len(ergebnisse)} erfolgreiche Berechnungen) ---")
        print(f"  Minimum:     {min(ergebnisse):.6g}")
        print(f"  Maximum:     {max(ergebnisse):.6g}")
        print(f"  Mittelwert:  {sum(ergebnisse)/len(ergebnisse):.6g}")

# --- Demonstration ---
tr = Taschenrechner()

print("\n1) Grundrechenarten:")
for op, a, b in [("+",15,27),("-",100,37.5),("*",6,7),("/",355,113),("**",2,10)]:
    r = tr.berechne(op, a, b)
    print(f"   {a} {op} {b} = {r:.6g}")

print("\n2) Wissenschaftliche Funktionen:")
for op, a in [("√",144),("log",1000),("sin",30),("cos",60),("tan",45)]:
    r = tr.berechne(op, a)
    print(f"   {op}({a}) = {r:.6g}")

print("\n3) Speicher:")
tr.berechne("**", 2, 10)
tr.speichern()
gespeichert = tr.speicher_laden()
r = tr.berechne("*", gespeichert, 3)
print(f"   Speicher ({gespeichert}) * 3 = {r}")

print("\n4) Fehlerbehandlung:")
tr.berechne("/", 5, 0)
tr.berechne("√", -9)
tr.berechne("tan", 90)

tr.verlauf_anzeigen()
tr.statistik()

# --- Ergebnisse speichern ---
import csv
with open("taschenrechner_verlauf.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Nr","Ausdruck","Ergebnis"])
    for i,v in enumerate(tr.verlauf,1):
        w.writerow([i, v["ausdruck"], v["ergebnis"]])
print("\ntaschenrechner_verlauf.csv gespeichert.")
print("\n" + "=" * 60)
print("Miniprojekt W1/1 abgeschlossen!")
print("=" * 60)
