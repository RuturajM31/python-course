# tag03_anfaenger.py
# Lerntag 3 - OOP Grundlagen (Anfaenger)
# Thema: Klassen, Objekte, __init__, Methoden, Vererbung
# Ausfuehren in Spyder: F5

print("=" * 60)
print("LERNTAG 3 - Objektorientierung fuer Anfaenger")
print("=" * 60)

# AUFGABE 1: Einfache Klasse
print("\nAUFGABE 1: Einfache Klasse")
class Tier:
    def __init__(self, name, art, alter):
        self.name  = name
        self.art   = art
        self.alter = alter

    def vorstellen(self):
        return f"Ich bin {self.name}, ein {self.art}, {self.alter} Jahre alt."

hund = Tier("Bello", "Hund", 4)
katze= Tier("Mimi",  "Katze", 7)
print(hund.vorstellen())
print(katze.vorstellen())
# LOESUNG: class Name: + __init__(self,...) als Konstruktor. self = das Objekt selbst.

# AUFGABE 2: Attribute und Methoden
print("\nAUFGABE 2: Methoden")
class Konto:
    def __init__(self, inhaber, stand=0.0):
        self.inhaber = inhaber
        self.stand   = stand
        self.history = []

    def einzahlen(self, betrag):
        self.stand += betrag
        self.history.append(f"+{betrag:.2f}")

    def abheben(self, betrag):
        if betrag > self.stand:
            return "Nicht genug Guthaben!"
        self.stand -= betrag
        self.history.append(f"-{betrag:.2f}")
        return f"{betrag:.2f} EUR abgehoben."

    def __str__(self):
        return f"Konto {self.inhaber}: {self.stand:.2f} EUR"

k = Konto("Max", 100)
k.einzahlen(250)
print(k.abheben(80))
print(k.abheben(500))
print(k)
print(f"Historie: {k.history}")
# LOESUNG: __str__ bestimmt, was print(objekt) ausgibt.

# AUFGABE 3: Klassenattribute
print("\nAUFGABE 3: Klassenattribute")
class Student:
    anzahl = 0  # Klassenattribut - geteilt von allen Instanzen

    def __init__(self, name, fach):
        self.name = name
        self.fach = fach
        Student.anzahl += 1

    @classmethod
    def wieviele(cls):
        return f"{cls.anzahl} Studenten registriert"

s1 = Student("Anna","Informatik")
s2 = Student("Bob", "Mathematik")
s3 = Student("Cara","Physik")
print(Student.wieviele())
print(f"s1.anzahl = {s1.anzahl}  (gleich fuer alle)")
# LOESUNG: Klassenattribute gehoeren der Klasse, nicht der Instanz.

# AUFGABE 4: Vererbung
print("\nAUFGABE 4: Vererbung")
class Fahrzeug:
    def __init__(self, marke, baujahr):
        self.marke   = marke
        self.baujahr = baujahr

    def info(self):
        return f"{self.marke} ({self.baujahr})"

class Auto(Fahrzeug):
    def __init__(self, marke, baujahr, ps):
        super().__init__(marke, baujahr)
        self.ps = ps

    def info(self):
        return f"{super().info()}, {self.ps} PS"

class Elektroauto(Auto):
    def __init__(self, marke, baujahr, ps, reichweite):
        super().__init__(marke, baujahr, ps)
        self.reichweite = reichweite

    def info(self):
        return f"{super().info()}, {self.reichweite} km Reichweite"

f = Fahrzeug("Fahrrad",  2020)
a = Auto("BMW", 2022, 184)
e = Elektroauto("Tesla", 2023, 450, 580)
for obj in [f, a, e]:
    print(f"  {obj.info()}")
# LOESUNG: super().__init__() ruft Konstruktor der Elternklasse auf.

# AUFGABE 5: isinstance und issubclass
print("\nAUFGABE 5: isinstance / issubclass")
print(f"e ist Auto?        {isinstance(e, Auto)}")
print(f"e ist Fahrzeug?    {isinstance(e, Fahrzeug)}")
print(f"a ist Elektroauto? {isinstance(a, Elektroauto)}")
print(f"Elektroauto < Auto?    {issubclass(Elektroauto, Auto)}")
print(f"Elektroauto < Fahrzeug?{issubclass(Elektroauto, Fahrzeug)}")
# LOESUNG: isinstance prueft Instanz, issubclass prueft Klassenhierarchie.

