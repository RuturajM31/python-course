# woche1_mini3_fortgeschrittene_oop_bank.py
# MINIPROJEKT WOCHE 1 - Fortgeschrittene (1/2)
# Titel: Banksystem mit OOP, Vererbung, Dekoratoren und Analyse
# Thema: OOP, Vererbung, Dataclasses, Closures, Matplotlib (Lerntage 1-5)
# Ausfuehren in Spyder: F5

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
import functools
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

print("=" * 60)
print("MINIPROJEKT W1/3 (Fortgeschrittene): OOP-Banksystem")
print("=" * 60)

# --- Transaktion als Dataclass ---
@dataclass
class Transaktion:
    typ:       str           # "Einzahlung","Abhebung","Ueberweisung","Zinsen"
    betrag:    float
    datum:     datetime = field(default_factory=datetime.now)
    empfaenger:str = ""
    notiz:     str = ""

    def __str__(self):
        richtung = "+" if self.typ in ("Einzahlung","Zinsen","Ueberweisung_ein") else "-"
        return (f"[{self.datum.strftime('%d.%m.%Y')}] "
                f"{self.typ:<18} {richtung}{self.betrag:>9.2f} EUR"
                + (f"  -> {self.empfaenger}" if self.empfaenger else "")
                + (f"  ({self.notiz})" if self.notiz else ""))


