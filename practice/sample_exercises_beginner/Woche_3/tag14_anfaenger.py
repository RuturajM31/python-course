# tag14_anfaenger.py
# Lerntag 14 - Zeitreihenanalyse: Grundlagen (Anfaenger)
# Thema: resample, rolling, pct_change, Anomalieerkennung, Visualisierung
# Ausfuehren in Spyder: F5

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("LERNTAG 14 - Zeitreihenanalyse fuer Anfaenger")
print("=" * 60)
np.random.seed(42)

# AUFGABE 1: Zeitreihe erzeugen
print("\nAUFGABE 1: Zeitreihe erstellen")
datum  = pd.date_range("2022-01-01", "2023-12-31", freq="D")
umsatz = (200 + np.arange(len(datum))*0.15
          + 50*np.sin(2*np.pi*np.arange(len(datum))/365)
          + np.random.randn(len(datum))*20)
ts = pd.Series(umsatz.round(2), index=datum, name="Umsatz")
print(ts.head(3)); print(f"Laenge: {len(ts)} Tage")
# LOESUNG: pd.Series(werte, index=DatetimeIndex) = Zeitreihe.

# AUFGABE 2: Grundstatistik
print("\nAUFGABE 2: Statistik")
print(ts.describe().round(2))
print(f"Trend: {ts.iloc[0]:.2f} -> {ts.iloc[-1]:.2f}  (+{ts.iloc[-1]-ts.iloc[0]:.2f})")
# LOESUNG: .iloc[0] = erster Wert, .iloc[-1] = letzter Wert.

# AUFGABE 3: Monatliche Aggregation
print("\nAUFGABE 3: Monatlich")
monatlich = ts.resample("ME").agg(["sum","mean","min","max"]).round(1)
monatlich.index = monatlich.index.strftime("%Y-%m")
print(monatlich.head(6))
# LOESUNG: resample("ME") = Monatsende-Aggregation.

# AUFGABE 4: Rollende Durchschnitte
print("\nAUFGABE 4: Rolling Mean")
df = ts.to_frame()
df["MA7"]  = ts.rolling(7).mean()
df["MA30"] = ts.rolling(30).mean()
df["MA90"] = ts.rolling(90).mean()
print(df.tail(4).round(2))
# LOESUNG: rolling(n).mean() glaettet kurzfristige Schwankungen.

# AUFGABE 5: Visualisierung
print("\nAUFGABE 5: Plot")
fig, ax = plt.subplots(figsize=(11,4))
ax.plot(df.index, df["Umsatz"], alpha=0.3, color="gray", lw=0.7, label="Tagesumsatz")
ax.plot(df.index, df["MA7"],  color="steelblue", lw=1,   label="MA7")
ax.plot(df.index, df["MA30"], color="navy",      lw=2,   label="MA30")
ax.plot(df.index, df["MA90"], color="red",       lw=2,   label="MA90")
ax.set_title("Umsatz-Zeitreihe 2022-2023"); ax.set_ylabel("EUR")
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.savefig("plot_14_05.png", dpi=100); plt.show()

# AUFGABE 6: Wochentagsanalyse
print("\nAUFGABE 6: Wochentage")
df["Wochentag"] = df.index.dayofweek
wt_namen = ["Mo","Di","Mi","Do","Fr","Sa","So"]
wt = df.groupby("Wochentag")["Umsatz"].mean().round(1)
wt.index = wt_namen
print(wt)
fig, ax = plt.subplots(figsize=(7,3))
wt.plot(kind="bar", ax=ax, color="steelblue", edgecolor="white")
ax.set_title("Durchschnittsumsatz nach Wochentag"); ax.set_ylabel("EUR")
plt.xticks(rotation=0); plt.tight_layout()
plt.savefig("plot_14_06.png", dpi=100); plt.show()
# LOESUNG: .index.dayofweek gibt 0=Mo ... 6=So.

# AUFGABE 7: Jahresvergleich
print("\nAUFGABE 7: Jahresvergleich")
jaehrlich = ts.resample("YE").sum()
jaehrlich.index = jaehrlich.index.year
for j, v in jaehrlich.items():
    print(f"  {j}: {v:,.0f} EUR")
# LOESUNG: resample("YE") fasst nach Jahresende zusammen.

# AUFGABE 8: Anomalieerkennung
print("\nAUFGABE 8: Anomalien")
mittel = ts.rolling(30, center=True).mean()
std    = ts.rolling(30, center=True).std()
anom   = ts[(ts > mittel + 2*std) | (ts < mittel - 2*std)]
print(f"Anomalien (±2σ): {len(anom)}")
print(anom.head(4).round(2))
# LOESUNG: Werte ausserhalb Mittelwert ± 2*Std. = Ausreisser.

# AUFGABE 9: Prozentuale Veraenderung
print("\nAUFGABE 9: pct_change")
woeche = ts.resample("W").mean()
woeche_pct = woeche.pct_change() * 100
print("Wochenaenderung (erste 5):")
print(woeche_pct.dropna().head(5).round(2))
# LOESUNG: pct_change() = prozentuale Aenderung zur Vorperiode.

# AUFGABE 10: Speichern
print("\nAUFGABE 10: CSV")
df.to_csv("zeitreihe_umsatz.csv")
print("zeitreihe_umsatz.csv gespeichert.")
plt.close("all")

print("\n" + "=" * 60)
print("Tag 14 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
