# tag04_fortgeschrittene.py
# Lerntag 4 - NumPy Fortgeschrittene
# Thema: Fancy Indexing, Strides, ufuncs, Vectorisierung, FFT, Polynome
# Ausfuehren in Spyder: F5

import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("LERNTAG 4 - NumPy Fortgeschrittene")
print("=" * 60)
np.random.seed(42)

# AUFGABE 1: Fancy Indexing
print("\nAUFGABE 1: Fancy Indexing")
a = np.arange(10)**2
idx = np.array([1,3,5,7])
print(f"a = {a}")
print(f"a[[1,3,5,7]] = {a[idx]}")
# 2D Fancy Indexing
m = np.arange(16).reshape(4,4)
zeilen = np.array([0,2,3])
sp     = np.array([1,0,2])
print(f"m[zeilen, sp] = {m[zeilen, sp]}")
# np.ix_ fuer Kreuzprodukt-Selektion
print(f"m[np.ix_([0,2],[1,3])]:\n{m[np.ix_([0,2],[1,3])]}")
# LOESUNG: Integer-Arrays als Indizes = Fancy Indexing. np.ix_ erzeugt Gitter.

# AUFGABE 2: Strides und Views
print("\nAUFGABE 2: Strides")
a = np.arange(12).reshape(3,4)
b = a[1:, ::2]        # View (kein Kopie)
b[0,0] = 99
print(f"a nach b[0,0]=99:\n{a}")
c = a.copy()          # echte Kopie
c[0,0] = 0
print(f"a unveraendert nach c-Aenderung: {a[0,0]!=0}")
print(f"Strides von a: {a.strides}")
# LOESUNG: Slice erzeugt View (teilt Speicher). .copy() fuer unabhaengige Kopie.

# AUFGABE 3: Vectorized Functions (ufuncs)
print("\nAUFGABE 3: Ufuncs")
def python_norm(v):
    return sum(x**2 for x in v)**0.5

def numpy_norm(v):
    return np.sqrt(np.sum(v**2))

import time
v = np.random.randn(1_000_000)
t0 = time.perf_counter(); r1 = python_norm(v); t1 = time.perf_counter()
t2 = time.perf_counter(); r2 = numpy_norm(v);  t3 = time.perf_counter()
print(f"Python: {(t1-t0)*1000:.1f} ms  Result={r1:.6f}")
print(f"NumPy:  {(t3-t2)*1000:.1f} ms  Result={r2:.6f}")
print(f"Speedup: ~{(t1-t0)/(t3-t2):.0f}x")
# LOESUNG: NumPy-Operationen laufen in C -> viel schneller als Python-Schleifen.

# AUFGABE 4: np.where und np.select
print("\nAUFGABE 4: where / select")
noten  = np.array([45,72,88,61,95,53,79,82])
letter = np.select(
    [noten>=90, noten>=80, noten>=70, noten>=60],
    ["A",       "B",       "C",       "D"],
    default="F")
print(f"Noten:  {noten}")
print(f"Grades: {letter}")
korr = np.where(noten<60, 60, noten)
print(f"Korr:   {korr}")
# LOESUNG: np.where(cond, val_true, val_false). np.select fuer mehrere Bedingungen.

# AUFGABE 5: Polynome
print("\nAUFGABE 5: Polynome")
x = np.linspace(-3, 3, 200)
koeff = np.polyfit(x + np.random.randn(200)*0.3, x**3 - 2*x + 1 + np.random.randn(200)*0.5, 3)
print(f"Gefittete Koeffizienten: {koeff.round(3)}")
y_fit = np.polyval(koeff, x)
plt.figure(figsize=(7,4))
plt.plot(x, x**3-2*x+1, "b-", lw=2, label="Original")
plt.plot(x, y_fit, "r--", lw=2, label="Fit (Grad 3)")
plt.title("Polynomfit"); plt.legend(); plt.grid(alpha=0.3)
plt.tight_layout(); plt.savefig("plot_04f_05.png", dpi=100); plt.show()
# LOESUNG: polyfit(x,y,grad) bestimmt Koeffizienten, polyval wertet aus.

