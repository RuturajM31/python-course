# woche1_mini2_anfaenger_notenrechner.py
# MINIPROJEKT WOCHE 1 - Anfaenger (2/2)
# Titel: Schulnotenrechner mit Visualisierung
# Thema: Listen, Dicts, Klassen, Kontrollstrukturen, Matplotlib (Lerntage 1-5)
# Ausfuehren in Spyder: F5

import matplotlib.pyplot as plt
import numpy as np

print("=" * 60)
print("MINIPROJEKT W1/2 (Anfaenger): Schulnotenrechner")
print("=" * 60)

# --- Klasse fuer einen Schueler ---
class Schueler:
    NOTENNAMEN = {1:"Sehr gut",2:"Gut",3:"Befriedigend",
                  4:"Ausreichend",5:"Mangelhaft",6:"Ungenuegend"}

    def __init__(self, name, klasse):
        self.name   = name
        self.klasse = klasse
        self.faecher = {}   # fach -> [(note, gewicht), ...]

    def note_eintragen(self, fach, note, gewicht=1.0):
        if not (1 <= note <= 6):
            raise ValueError(f"Note muss 1-6 sein, war: {note}")
        if fach not in self.faecher:
            self.faecher[fach] = []
        self.faecher[fach].append((note, gewicht))

    def schnitt_fach(self, fach):
        if fach not in self.faecher or not self.faecher[fach]: return None
        noten   = self.faecher[fach]
        gesamt  = sum(n*g for n,g in noten)
        gewichte= sum(g for _,g in noten)
        return round(gesamt / gewichte, 2)

    def schnitt_gesamt(self):
        schnitte = [self.schnitt_fach(f) for f in self.faecher]
        schnitte = [s for s in schnitte if s is not None]
        return round(sum(schnitte)/len(schnitte), 2) if schnitte else None

    def versetzt(self):
        gesamt = self.schnitt_gesamt()
        if gesamt is None: return False
        schlechte = sum(1 for f in self.faecher if (self.schnitt_fach(f) or 0) >= 5)
        return gesamt < 4.0 and schlechte <= 1

    def zeugnis(self):
        print(f"\n{'='*50}")
        print(f" ZEUGNIS: {self.name}  |  Klasse {self.klasse}")
        print(f"{'='*50}")
        for fach, noten in sorted(self.faecher.items()):
            schnitt = self.schnitt_fach(fach)
            name    = self.NOTENNAMEN.get(round(schnitt),"-")
            einzel  = [str(n) for n,_ in noten]
            print(f"  {fach:<15} {schnitt:.1f}  ({name:<15}) Noten: {', '.join(einzel)}")
        print(f"{'─'*50}")
        gesamt = self.schnitt_gesamt()
        print(f"  {'GESAMTSCHNITT':<15} {gesamt:.2f}")
        status = "✓ VERSETZT" if self.versetzt() else "✗ NICHT VERSETZT"
        print(f"  Status: {status}")

# --- Klasse fuer die Schulklasse ---
class Schulklasse:
    def __init__(self, bezeichnung):
        self.bezeichnung = bezeichnung
        self.schueler    = []

    def hinzufuegen(self, s): self.schueler.append(s)

    def klassenschnitt(self, fach=None):
        if fach:
            werte = [s.schnitt_fach(fach) for s in self.schueler]
        else:
            werte = [s.schnitt_gesamt() for s in self.schueler]
        werte = [v for v in werte if v is not None]
        return round(sum(werte)/len(werte),2) if werte else None

    def rangliste(self):
        return sorted(self.schueler,
            key=lambda s: s.schnitt_gesamt() or 9.9)

    def notenverteilung(self, fach=None):
    	# Alle Einzelnoten sammeln
        alle = []
        for s in self.schueler:
            if fach:
                if fach in s.faecher:
                    alle += [n for n,_ in s.faecher[fach]]
            else:
                for noten in s.faecher.values():
                    alle += [n for n,_ in noten]
        return alle

# --- Beispieldaten generieren ---
print("\n1) Erstelle Beispielklasse 10b...")
np.random.seed(42)
FAECHER = ["Mathematik","Deutsch","Englisch","Physik","Geschichte"]
klasse  = Schulklasse("10b")

