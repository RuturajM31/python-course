# tag05_anfaenger.py
# Lerntag 5 - Pandas Grundlagen (Anfaenger)
# Thema: Series, DataFrame, Einlesen, Filtern, Groupby, Visualisierung
# Ausfuehren in Spyder: F5

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("LERNTAG 5 - Pandas fuer Anfaenger")
print("=" * 60)
np.random.seed(42)

# AUFGABE 1: Series erstellen
print("\nAUFGABE 1: Series")
temp_woche = pd.Series([18.5,20.1,17.3,22.4,25.1,23.6,19.8],
    index=["Mo","Di","Mi","Do","Fr","Sa","So"], name="Temperatur (°C)")
print(temp_woche)
print(f"Mittel: {temp_woche.mean():.1f}°C")
print(f"Max:    {temp_woche.max()} am {temp_woche.idxmax()}")
# LOESUNG: pd.Series(data, index=..., name=...) erzeugt beschriftete 1D-Datenreihe.

# AUFGABE 2: DataFrame erstellen
print("\nAUFGABE 2: DataFrame")
df = pd.DataFrame({
    "Name":    ["Anna","Bob","Cara","Dave","Eva","Frank"],
    "Alter":   [28,35,22,41,30,27],
    "Gehalt":  [3200,4500,2800,5100,3600,3900],
    "Abt":     ["IT","Sales","IT","Mgmt","HR","IT"],
    "Jahre":   [3,8,1,15,5,4],
})
print(df)
print(f"\nShape: {df.shape}")
print(f"Dtypes:\n{df.dtypes}")
# LOESUNG: pd.DataFrame(dict) erzeugt Tabelle. .shape gibt (Zeilen,Spalten).

# AUFGABE 3: Auswahl und Filterung
print("\nAUFGABE 3: Filtern")
print("IT-Mitarbeiter:")
it = df[df["Abt"]=="IT"]
print(it[["Name","Gehalt","Jahre"]])
print("\nMitarbeiter mit Gehalt > 3500:")
gut = df[df["Gehalt"] > 3500]
print(gut[["Name","Gehalt","Abt"]])
# LOESUNG: df[bedingung] filtert Zeilen. df[["sp1","sp2"]] waehlt Spalten.

# AUFGABE 4: Neue Spalten berechnen
print("\nAUFGABE 4: Neue Spalten")
df["Jahresgehalt"] = df["Gehalt"] * 12
df["Gehalt_kl"]    = pd.cut(df["Gehalt"],
    bins=[0,3000,4000,6000], labels=["<3k","3k-4k",">4k"])
df["Senior"] = df["Jahre"] >= 5
print(df[["Name","Gehalt","Jahresgehalt","Gehalt_kl","Senior"]])
# LOESUNG: df["neu"] = ausdruck erzeugt neue Spalte. pd.cut() = Kategorisierung.

# AUFGABE 5: Grundlegende Statistik
print("\nAUFGABE 5: Statistik")
print(df[["Alter","Gehalt","Jahre"]].describe().round(1))
print(f"\nKorrelation Alter/Gehalt: {df['Alter'].corr(df['Gehalt']):.3f}")
# LOESUNG: .describe() gibt alle Grundkennzahlen. .corr() berechnet Korrelation.

# AUFGABE 6: Groupby
print("\nAUFGABE 6: Groupby")
abt = df.groupby("Abt").agg(
    Anzahl=("Name","count"),
    Gehalt_Mittel=("Gehalt","mean"),
    Alter_Mittel=("Alter","mean")
).round(1)
print(abt)
# LOESUNG: .groupby(spalte).agg(neu=(spalte, funktion)) = Aggregation je Gruppe.

# AUFGABE 7: Sortieren und Ranking
print("\nAUFGABE 7: Sortieren")
df_sort = df.sort_values("Gehalt", ascending=False).reset_index(drop=True)
df_sort["Rang"] = df_sort["Gehalt"].rank(ascending=False).astype(int)
print(df_sort[["Rang","Name","Gehalt","Abt"]])
# LOESUNG: .sort_values() sortiert. .rank() gibt Rang (1=hoechste). reset_index() neu nummerieren.

# AUFGABE 8: CSV lesen und schreiben
print("\nAUFGABE 8: CSV")
df.to_csv("mitarbeiter.csv", index=False)
df2 = pd.read_csv("mitarbeiter.csv")
print(f"Eingelesen: {df2.shape}, Spalten: {list(df2.columns)}")
print(df2.head(3))
# LOESUNG: .to_csv(pfad, index=False) speichert. pd.read_csv(pfad) laedt.

# AUFGABE 9: Fehlende Werte
print("\nAUFGABE 9: NaN behandeln")
df3 = df.copy()
df3.loc[1,"Gehalt"] = np.nan
df3.loc[3,"Alter"]  = np.nan
print(f"NaN-Anzahl:\n{df3.isnull().sum()}")
df3["Gehalt"] = df3["Gehalt"].fillna(df3["Gehalt"].median())
df3.dropna(subset=["Alter"], inplace=True)
print(f"Nach Bereinigung: {df3.shape}")
# LOESUNG: .isnull().sum() zaehlt NaN. .fillna() ersetzt, .dropna() loescht Zeilen.

# AUFGABE 10: Visualisierung
print("\nAUFGABE 10: Plot")
fig, axes = plt.subplots(1, 2, figsize=(11,4))
df.groupby("Abt")["Gehalt"].mean().sort_values().plot(
    kind="barh", ax=axes[0], color="steelblue", title="Ø Gehalt je Abteilung")
axes[0].set_xlabel("EUR")
df["Gehalt"].plot(kind="hist", bins=6, ax=axes[1], color="tomato", edgecolor="white",
                  title="Gehaltsverteilung")
axes[1].set_xlabel("EUR")
plt.tight_layout(); plt.savefig("plot_05_10.png", dpi=100); plt.show()
plt.close("all")
print("plot_05_10.png gespeichert.")
# LOESUNG: .plot(kind="barh") und .plot(kind="hist") = schnelle Pandas-Visualisierung.

print("\n" + "=" * 60)
print("Tag 5 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