# AUFGABE 6: FFT - Frequenzanalyse
print("\nAUFGABE 6: FFT")
fs = 1000
t  = np.linspace(0, 1, fs, endpoint=False)
signal = (np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)
          + np.random.randn(fs)*0.2)
fft_vals = np.abs(np.fft.rfft(signal))
freqs    = np.fft.rfftfreq(fs, 1/fs)
haupt_freq = freqs[np.argsort(fft_vals)[-2:]]
print(f"Erkannte Hauptfrequenzen: {sorted(haupt_freq.round(0).astype(int))} Hz")
plt.figure(figsize=(9,3))
plt.plot(freqs[:200], fft_vals[:200])
plt.title("FFT-Spektrum"); plt.xlabel("Hz"); plt.ylabel("|Amplitude|")
plt.grid(alpha=0.3); plt.tight_layout()
plt.savefig("plot_04f_06.png", dpi=100); plt.show()
# LOESUNG: rfft fuer reelle Signale. rfftfreq gibt Frequenzachse. Peaks = Frequenzen.

# AUFGABE 7: Structured Arrays
print("\nAUFGABE 7: Structured Arrays")
dtype = np.dtype([("name","U20"),("alter","i4"),("gehalt","f8")])
data  = np.array([("Anna",28,3200.0),("Bob",35,4100.0),("Cara",22,2900.0)], dtype=dtype)
print(f"Namen:  {data['name']}")
print(f"Alter:  {data['alter']}")
reich = data[data["gehalt"] > 3000]
print(f"Gehalt>3000: {reich['name']}")
# LOESUNG: Structured arrays mit dtype kombinieren verschiedene Typen pro Element.

# AUFGABE 8: Broadcasting fortgeschritten
print("\nAUFGABE 8: Broadcasting Distanzmatrix")
punkte = np.random.rand(5, 2)
diff   = punkte[:, np.newaxis, :] - punkte[np.newaxis, :, :]
dists  = np.sqrt((diff**2).sum(axis=2))
np.fill_diagonal(dists, np.inf)
naechste = np.argmin(dists, axis=1)
print("Naechster Nachbar je Punkt:")
for i, j in enumerate(naechste):
    print(f"  Punkt {i} -> Punkt {j}  (Abstand {dists[i,j]:.3f})")
# LOESUNG: [:, newaxis, :] und [newaxis, :, :] = Broadcasting fuer Paarvergleiche.

# AUFGABE 9: Eigenwerte und SVD
print("\nAUFGABE 9: SVD")
np.random.seed(1)
A = np.random.randn(4, 3)
U, S, Vt = np.linalg.svd(A, full_matrices=False)
print(f"Singulaerwerte: {S.round(3)}")
A_rekonstruiert = U @ np.diag(S) @ Vt
print(f"Rekonstruktionsfehler: {np.max(np.abs(A - A_rekonstruiert)):.2e}")
A_komp = U[:,:2] @ np.diag(S[:2]) @ Vt[:2,:]
print(f"Mit 2 Komponenten:     {np.max(np.abs(A - A_komp)):.4f}")
# LOESUNG: SVD = Zerlegung in U, Σ, Vt. Dimensionsreduktion durch wenige Singulaerwerte.

# AUFGABE 10: Custom ufunc
print("\nAUFGABE 10: Custom ufunc + Vectorize")
def clamped_sigmoid(x, lo=-5, hi=5):
    x = np.clip(x, lo, hi)
    return 1 / (1 + np.exp(-x))

sig_vec = np.vectorize(clamped_sigmoid)
x = np.linspace(-8, 8, 300)
y = clamped_sigmoid(x)
plt.figure(figsize=(7,3))
plt.plot(x, y, "steelblue", lw=2)
plt.title("Clamped Sigmoid [-5,5]"); plt.grid(alpha=0.3)
plt.tight_layout(); plt.savefig("plot_04f_10.png", dpi=100); plt.show()
plt.close("all")
print(f"sigmoid(0)={clamped_sigmoid(0):.4f}, sigmoid(10)={clamped_sigmoid(10):.4f}")
# LOESUNG: np.vectorize + Funktionen auf Array anwenden. np.clip begrenzt Wertebereich.

print("\n" + "=" * 60)
print("Tag 4 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
