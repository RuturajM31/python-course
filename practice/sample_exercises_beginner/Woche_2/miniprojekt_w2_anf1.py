# miniprojekt_w2_anf1.py
# MINIPROJEKT 1 (Anfaenger) - Woche 2
# Titel: Mein persoenlicher Notenrechner
# Kombiniert: NumPy + Pandas + Matplotlib
# Ausfuehren in Spyder: F5
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("MINIPROJEKT 1 - Notenrechner")
print("=" * 60)

# --- 1. Daten ---
faecher = ["Mathematik","Deutsch","Englisch","Informatik","Geschichte","Sport"]
noten   = [2.0, 3.0, 1.5, 1.0, 2.5, 2.0]

# --- 2. NumPy-Auswertung ---
arr = np.array(noten)
print(f"Durchschnitt:        {arr.mean():.2f}")
print(f"Beste Note:          {arr.min():.1f}")
print(f"Schlechteste Note:   {arr.max():.1f}")
print(f"Standardabweichung:  {arr.std():.2f}")

# --- 3. Pandas DataFrame ---
df = pd.DataFrame({"Fach": faecher, "Note": noten})
df["Bewertung"] = pd.cut(df["Note"], bins=[0,1.5,2.5,4.0,6.0],
                          labels=["sehr gut","gut","befriedigend","ausreichend"])
print("\nNotentabelle:")
print(df.to_string(index=False))

# --- 4. CSV speichern ---
df.to_csv("noten_ergebnis.csv", index=False)
print("\nCSV gespeichert.")

# --- 5. Visualisierung ---
farben_map = {"sehr gut":"#2ecc71","gut":"#3498db",
              "befriedigend":"#f39c12","ausreichend":"#e74c3c"}
bar_farben = [farben_map[str(b)] for b in df["Bewertung"]]

fig, ax = plt.subplots(figsize=(8,5))
balken = ax.bar(df["Fach"], df["Note"], color=bar_farben, edgecolor="white", width=0.6)
for b in balken:
    ax.text(b.get_x()+b.get_width()/2, b.get_height()+0.05,
            str(b.get_height()), ha="center", va="bottom", fontsize=11)
ax.axhline(arr.mean(), color="navy", linestyle="--", lw=1.5,
           label=f"Durchschnitt {arr.mean():.2f}")
ax.set_title("Mein Halbjahreszeugnis", fontsize=14, fontweight="bold")
ax.set_ylabel("Note (1=beste)"); ax.set_ylim(0,6.5); ax.invert_yaxis()
ax.legend(); ax.grid(axis="y", alpha=0.3)
plt.xticks(rotation=15, ha="right"); plt.tight_layout()
plt.savefig("mp1_notenrechner.png", dpi=150); plt.show()
print("Plot gespeichert: mp1_notenrechner.png")
print(f"\nEmpfehlung: Fokus auf '{df.loc[df['Note'].idxmax(),'Fach']}'")