# --- Logging-Dekorator ---
def transaktions_log(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        vorher = self.kontostand
        result = func(self, *args, **kwargs)
        nachher = self.kontostand
        if vorher != nachher:
            print(f"   ✓ {func.__name__}: {vorher:.2f} -> {nachher:.2f} EUR")
        return result
    return wrapper


# --- Abstrakte Basisklasse ---
class Konto(ABC):
    _naechste_id = 1000

    def __init__(self, inhaber: str, einlage: float = 0.0):
        Konto._naechste_id += 1
        self.kontonummer  = str(Konto._naechste_id)
        self.inhaber      = inhaber
        self._stand       = 0.0
        self.transaktionen= []
        self.erstellt      = datetime.now()
        if einlage > 0:
            self._einzahlen_intern(einlage, "Eroefffnungseinlage")

    def _einzahlen_intern(self, betrag, notiz=""):
        self._stand += betrag
        self.transaktionen.append(Transaktion("Einzahlung", betrag,
                                               notiz=notiz))

    @property
    def kontostand(self): return self._stand

    @transaktions_log
    def einzahlen(self, betrag: float, notiz=""):
        if betrag <= 0: raise ValueError("Betrag muss positiv sein.")
        self._stand += betrag
        self.transaktionen.append(Transaktion("Einzahlung", betrag, notiz=notiz))

    @abstractmethod
    def abheben(self, betrag: float) -> bool: pass

    @abstractmethod
    def jaehrliche_verarbeitung(self): pass

    def kontoauszug(self, letzte_n=None):
        print(f"\n--- Kontoauszug: {self.inhaber} (Nr. {self.kontonummer}) ---")
        t_liste = self.transaktionen[-letzte_n:] if letzte_n else self.transaktionen
        for t in t_liste:
            print(f"  {t}")
        print(f"  {'─'*55}")
        print(f"  Aktueller Stand: {self._stand:.2f} EUR")

    def verlauf_als_serie(self):
        """Gibt (datum, kumulierter_stand) als Listen zurueck."""
        stand = 0.0
        daten, staende = [], []
        for t in self.transaktionen:
            if t.typ in ("Einzahlung","Zinsen","Ueberweisung_ein"):
                stand += t.betrag
            else:
                stand -= t.betrag
            daten.append(t.datum)
            staende.append(round(stand, 2))
        return daten, staende


# --- Girokonto ---
class Girokonto(Konto):
    def __init__(self, inhaber, einlage=0, dispo=1000):
        self.dispo = dispo
        super().__init__(inhaber, einlage)

    @transaktions_log
    def abheben(self, betrag, notiz=""):
        if betrag <= 0: raise ValueError("Betrag muss positiv sein.")
        if self._stand - betrag < -self.dispo:
            print(f"   ✗ Dispo ({self.dispo} EUR) ueberschritten!")
            return False
        self._stand -= betrag
        self.transaktionen.append(Transaktion("Abhebung", betrag, notiz=notiz))
        return True

    def jaehrliche_verarbeitung(self):
        if self._stand < 0:
            zinsen = abs(self._stand) * 0.12
            self._stand -= zinsen
            self.transaktionen.append(Transaktion("Dispozinsen", zinsen,
                                                   notiz="12% p.a."))

    @transaktions_log
    def ueberweisen(self, betrag, zielkonto, verwendung=""):
        if self._stand - betrag < -self.dispo:
            print(f"   ✗ Ueberweisung abgelehnt (Dispo).")
            return False
        self._stand -= betrag
        self.transaktionen.append(Transaktion("Ueberweisung",betrag,
            empfaenger=zielkonto.inhaber, notiz=verwendung))
        zielkonto._stand += betrag
        zielkonto.transaktionen.append(Transaktion("Ueberweisung_ein",betrag,
            empfaenger=self.inhaber, notiz=verwendung))
        return True


# --- Sparkonto ---
class Sparkonto(Konto):
    def __init__(self, inhaber, einlage=0, zinssatz=0.025):
        self.zinssatz   = zinssatz
        self.abhebungen = 0
        super().__init__(inhaber, einlage)

    @transaktions_log
    def abheben(self, betrag):
        if self.abhebungen >= 2:
            print("   ✗ Max. 2 kostenlose Abhebungen/Monat erreicht.")
            return False
        if betrag > self._stand:
            print("   ✗ Nicht genug Guthaben.")
            return False
        self._stand -= betrag
        self.abhebungen += 1
        self.transaktionen.append(Transaktion("Abhebung", betrag))
        return True

    def jaehrliche_verarbeitung(self):
        zinsen = self._stand * self.zinssatz
        self._stand += zinsen
        self.transaktionen.append(Transaktion("Zinsen", round(zinsen,2),
                                               notiz=f"{self.zinssatz*100:.1f}% p.a."))
        self.abhebungen = 0
        print(f"   Zinsgutschrift: {zinsen:.2f} EUR (Stand: {self._stand:.2f} EUR)")


# --- Simulation ---
random.seed(42)
print("\n1) Konto eroeffnen und Transaktionen...")

giro  = Girokonto("Anna Meier",  einlage=2500, dispo=1500)
spar  = Sparkonto("Anna Meier",  einlage=5000, zinssatz=0.030)
giro2 = Girokonto("Bob Mueller", einlage=1200)

# Simuliere 12 Monate
basis_datum = datetime(2024, 1, 1)
for monat in range(12):
    datum_offset = basis_datum + timedelta(days=monat*30)
    # Gehalt
    betrag = 2800 + random.gauss(0,100)
    t = Transaktion("Einzahlung", round(betrag,2), datum=datum_offset, notiz="Gehalt")
    giro._stand += round(betrag,2)
    giro.transaktionen.append(t)
    # Miete
    t2 = Transaktion("Abhebung", 950, datum=datum_offset+timedelta(days=2), notiz="Miete")
    giro._stand -= 950
    giro.transaktionen.append(t2)
    # Zufaellige Ausgaben
    for _ in range(random.randint(3,8)):
        betrag_a = round(random.uniform(10,300),2)
        if giro._stand - betrag_a > -giro.dispo:
            t3 = Transaktion("Abhebung", betrag_a,
                             datum=datum_offset+timedelta(days=random.randint(1,28)))
            giro._stand -= betrag_a
            giro.transaktionen.append(t3)
    # Sparen
    if monat % 3 == 0:
        spar.einzahlen(300, "Monatliche Sparrate")

print(f"   Giro-Stand nach Simulation: {giro.kontostand:.2f} EUR")
print(f"   Spar-Stand nach Simulation: {spar.kontostand:.2f} EUR")

print("\n2) Jaehrliche Verarbeitung...")
spar.jaehrliche_verarbeitung()

print("\n3) Ueberweisung:")
giro.ueberweisen(200, giro2, "Schulden zurueck")

giro.kontoauszug(letzte_n=8)

# --- Visualisierung ---
print("\n4) Erstelle Dashboard...")
fig, axes = plt.subplots(1,2,figsize=(13,5))
fig.suptitle("Konto-Dashboard: Anna Meier", fontsize=13, fontweight="bold")

for ax, konto, farbe, titel in [
    (axes[0], giro, "steelblue", "Girokonto"),
    (axes[1], spar, "seagreen",  "Sparkonto"),
]:
    daten, staende = konto.verlauf_als_serie()
    ax.plot(daten, staende, lw=2, color=farbe)
    ax.fill_between(daten, 0, staende, alpha=0.12, color=farbe)
    ax.axhline(0, color="black", lw=0.8, linestyle="--")
    if hasattr(konto,"dispo"):
        ax.axhline(-konto.dispo, color="red", lw=1, linestyle=":", alpha=0.7,
                   label=f"Dispo-Limit (-{konto.dispo} EUR)")
        ax.legend(fontsize=8)
    ax.set_title(f"{titel}: {konto.inhaber}")
    ax.set_ylabel("Kontostand (EUR)")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, ha="right")
    ax.grid(alpha=0.3)
    ax.text(0.02, 0.97, f"Aktuell: {konto.kontostand:.2f} EUR",
            transform=ax.transAxes, fontsize=10, verticalalignment="top",
            bbox=dict(boxstyle="round", facecolor=farbe, alpha=0.15))

plt.tight_layout()
plt.savefig("banksystem_dashboard.png", dpi=120)
plt.show()
plt.close("all")

print("\nGespeichert: banksystem_dashboard.png")
print("\n" + "=" * 60)
print("Miniprojekt W1/3 abgeschlossen!")
print("=" * 60)
