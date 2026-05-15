# tag06_fortgeschrittene.py
# Lerntag 6 - NumPy: Fortgeschrittene Techniken
# Thema: Broadcasting, Lineare Algebra, Vektorisierung
# Ausfuehren in Spyder: F5

import numpy as np
import time

print("=" * 60)
print("LERNTAG 6 - NumPy fuer Fortgeschrittene")
print("=" * 60)

# AUFGABE 1: Broadcasting
print("\nAUFGABE 1: Broadcasting")
M = np.array([[1,2,3],[4,5,6],[7,8,9]])
v = np.array([10, 20, 30])
print("Matrix + [10,20,30]:\n", M + v)
# LOESUNG: NumPy dehnt kleinere Arrays automatisch aus (broadcastet).

# AUFGABE 2: Matrixmultiplikation
print("\nAUFGABE 2: Matrixmultiplikation")
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print("A @ B:\n", A @ B)
print("A * B (elementweise):\n", A * B)
# LOESUNG: @ fuer echte Matrixmultiplikation, * elementweise.

# AUFGABE 3: Transponieren + Determinante + Inverse
print("\nAUFGABE 3: linalg")
M = np.array([[2.,1.],[5.,3.]])
print("M^T:\n", M.T)
print("det(M):", np.linalg.det(M).round(4))
print("inv(M):\n", np.linalg.inv(M).round(4))
# LOESUNG: .T transponiert. linalg.det/inv aus dem LA-Modul.

# AUFGABE 4: Eigenwerte und Eigenvektoren
print("\nAUFGABE 4: Eigenwerte")
M = np.array([[4.,2.],[1.,3.]])
werte, vektoren = np.linalg.eig(M)
print("Eigenwerte:", werte.round(3))
print("Eigenvektoren:\n", vektoren.round(3))
# LOESUNG: eig(M) gibt (werte, vektoren) zurueck. Wichtig fuer PCA.

# AUFGABE 5: Normalgleichung (Lineare Regression)
print("\nAUFGABE 5: Lineare Regression")
np.random.seed(0)
x = np.linspace(0, 10, 50)
y = 2.5 * x + 1.0 + np.random.randn(50) * 2
X = np.column_stack([np.ones(50), x])
beta = np.linalg.lstsq(X, y, rcond=None)[0]
print(f"Intercept={beta[0]:.3f}, Slope={beta[1]:.3f}")
# LOESUNG: lstsq loest min||Xb-y||^2 direkt.

# AUFGABE 6: Fancy Indexing + argsort
print("\nAUFGABE 6: argsort Rangliste")
punkte = np.array([78,45,92,61,88,55])
namen  = np.array(["Ali","Ben","Cara","Dan","Eva","Finn"])
rang   = np.argsort(punkte)[::-1]
for i, idx in enumerate(rang):
    print(f"  {i+1}. {namen[idx]}: {punkte[idx]} Pkt")
# LOESUNG: argsort() gibt Indizes der Sortierreihenfolge zurueck.

# AUFGABE 7: Vektorisierung - Performance-Vergleich
print("\nAUFGABE 7: Vektorisierung vs. Loop")
daten = np.random.rand(500_000)
t0 = time.time()
result_loop = np.array([x*0.1 if x<0.3 else (x*0.25 if x<0.7 else x*0.42) for x in daten])
t1 = time.time()
result_vek  = np.where(daten<0.3, daten*0.1, np.where(daten<0.7, daten*0.25, daten*0.42))
t2 = time.time()
print(f"Loop:    {t1-t0:.4f}s")
print(f"np.where:{t2-t1:.4f}s")
print(f"Identisch: {np.allclose(result_loop, result_vek)}")
# LOESUNG: np.where ist deutlich schneller als Python-Loops.

# AUFGABE 8: vstack, hstack, split
print("\nAUFGABE 8: Stacking")
a = np.array([[1,2,3]])
b = np.array([[4,5,6]])
print("vstack:\n", np.vstack([a,b]))
print("hstack:", np.hstack([a,b]))
print("split:", np.split(np.arange(9), 3))
# LOESUNG: vstack = vertikal (Zeilen), hstack = horizontal (Spalten).

# AUFGABE 9: Korrelation und Kovarianz
print("\nAUFGABE 9: Korrelation")
np.random.seed(1)
x = np.random.randn(100)
y = 0.8*x + 0.2*np.random.randn(100)
print(f"Kovarianz x,y:   {np.cov(x,y)[0,1]:.4f}")
print(f"Korrelation x,y: {np.corrcoef(x,y)[0,1]:.4f}")
# LOESUNG: cov/corrcoef geben 2x2-Matrizen - [0,1] ist der Kreuswert.

# AUFGABE 10: Speichern und Laden
print("\nAUFGABE 10: Speichern")
d = np.random.randn(5, 3).round(3)
np.save("array_gespeichert.npy", d)
geladen = np.load("array_gespeichert.npy")
print("Geladen:\n", geladen)
np.savetxt("array_gespeichert.csv", d, delimiter=",", fmt="%.3f")
print("Auch als CSV gespeichert.")
# LOESUNG: .npy binaer (schnell+genau), .csv lesbar.

print("\n" + "=" * 60)
print("Tag 6 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
