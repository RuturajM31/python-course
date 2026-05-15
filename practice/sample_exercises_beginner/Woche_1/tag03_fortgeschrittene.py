# tag03_fortgeschrittene.py
# Lerntag 3 - OOP Fortgeschrittene
# Thema: Dataclasses, Slots, MRO, Mixins, Protokolle, __slots__
# Ausfuehren in Spyder: F5

from dataclasses import dataclass, field
from typing import Protocol, ClassVar
import functools

print("=" * 60)
print("LERNTAG 3 - OOP Fortgeschrittene")
print("=" * 60)

# AUFGABE 1: Dataclasses
print("\nAUFGABE 1: Dataclasses")
@dataclass(order=True)
class Punkt:
    x: float
    y: float
    z: float = 0.0

    def distanz(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __post_init__(self):
        if self.distanz() > 1000:
            raise ValueError("Punkt zu weit vom Ursprung")

punkte = [Punkt(3,4), Punkt(1,1), Punkt(0,5,12)]
for p in punkte:
    print(f"  {p}  |  Distanz={p.distanz():.2f}")
print(f"Sortiert: {sorted(punkte)}")
# LOESUNG: @dataclass generiert __init__, __repr__, __eq__ automatisch.

# AUFGABE 2: Dataclass mit field()
print("\nAUFGABE 2: field()")
@dataclass
class Team:
    name:     str
    mitglieder: list = field(default_factory=list)
    punkte:   int = field(default=0, repr=True)
    _id:      ClassVar[int] = 0

    def __post_init__(self):
        Team._id += 1
        self.id = Team._id

    def hinzufuegen(self, name):
        self.mitglieder.append(name)

t1 = Team("Rote")
t2 = Team("Blaue", punkte=10)
t1.hinzufuegen("Anna"); t1.hinzufuegen("Bob")
print(f"{t1}  id={t1.id}")
print(f"{t2}  id={t2.id}")
# LOESUNG: field(default_factory=list) verhindert geteilte Mutable-Defaults.

# AUFGABE 3: MRO - Method Resolution Order
print("\nAUFGABE 3: MRO")
class A:
    def hallo(self): return "A"
class B(A):
    def hallo(self): return f"B->{super().hallo()}"
class C(A):
    def hallo(self): return f"C->{super().hallo()}"
class D(B, C):
    def hallo(self): return f"D->{super().hallo()}"

d = D()
print(f"D().hallo() = {d.hallo()}")
print(f"MRO: {[cls.__name__ for cls in D.__mro__]}")
# LOESUNG: Python nutzt C3-Linearisierung (links vor rechts, Kinder vor Eltern).

# AUFGABE 4: Mixins
print("\nAUFGABE 4: Mixins")
class LogMixin:
    def log(self, msg):
        print(f"  [{type(self).__name__}] {msg}")

class ValidierMixin:
    def validiere(self, wert, min_val, max_val):
        if not (min_val <= wert <= max_val):
            raise ValueError(f"{wert} nicht in [{min_val},{max_val}]")
        return True

class Sensor(LogMixin, ValidierMixin):
    def __init__(self, name):
        self.name   = name
        self.werte  = []

    def messen(self, wert):
        self.validiere(wert, -50, 150)
        self.werte.append(wert)
        self.log(f"Messung: {wert}°C")

s = Sensor("TempSensor01")
for w in [22.5, 37.1, 18.0]:
    s.messen(w)
print(f"  Mittelwert: {sum(s.werte)/len(s.werte):.2f}°C")
# LOESUNG: Mixins geben Klassen Zusatzfunktionen ohne tiefe Vererbung.

# AUFGABE 5: Protokolle (Structural Subtyping)
print("\nAUFGABE 5: Protocol")
class Sortierbar(Protocol):
    def __lt__(self, other) -> bool: ...

@dataclass(order=True)
class Produkt:
    preis: float
    name:  str

def kleinste(items):
    return min(items)

produkte = [Produkt(9.99,"Buch"), Produkt(4.49,"Stift"), Produkt(24.99,"Heft")]
print(f"Guenstigstes: {kleinste(produkte)}")
# LOESUNG: Protocol definiert Interface ohne Vererbung ("duck typing mit Typcheck").

# AUFGABE 6: __slots__ fuer Speichereffizienz
print("\nAUFGABE 6: __slots__")
class PunktNormal:
    def __init__(self, x, y): self.x, self.y = x, y

class PunktSlots:
    __slots__ = ["x","y"]
    def __init__(self, x, y): self.x, self.y = x, y

import sys
pn = PunktNormal(1,2)
ps = PunktSlots(1,2)
print(f"Normal:  {sys.getsizeof(pn.__dict__)} Bytes (dict)")
print(f"Slots:   kein __dict__, kompakter")
print(f"ps.x={ps.x}, ps.y={ps.y}")
# LOESUNG: __slots__ verhindert __dict__ -> weniger Speicher bei vielen Instanzen.

# AUFGABE 7: Deskriptoren
print("\nAUFGABE 7: Deskriptoren")
class Positiv:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None: return self
        return getattr(obj, f"_{self.name}", 0)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.name} muss >= 0 sein, war {value}")
        setattr(obj, f"_{self.name}", value)

