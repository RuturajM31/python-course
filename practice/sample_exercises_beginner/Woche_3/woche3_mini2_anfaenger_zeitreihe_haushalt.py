# woche3_mini2_anfaenger_zeitreihe_haushalt.py
# MINIPROJEKT WOCHE 3 - Anfaenger (2/2)
# Titel: Haushaltsbuch mit Zeitreihenanalyse
# Thema: datetime + Pandas + Zeitreihe + Visualisierung (Lerntage 12-14)
# Ausfuehren in Spyder: F5

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from datetime import datetime

print("=" * 60)
print("MINIPROJEKT W3/2 (Anfaenger): Haushaltsbuch-Analyse")
print("=" * 60)
np.random.seed(42)

# --- SCHRITT 1: Simulierte Haushaltsdaten erzeugen ---
print("\n1) Erstelle Haushaltsdaten (12 Monate)...")

kategorien = {
    "Miete":       (900,  20,  1),   # (Basis, Std, Frequenz/Monat)
    "Lebensmittel":(350,  40, 12),
    "Transport":   (120,  30,  8),
    "Freizeit":    (150,  50,  6),
    "Kleidung":    (80,   60,  2),
    "Gesundheit":  (60,   40,  2),
    "Strom/Gas":   (110,  15,  1),
    "Internet":    (45,    5,  1),
}

einnahmen_basis = 2800

eintraege = []
start = datetime(2024, 1, 1)
monate = pd.date_range(start, periods=12, freq="MS")

for monat in monate:
    # Einnahmen
    gehalt = einnahmen_basis + np.random.normal(0, 100)
    bonus  = 500 if monat.month in [6, 12] else 0
    eintraege.append({
        "Datum":     monat + pd.Timedelta(days=1),
        "Kategorie": "Gehalt",
        "Typ":       "Einnahme",
        "Betrag":    round(gehalt + bonus, 2),
        "Notiz":     "Monatsgehalt" + (" + Bonus" if bonus else ""),
    })
    # Ausgaben
    for kat, (basis, std, freq) in kategorien.items():
        for _ in range(freq):
            tag = np.random.randint(1, 28)
            betrag = max(0, round(basis/freq + np.random.normal(0, std/freq), 2))
            eintraege.append({
                "Datum":     monat + pd.Timedelta(days=tag),
                "Kategorie": kat,
                "Typ":       "Ausgabe",
                "Betrag":    betrag,
                "Notiz":     f"{kat} {monat.strftime('%b %Y')}",
            })

df = pd.DataFrame(eintraege).sort_values("Datum").reset_index(drop=True)
df["Datum"] = pd.to_datetime(df["Datum"])
df.to_csv("haushaltsbuch.csv", index=False)
print(f"   {len(df)} Eintraege, {df['Kategorie'].nunique()} Kategorien")

# --- SCHRITT 2: Monatliche Bilanz ---
print("\n2) Monatliche Bilanz:")
df["Monat"] = df["Datum"].dt.to_period("M")
monats_ein  = df[df["Typ"]=="Einnahme"].groupby("Monat")["Betrag"].sum()
monats_aus  = df[df["Typ"]=="Ausgabe"].groupby("Monat")["Betrag"].sum()
bilanz      = (monats_ein - monats_aus).round(2)

monats_df = pd.DataFrame({
    "Einnahmen": monats_ein,
    "Ausgaben":  monats_aus,
    "Bilanz":    bilanz,
    "Sparquote": ((bilanz / monats_ein)*100).round(1),
}).round(2)
print(monats_df.to_string())
print(f"\n   Jahres-Sparquote: {bilanz.sum()/monats_ein.sum()*100:.1f}%")
print(f"   Ersparnisse 2024: {bilanz.sum():.2f} EUR")

# --- SCHRITT 3: Kategorienanalyse ---
print("\n3) Ausgaben nach Kategorie:")
kat_sum = (df[df["Typ"]=="Ausgabe"]
           .groupby("Kategorie")["Betrag"].sum()
           .sort_values(ascending=False))