namen   = ["Anna","Ben","Cara","Dave","Eva","Felix","Greta","Hans",
           "Iris","Jan","Kira","Leo","Mia","Nils","Ola"]
for name in namen:
    s = Schueler(name, "10b")
    for fach in FAECHER:
        # 3-5 Noten pro Fach, leicht normalverteilt
        n_noten = np.random.randint(3,6)
        for _ in range(n_noten):
            note = int(np.clip(np.round(np.random.normal(3.0,1.2)),1,6))
            s.note_eintragen(fach, note)
    klasse.hinzufuegen(s)

# --- Zeugnis fuer ersten Schueler ---
klasse.schueler[0].zeugnis()

# --- Klassenstatistik ---
print(f"\n2) Klassenstatistik {klasse.bezeichnung}:")
print(f"   Gesamtschnitt: {klasse.klassenschnitt():.2f}")
versetzt = sum(1 for s in klasse.schueler if s.versetzt())
print(f"   Versetzt: {versetzt}/{len(klasse.schueler)}")
print(f"\n   {'Rang':<5} {'Name':<10} {'Schnitt':>8}")
for rang, s in enumerate(klasse.rangliste(),1):
    print(f"   {rang:<5} {s.name:<10} {s.schnitt_gesamt():>8.2f}")

# --- Visualisierung ---
print("\n3) Erstelle Diagramme...")
fig, axes = plt.subplots(1, 3, figsize=(14,5))
fig.suptitle(f"Notenauswertung Klasse {klasse.bezeichnung}", fontsize=13, fontweight="bold")

# Plot 1: Klassenscnitte je Fach
fach_schnitte = {f: klasse.klassenschnitt(f) for f in FAECHER}
farben = ["seagreen" if v<3 else "steelblue" if v<4 else "tomato"
          for v in fach_schnitte.values()]
axes[0].barh(list(fach_schnitte.keys()), list(fach_schnitte.values()),
             color=farben, edgecolor="white")
axes[0].axvline(4.0, color="red", lw=1.5, linestyle="--", alpha=0.6)
axes[0].set_xlim(1,6); axes[0].set_title("Ø Klassenschnitt je Fach")
axes[0].set_xlabel("Note (1=beste)"); axes[0].grid(axis="x", alpha=0.3)

# Plot 2: Notenverteilung gesamt (Histogramm)
alle_noten = klasse.notenverteilung()
axes[1].hist(alle_noten, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5],
             color="steelblue", edgecolor="white", rwidth=0.8)
axes[1].set_xticks([1,2,3,4,5,6])
axes[1].set_xticklabels(["1\nSehr gut","2\nGut","3\nBefr.","4\nAusrch.","5\nMang.","6\nUngn."])
axes[1].set_title("Notenverteilung gesamt")
axes[1].set_ylabel("Anzahl"); axes[1].grid(axis="y", alpha=0.3)

# Plot 3: Gesamtschnitt je Schueler
schnitte = [(s.name, s.schnitt_gesamt()) for s in klasse.rangliste()]
namen_s  = [x[0] for x in schnitte]
werte_s  = [x[1] for x in schnitte]
farben_s = ["seagreen" if v<3 else "steelblue" if v<4 else "tomato" for v in werte_s]
axes[2].barh(namen_s, werte_s, color=farben_s, edgecolor="white")
axes[2].axvline(4.0, color="red", lw=1.5, linestyle="--", alpha=0.6)
axes[2].set_xlim(1,6); axes[2].set_title("Gesamtschnitt je Schueler")
axes[2].set_xlabel("Note"); axes[2].grid(axis="x", alpha=0.3)

plt.tight_layout()
plt.savefig("notenrechner_auswertung.png", dpi=120)
plt.show()
plt.close("all")

import csv
with open("klassennotenrechner.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Name"]+FAECHER+["Gesamtschnitt","Versetzt"])
    for s in klasse.rangliste():
        w.writerow([s.name]+[s.schnitt_fach(f) for f in FAECHER]+
                   [s.schnitt_gesamt(), "Ja" if s.versetzt() else "Nein"])
print("\nGespeichert: notenrechner_auswertung.png, klassennotenrechner.csv")
print("\n" + "=" * 60)
print("Miniprojekt W1/2 abgeschlossen!")
print("=" * 60)
