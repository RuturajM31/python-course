# tag08_anfaenger.py
# Lerntag 8 - Matplotlib: Grundlagen (Anfaenger)
# Thema: Linien-, Balken-, Histogramm-, Scatter-, Tortendiagramm, Subplots
# Ausfuehren in Spyder: F5 | Plots erscheinen im Plots-Panel

import matplotlib.pyplot as plt
import numpy as np

print("=" * 60)
print("LERNTAG 8 - Matplotlib fuer Anfaenger")
print("=" * 60)

# AUFGABE 1: Linienplot y = x^2
print("\nAUFGABE 1: Linienplot")
x = np.linspace(0, 10, 100)
plt.figure(); plt.plot(x, x**2, color="steelblue")
plt.title("y = x^2"); plt.xlabel("x"); plt.ylabel("y"); plt.grid(True)
plt.tight_layout(); plt.savefig("plot_08_01.png", dpi=100); plt.show()
# LOESUNG: plt.figure() -> plot() -> title/xlabel/ylabel -> grid -> show/savefig.

# AUFGABE 2: Linienfarbe, Stil, Marker
print("\nAUFGABE 2: Stil und Marker")
x = np.linspace(0, 2*np.pi, 50)
plt.figure()
plt.plot(x, np.sin(x), color="red", linestyle="--", marker="o", markersize=4, label="sin(x)")
plt.title("Sinus mit Stil"); plt.legend(); plt.grid(True)
plt.tight_layout(); plt.savefig("plot_08_02.png", dpi=100); plt.show()
# LOESUNG: color, linestyle, marker, label -> legend() anzeigen.

# AUFGABE 3: Mehrere Linien
print("\nAUFGABE 3: Mehrere Linien")
x = np.linspace(0, 2*np.pi, 100)
plt.figure()
plt.plot(x, np.sin(x), label="sin(x)", color="blue")
plt.plot(x, np.cos(x), label="cos(x)", color="orange")
plt.title("sin und cos"); plt.legend(); plt.grid(True)
plt.tight_layout(); plt.savefig("plot_08_03.png", dpi=100); plt.show()
# LOESUNG: Mehrere plt.plot() vor plt.show() zeichnen in dieselbe Grafik.

# AUFGABE 4: Balkendiagramm
print("\nAUFGABE 4: Balkendiagramm")
monate = ["Jan","Feb","Mrz","Apr","Mai","Jun"]
umsatz = [45000,52000,48000,61000,58000,70000]
plt.figure(); plt.bar(monate, umsatz, color="steelblue", edgecolor="white")
plt.title("Monatsumsatz H1"); plt.ylabel("EUR")
plt.tight_layout(); plt.savefig("plot_08_04.png", dpi=100); plt.show()
# LOESUNG: plt.bar(kategorien, werte).

# AUFGABE 5: Histogramm
print("\nAUFGABE 5: Histogramm")
np.random.seed(42)
daten = np.random.normal(170, 10, 500)
plt.figure(); plt.hist(daten, bins=20, color="mediumseagreen", edgecolor="white")
plt.title("Koerpergroesse (n=500)"); plt.xlabel("cm"); plt.ylabel("Haeufigkeit")
plt.tight_layout(); plt.savefig("plot_08_05.png", dpi=100); plt.show()
# LOESUNG: bins=n steuert Aufloesung.

# AUFGABE 6: Streudiagramm
print("\nAUFGABE 6: Streudiagramm")
np.random.seed(0)
gr = np.random.normal(170,10,80); gw = 0.5*gr-15+np.random.normal(0,5,80)
plt.figure(); plt.scatter(gr, gw, alpha=0.6, color="tomato")
plt.title("Groesse vs. Gewicht"); plt.xlabel("cm"); plt.ylabel("kg")
plt.tight_layout(); plt.savefig("plot_08_06.png", dpi=100); plt.show()
# LOESUNG: plt.scatter(x, y, alpha=Transparenz).

# AUFGABE 7: Tortendiagramm
print("\nAUFGABE 7: Tortendiagramm")
plt.figure()
plt.pie([40,30,20,10], labels=["A","B","C","Sonst."], autopct="%1.1f%%", startangle=90)
plt.title("Marktanteile"); plt.tight_layout()
plt.savefig("plot_08_07.png", dpi=100); plt.show()
# LOESUNG: autopct formatiert Prozente. startangle=90 beginnt oben.

# AUFGABE 8: Subplots
print("\nAUFGABE 8: Subplots 1x2")
x = np.linspace(0, 2*np.pi, 100)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,4))
ax1.plot(x, np.sin(x)); ax1.set_title("sin(x)"); ax1.grid(True)
ax2.plot(x, np.cos(x), color="orange"); ax2.set_title("cos(x)"); ax2.grid(True)
plt.suptitle("Trigonometrie"); plt.tight_layout()
plt.savefig("plot_08_08.png", dpi=100); plt.show()
# LOESUNG: plt.subplots(rows, cols) gibt fig + Axes zurueck.

# AUFGABE 9: Annotationen
print("\nAUFGABE 9: Annotationen")
x = np.linspace(0, 5, 100)
plt.figure(); plt.plot(x, np.exp(-x), color="purple")
plt.annotate("Start (0,1)", xy=(0,1), xytext=(1.5,0.8),
             arrowprops=dict(arrowstyle="->"))
plt.title("Exponentialabfall"); plt.grid(True)
plt.tight_layout(); plt.savefig("plot_08_09.png", dpi=100); plt.show()
# LOESUNG: annotate(text, xy=Ziel, xytext=Textpos, arrowprops=...).

# AUFGABE 10: Speichern PNG + SVG
print("\nAUFGABE 10: Speichern")
fig, ax = plt.subplots(); ax.bar(range(5), [3,7,2,8,5]); ax.set_title("Beispiel")
fig.tight_layout(); fig.savefig("plot_08_10.png", dpi=150); fig.savefig("plot_08_10.svg")
print("Gespeichert als PNG und SVG.")
plt.close("all")

print("\n" + "=" * 60)
print("Tag 8 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