gesamt_aus = kat_sum.sum()
for kat, val in kat_sum.items():
    bar = "█" * int(val/gesamt_aus*30)
    print(f"   {kat:<15} {val:>7.2f} EUR  {val/gesamt_aus*100:4.1f}%  {bar}")

# --- SCHRITT 4: Rolling-Analyse ---
print("\n4) Rollende 3-Monats-Analyse...")
taeglich = df[df["Typ"]=="Ausgabe"].set_index("Datum").resample("D")["Betrag"].sum()
taeglich_voll = taeglich.reindex(pd.date_range(df["Datum"].min(),
                                               df["Datum"].max(), freq="D"), fill_value=0)
rolling30 = taeglich_voll.rolling(30).mean()
print(f"   Ø taegl. Ausgaben (letzte 30T): {rolling30.iloc[-1]:.2f} EUR")

# --- SCHRITT 5: Dashboard ---
print("\n5) Erstelle Dashboard...")
fig = plt.figure(figsize=(13, 10))
fig.suptitle("Haushaltsbuch 2024 – Jahresanalyse", fontsize=14, fontweight="bold")

# Oben links: Monatliche Ein-/Ausgaben
ax1 = fig.add_subplot(2, 2, 1)
x = range(len(monats_df))
ax1.bar([i-0.2 for i in x], monats_df["Einnahmen"], 0.4,
        label="Einnahmen", color="seagreen", alpha=0.85)
ax1.bar([i+0.2 for i in x], monats_df["Ausgaben"],  0.4,
        label="Ausgaben",  color="tomato",   alpha=0.85)
ax1.set_xticks(list(x)); ax1.set_xticklabels(
    [str(m) for m in monats_df.index], rotation=45, ha="right", fontsize=7)
ax1.legend(fontsize=8); ax1.set_title("Monatl. Ein- & Ausgaben")
ax1.set_ylabel("EUR"); ax1.grid(axis="y", alpha=0.3)

# Oben rechts: Monatliche Bilanz (Bar-Chart mit Farbe)
ax2 = fig.add_subplot(2, 2, 2)
farben = ["seagreen" if b >= 0 else "tomato" for b in bilanz]
ax2.bar(range(len(bilanz)), bilanz.values, color=farben, alpha=0.85)
ax2.axhline(0, color="black", lw=0.8)
ax2.set_xticks(range(len(bilanz)))
ax2.set_xticklabels([str(m) for m in bilanz.index], rotation=45, ha="right", fontsize=7)
ax2.set_title("Monatliche Bilanz (Sparrate)"); ax2.set_ylabel("EUR")
ax2.grid(axis="y", alpha=0.3)

# Unten links: Tortendiagramm Ausgaben
ax3 = fig.add_subplot(2, 2, 3)
wedge_props = dict(width=0.55, edgecolor="white")
ax3.pie(kat_sum.values, labels=kat_sum.index, autopct="%1.1f%%",
        startangle=90, wedgeprops=wedge_props, textprops={"fontsize":8})
ax3.set_title("Ausgabenverteilung")

# Unten rechts: Rollende 30-Tage-Ausgaben
ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(taeglich_voll.index, taeglich_voll.values,
         alpha=0.2, color="gray", lw=0.5)
ax4.plot(rolling30.index, rolling30.values,
         color="steelblue", lw=2, label="Rolling 30T")
ax4.set_title("Taegl. Ausgaben + 30T-Mittel")
ax4.set_ylabel("EUR/Tag"); ax4.legend(fontsize=8); ax4.grid(alpha=0.3)
ax4.xaxis.set_major_locator(mticker.MaxNLocator(6))
plt.xticks(rotation=30, ha="right")

plt.tight_layout()
plt.savefig("haushaltsbuch_dashboard.png", dpi=120)
plt.show()
plt.close("all")

print("\n   Gespeichert: haushaltsbuch.csv, haushaltsbuch_dashboard.png")
print("\n" + "=" * 60)
print("Miniprojekt W3/2 abgeschlossen!")
print("=" * 60)