class Rechteck:
    breite = Positiv()
    hoehe  = Positiv()

    def __init__(self, b, h): self.breite=b; self.hoehe=h

    @property
    def flaeche(self): return self.breite * self.hoehe

r = Rechteck(5, 3)
print(f"Flaeche: {r.flaeche}")
try: r.breite = -1
except ValueError as e: print(f"Fehler: {e}")
# LOESUNG: Deskriptoren (get/set/set_name) fuer wiederverwendbare Validierungslogik.

# AUFGABE 8: __getattr__ und __setattr__
print("\nAUFGABE 8: Attributzugriff kontrollieren")
class Konfiguration:
    _erlaubt = {"debug","loglevel","timeout","max_retries"}

    def __setattr__(self, name, wert):
        if not name.startswith("_") and name not in self._erlaubt:
            raise AttributeError(f"'{name}' ist kein gueltiger Config-Schluessel")
        super().__setattr__(name, wert)

    def __getattr__(self, name):
        return f"<nicht gesetzt: {name}>"

cfg = Konfiguration()
cfg.debug = True; cfg.loglevel = "INFO"
print(f"debug={cfg.debug}, loglevel={cfg.loglevel}")
print(f"timeout={cfg.timeout}")
try: cfg.passwort = "geheim"
except AttributeError as e: print(f"Fehler: {e}")
# LOESUNG: __setattr__/__getattr__ kontrollieren Lese-/Schreibzugriff auf Attribute.

# AUFGABE 9: Singleton-Pattern
print("\nAUFGABE 9: Singleton")
class Singleton:
    _instanz = None

    def __new__(cls, *args, **kwargs):
        if cls._instanz is None:
            cls._instanz = super().__new__(cls)
        return cls._instanz

    def __init__(self, name=""):
        if not hasattr(self,"_init"):
            self.name  = name
            self._init = True

s1 = Singleton("Erste")
s2 = Singleton("Zweite")
print(f"s1 is s2: {s1 is s2}")
print(f"s1.name: {s1.name}, s2.name: {s2.name}")
# LOESUNG: __new__ kontrolliert Objekterzeugung. Singleton = nur eine Instanz moeglich.

# AUFGABE 10: Vollstaendige OOP-Anwendung
print("\nAUFGABE 10: Warenkorb")
@dataclass
class ArtikelPos:
    artikel: str
    preis:   float
    menge:   int = 1

    @property
    def gesamt(self): return self.preis * self.menge

@dataclass
class Warenkorb:
    kunde:     str
    positionen: list = field(default_factory=list)

    def hinzufuegen(self, artikel, preis, menge=1):
        self.positionen.append(ArtikelPos(artikel, preis, menge))

    @property
    def summe(self): return sum(p.gesamt for p in self.positionen)

    def rabatt(self, prozent):
        return self.summe * (1 - prozent/100)

    def __str__(self):
        zeilen = [f"  {p.menge}x {p.artikel:<15} {p.gesamt:>7.2f} EUR" for p in self.positionen]
        return "\n".join([f"Warenkorb: {self.kunde}"] + zeilen +
                         [f"  {'Gesamt':<17} {self.summe:>7.2f} EUR"])

wk = Warenkorb("Max Mustermann")
wk.hinzufuegen("Python-Buch", 39.99)
wk.hinzufuegen("USB-Hub", 24.99, 2)
wk.hinzufuegen("Maus", 14.99)
print(wk)
print(f"  Mit 10% Rabatt: {wk.rabatt(10):.2f} EUR")
# LOESUNG: Dataclasses + Properties + Komposition fuer eleganten Code.

print("\n" + "=" * 60)
print("Tag 3 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
