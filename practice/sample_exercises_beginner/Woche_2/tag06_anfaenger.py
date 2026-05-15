# tag06_anfaenger.py
# Lerntag 6 - NumPy: Grundlagen (Anfaenger)
# Thema: NumPy Arrays, Operationen, Statistik
# Ausfuehren in Spyder: F5

import numpy as np

print("=" * 60)
print("LERNTAG 6 - NumPy fuer Anfaenger")
print("=" * 60)

# AUFGABE 1: Array erstellen
print("\nAUFGABE 1: Arrays erstellen")
a = np.array([10, 20, 30, 40, 50])
print("1D-Array:", a)
print("Typ:", a.dtype, "| Shape:", a.shape)
# LOESUNG: np.array([...]) wandelt eine Python-Liste in ein NumPy-Array um.

# AUFGABE 2: arange und linspace
print("\nAUFGABE 2: arange und linspace")
r = np.arange(0, 10, 2)
l = np.linspace(0, 1, 6)
print("arange(0,10,2):", r)
print("linspace(0,1,6):", l)
# LOESUNG: arange(start,stop,step) | linspace(start,stop,anzahl)

# AUFGABE 3: 2D-Array (Matrix)
print("\nAUFGABE 3: 2D-Array")
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Matrix:\n", m)
print("Shape:", m.shape, "| Element [1,2]:", m[1,2])
# LOESUNG: m[Zeile, Spalte] - Indizierung beginnt bei 0.

# AUFGABE 4: Slicing
print("\nAUFGABE 4: Slicing")
a = np.arange(10)
print("Array:", a)
print("a[2:6]:", a[2:6])
print("a[::2]:", a[::2])
print("a[-3:]:", a[-3:])
# LOESUNG: [start:stop:step] - negativ zaehlt vom Ende.

# AUFGABE 5: Vektorisierte Operationen
print("\nAUFGABE 5: Vektorisierte Operationen")
a = np.array([1.0, 2.0, 3.0, 4.0])
print("a * 2:", a * 2)
print("a ** 2:", a ** 2)
print("sqrt(a):", np.sqrt(a).round(3))
# LOESUNG: Operationen wirken elementweise - kein for-loop noetig!

# AUFGABE 6: Boolean-Indexing
print("\nAUFGABE 6: Boolean-Indexing")
noten = np.array([2.0, 1.5, 3.0, 1.0, 4.0, 2.5])
gute = noten[noten <= 2.0]
print("Alle Noten:", noten)
print("Noten <= 2.0:", gute)
# LOESUNG: Array[Bedingung] gibt alle Elemente zurueck, wo Bedingung True ist.

# AUFGABE 7: Statistische Grundfunktionen
print("\nAUFGABE 7: Statistik")
d = np.array([23,45,12,67,34,89,56,11,78,42])
print(f"Min: {d.min()}  Max: {d.max()}")
print(f"Mittelwert: {d.mean():.1f}  Median: {np.median(d):.1f}")
print(f"Std-Abw.: {d.std():.2f}")
# LOESUNG: .min()/.max()/.mean()/.std() sind Methoden des ndarray.

# AUFGABE 8: reshape
print("\nAUFGABE 8: reshape")
a = np.arange(12)
m = a.reshape(3, 4)
print("Original:", a)
print("Reshaped (3x4):\n", m)
# LOESUNG: reshape(zeilen, spalten) - Gesamtanzahl muss gleich bleiben.

# AUFGABE 9: Zufallszahlen
print("\nAUFGABE 9: Zufallszahlen")
np.random.seed(42)
wuerfe = np.random.randint(1, 7, size=20)
print("20 Wuerfelwuerfe:", wuerfe)
hfq = {i: int(np.sum(wuerfe == i)) for i in range(1, 7)}
print("Haeufigkeit:", hfq)
# LOESUNG: seed() macht Ergebnisse reproduzierbar. randint(low, high) exkl. high.

# AUFGABE 10: np.where - bedingte Auswahl
print("\nAUFGABE 10: np.where")
temp = np.array([15, 22, 8, 31, 18, 5, 27])
kat  = np.where(temp >= 20, "warm", "kalt")
print("Temperaturen:", temp)
print("Kategorien: ", kat)
# LOESUNG: np.where(bedingung, wert_true, wert_false)

print("\n" + "=" * 60)
print("Tag 6 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