# AUFGABE 6: Dunder-Methoden
print("\nAUFGABE 6: Dunder-Methoden")
class Vektor:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vektor({self.x}, {self.y})"

    def __add__(self, other):
        return Vektor(self.x+other.x, self.y+other.y)

    def __mul__(self, scalar):
        return Vektor(self.x*scalar, self.y*scalar)

    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

v1 = Vektor(3, 4)
v2 = Vektor(1, 2)
print(f"v1 = {v1}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 * 3  = {v1 * 3}")
print(f"|v1|    = {abs(v1):.2f}")
# LOESUNG: __add__, __mul__, __abs__ usw. erlauben Operatoren fuer eigene Klassen.

# AUFGABE 7: Properties
print("\nAUFGABE 7: Properties")
class Temperatur:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, wert):
        if wert < -273.15:
            raise ValueError("Unter dem absoluten Nullpunkt!")
        self._celsius = wert

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @property
    def kelvin(self):
        return self._celsius + 273.15

t = Temperatur(100)
print(f"{t.celsius}°C = {t.fahrenheit}°F = {t.kelvin}K")
t.celsius = -40
print(f"{t.celsius}°C = {t.fahrenheit}°F")
# LOESUNG: @property macht Methode wie Attribut nutzbar. @x.setter = Schreibzugriff.

# AUFGABE 8: Statische Methoden
print("\nAUFGABE 8: Statische Methoden")
class Rechner:
    @staticmethod
    def addiere(a, b):   return a + b

    @staticmethod
    def ist_primzahl(n):
        if n < 2: return False
        return all(n%i != 0 for i in range(2, int(n**0.5)+1))

    @staticmethod
    def ggT(a, b):
        while b: a, b = b, a%b
        return a

print(f"5+3={Rechner.addiere(5,3)}, ggT(48,18)={Rechner.ggT(48,18)}")
print(f"Primzahlen bis 30: {[n for n in range(2,31) if Rechner.ist_primzahl(n)]}")
# LOESUNG: @staticmethod braucht kein self/cls. Kein Zugriff auf Instanz/Klasse noetig.

# AUFGABE 9: Abstrakte Klassen
print("\nAUFGABE 9: Abstrakte Klassen")
from abc import ABC, abstractmethod

class Form(ABC):
    @abstractmethod
    def flaeche(self): pass

    @abstractmethod
    def umfang(self): pass

    def beschreiben(self):
        return f"{type(self).__name__}: Flaeche={self.flaeche():.2f}, Umfang={self.umfang():.2f}"

class Kreis(Form):
    def __init__(self, r): self.r = r
    def flaeche(self): return 3.14159 * self.r**2
    def umfang(self): return 2 * 3.14159 * self.r

class Rechteck(Form):
    def __init__(self, b, h): self.b, self.h = b, h
    def flaeche(self): return self.b * self.h
    def umfang(self): return 2*(self.b + self.h)

for f in [Kreis(5), Rechteck(4,7)]:
    print(f"  {f.beschreiben()}")
# LOESUNG: ABC = abstrakte Basisklasse. @abstractmethod muss in Unterklasse implementiert werden.

# AUFGABE 10: Vollstaendiges Beispiel
print("\nAUFGABE 10: Bibliotheksverwaltung")
class Buch:
    def __init__(self, titel, autor, seiten):
        self.titel, self.autor, self.seiten = titel, autor, seiten
        self.ausgeliehen = False

    def __repr__(self):
        status = "ausgeliehen" if self.ausgeliehen else "verfuegbar"
        return f"'{self.titel}' von {self.autor} [{status}]"

class Bibliothek:
    def __init__(self, name):
        self.name   = name
        self.buecher = []

    def hinzufuegen(self, buch):
        self.buecher.append(buch)

    def verfuegbare(self):
        return [b for b in self.buecher if not b.ausgeliehen]

    def ausleihen(self, titel):
        for b in self.buecher:
            if b.titel == titel and not b.ausgeliehen:
                b.ausgeliehen = True
                return f"'{titel}' ausgeliehen."
        return "Nicht verfuegbar."

bib = Bibliothek("Stadtbibliothek")
for t,a,s in [("Python lernen","Lutz",600),("Clean Code","Martin",464),("Der Hobbit","Tolkien",310)]:
    bib.hinzufuegen(Buch(t,a,s))

print(bib.ausleihen("Clean Code"))
print(f"Verfuegbar: {bib.verfuegbare()}")
# LOESUNG: Mehrere Klassen arbeiten zusammen (Komposition).

print("\n" + "=" * 60)
print("Tag 3 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
