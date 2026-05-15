# tag04_anfaenger.py
# Lerntag 4 - NumPy Grundlagen (Anfaenger)
# Thema: Arrays, Operationen, Indizierung, Broadcasting, lineare Algebra
# Ausfuehren in Spyder: F5

import numpy as np

print("=" * 60)
print("LERNTAG 4 - NumPy fuer Anfaenger")
print("=" * 60)
np.random.seed(42)

# AUFGABE 1: Arrays erstellen
print("\nAUFGABE 1: Arrays erstellen")
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.arange(0, 20, 2)
a3 = np.linspace(0, 1, 6)
a4 = np.zeros((3,4))
a5 = np.ones((2,3))
a6 = np.eye(3)
print(f"array:    {a1}")
print(f"arange:   {a2}")
print(f"linspace: {a3}")
print(f"zeros:\n{a4}")
print(f"eye:\n{a6}")
# LOESUNG: np.array(), arange(), linspace(), zeros(), ones(), eye() erstellen Arrays.

# AUFGABE 2: Array-Eigenschaften
print("\nAUFGABE 2: Eigenschaften")
m = np.random.randint(1, 100, (4, 5))
print(f"Array:\n{m}")
print(f"Shape:  {m.shape}")
print(f"Ndim:   {m.ndim}")
print(f"Size:   {m.size}")
print(f"Dtype:  {m.dtype}")
# LOESUNG: .shape = Dimensionen, .ndim = Anzahl Achsen, .size = Gesamtelemente.

# AUFGABE 3: Indexing und Slicing
print("\nAUFGABE 3: Indexing")
print(f"m[0,0]={m[0,0]}, m[-1,-1]={m[-1,-1]}")
print(f"Erste Zeile:  {m[0,:]}")
print(f"Letzte Spalte:{m[:,-1]}")
print(f"Submatrix [1:3,1:4]:\n{m[1:3,1:4]}")
# LOESUNG: [zeile, spalte], : = alle. -1 = letztes Element.

# AUFGABE 4: Arithmetik und Broadcasting
print("\nAUFGABE 4: Broadcasting")
a = np.array([1,2,3,4,5])
print(f"a*2+1:  {a*2+1}")
print(f"a**2:   {a**2}")
print(f"a/a.sum(): {(a/a.sum()).round(3)}")
mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"mat + [10,20,30]:\n{mat + np.array([10,20,30])}")
# LOESUNG: Broadcasting: Skalare oder kleinere Arrays werden automatisch angepasst.

# AUFGABE 5: Aggregationsfunktionen
print("\nAUFGABE 5: Aggregation")
daten = np.random.normal(100, 15, (6, 5))
print(f"Gesamt-Mittel: {daten.mean():.2f}")
print(f"Zeilen-Mittel: {daten.mean(axis=1).round(2)}")
print(f"Spalten-Summe:{daten.sum(axis=0).round(2)}")
print(f"Min/Max:       {daten.min():.2f} / {daten.max():.2f}")
print(f"Std:           {daten.std():.2f}")
# LOESUNG: axis=0 aggregiert spaltenweise, axis=1 zeilenweise.

# AUFGABE 6: Boolean-Indexing
print("\nAUFGABE 6: Boolean-Indexing")
noten = np.array([85,72,91,68,95,77,88,63,79,92])
print(f"Noten:       {noten}")
print(f"Bestanden (>=70): {noten[noten >= 70]}")
print(f"Anzahl bestanden: {(noten>=70).sum()}")
print(f"Durchschnitt:     {noten.mean():.1f}")
noten[noten < 70] = 70   # Note auf Mindest-70 setzen
print(f"Nach Korrektur:  {noten}")
# LOESUNG: array[bedingung] filtert direkt. .sum() zaehlt True-Werte.

# AUFGABE 7: Reshape und Transpose
print("\nAUFGABE 7: Reshape")
v = np.arange(1, 13)
m34  = v.reshape(3, 4)
m43  = v.reshape(4, 3)
m_T  = m34.T
print(f"Original (12,): {v}")
print(f"Reshape (3,4):\n{m34}")
print(f"Transponiert:\n{m_T}")
# LOESUNG: .reshape() aendert Form (Anzahl Elemente gleich!). .T transponiert.

# AUFGABE 8: Stapeln und Aufteilen
print("\nAUFGABE 8: Stack und Split")
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8,9],[10,11,12]])
v_stack = np.vstack([a,b])
h_stack = np.hstack([a,b])
teile   = np.hsplit(h_stack, 2)
print(f"vstack:\n{v_stack}")
print(f"hstack:\n{h_stack}")
print(f"hsplit Teil 1:\n{teile[0]}")
# LOESUNG: vstack = senkrecht stapeln, hstack = waagerecht. split = aufteilen.

# AUFGABE 9: Lineare Algebra
print("\nAUFGABE 9: Lineare Algebra")
A = np.array([[2,1],[5,3]])
b = np.array([4, 7])
x = np.linalg.solve(A, b)
print(f"Loesung Ax=b: x={x}  (Probe: {A@x})")
eigwerte, eigvektoren = np.linalg.eig(A)
print(f"Eigenwerte: {eigwerte.round(4)}")
print(f"Det(A): {np.linalg.det(A):.0f}")
# LOESUNG: linalg.solve loest lineare Gleichungssysteme. @ = Matrizenmultiplikation.

# AUFGABE 10: Zufallszahlen und Simulation
print("\nAUFGABE 10: Monte-Carlo Pi")
n = 1_000_000
x, y = np.random.uniform(-1, 1, n), np.random.uniform(-1, 1, n)
im_kreis = x**2 + y**2 <= 1
pi_approx = 4 * im_kreis.sum() / n
print(f"Pi (MC, n={n:,}): {pi_approx:.5f}")
print(f"Echtes Pi:         {np.pi:.5f}")
print(f"Fehler:            {abs(pi_approx - np.pi):.5f}")
# LOESUNG: Verhältnis Punkte im Einheitskreis zu gesamt * 4 approximiert Pi.

print("\n" + "=" * 60)
print("Tag 4 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
