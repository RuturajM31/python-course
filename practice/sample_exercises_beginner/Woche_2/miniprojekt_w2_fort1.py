# miniprojekt_w2_fort1.py
# MINIPROJEKT 3 (Fortgeschrittene) - Woche 2
# Titel: Aktienanalyse-Dashboard
# Kombiniert: NumPy + Pandas + Matplotlib (Moving Average, Bollinger, Volatilitaet)
# Ausfuehren in Spyder: F5
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(2024)
n = 252
datum = pd.date_range("2024-01-01", periods=n, freq="B")

print("=" * 60)
print("MINIPROJEKT 3 - Aktien-Dashboard")
print("=" * 60)

# Geometrische Brownsche Bewegung
renditen = np.random.normal(0.0005, 0.018, n)
kurs = 100 * np.exp(np.cumsum(renditen))
df = pd.DataFrame({"Kurs": kurs.round(2)}, index=datum)

# Technische Indikatoren
df["MA20"]     = df["Kurs"].rolling(20).mean().round(2)
df["MA50"]     = df["Kurs"].rolling(50).mean().round(2)
df["Rendite"]  = df["Kurs"].pct_change() * 100
df["Vol20"]    = df["Rendite"].rolling(20).std().round(4)
df["BB_oben"]  = df["MA20"] + 2*df["Kurs"].rolling(20).std()
df["BB_unten"] = df["MA20"] - 2*df["Kurs"].rolling(20).std()

print(f"Zeitraum:       {df.index[0].date()} bis {df.index[-1].date()}")
print(f"Startkurs:      {df['Kurs'].iloc[0]:.2f}")
print(f"Endkurs:        {df['Kurs'].iloc[-1]:.2f}")
print(f"Gesamtrendite:  {((df['Kurs'].iloc[-1]/df['Kurs'].iloc[0])-1)*100:.1f}%")
print(f"Annualis. Vola: {df['Rendite'].std()*np.sqrt(252):.2f}%")
print(f"Max Drawdown:   {((df['Kurs']/df['Kurs'].cummax())-1).min()*100:.1f}%")

fig, axes = plt.subplots(3,1, figsize=(12,10), sharex=True)
fig.suptitle("Aktien-Dashboard (simuliert, 1 Jahr)", fontsize=14, fontweight="bold")

# Kurs + Bollinger + MA
axes[0].plot(df.index, df["Kurs"], "k", lw=1, label="Kurs")
axes[0].plot(df.index, df["MA20"], "b", lw=1.5, label="MA20")
axes[0].plot(df.index, df["MA50"], color="orange", lw=1.5, label="MA50")
axes[0].fill_between(df.index, df["BB_unten"], df["BB_oben"],
                      alpha=0.15, color="blue", label="Bollinger")
axes[0].set_ylabel("Kurs"); axes[0].legend(loc="upper left"); axes[0].grid(alpha=0.3)

# Renditen
farben = ["green" if r>=0 else "red" for r in df["Rendite"].fillna(0)]
axes[1].bar(df.index, df["Rendite"], color=farben, width=1, alpha=0.7)
axes[1].axhline(0, color="black", lw=0.5); axes[1].set_ylabel("Rendite %"); axes[1].grid(axis="y",alpha=0.3)

# Volatilitaet
axes[2].plot(df.index, df["Vol20"], color="purple", lw=1.2)
axes[2].fill_between(df.index, 0, df["Vol20"].fillna(0), alpha=0.2, color="purple")
axes[2].set_ylabel("Vola (20T)"); axes[2].grid(alpha=0.3); axes[2].set_xlabel("Datum")

plt.tight_layout(); plt.savefig("mp3_aktien.png", dpi=150); plt.show()
df.to_csv("aktien_analyse.csv")
print("\nDateien gespeichert: mp3_aktien.png, aktien_analyse.csv")
