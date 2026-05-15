# tag07_anfaenger.py
# Lerntag 7 - Pandas: Grundlagen (Anfaenger)
# Thema: Series, DataFrame, Filtern, Groupby, CSV
# Ausfuehren in Spyder: F5

import pandas as pd
import numpy as np

print("=" * 60)
print("LERNTAG 7 - Pandas fuer Anfaenger")
print("=" * 60)

# AUFGABE 1: Series
print("\nAUFGABE 1: Series")
s = pd.Series([85,92,78,95,61], index=["Anna","Ben","Cara","Dan","Eva"])
print(s)
print("Max:", s.max(), "| Mittelwert:", s.mean().round(1))
# LOESUNG: pd.Series(daten, index=labels) - benannter Vektor.

# AUFGABE 2: DataFrame erstellen
print("\nAUFGABE 2: DataFrame")
df = pd.DataFrame({
    "Name":   ["Anna","Ben","Cara","Dan","Eva"],
    "Alter":  [25,32,28,41,19],
    "Gehalt": [3200,4500,3800,5200,2900],
    "Stadt":  ["Berlin","Hamburg","Berlin","Muenchen","Hamburg"]
})
print(df)
print("\nShape:", df.shape)
# LOESUNG: DataFrame aus Dict von Listen - alle Listen gleich lang.

# AUFGABE 3: Spalten auswaehlen und describe
print("\nAUFGABE 3: Spaltenauswahl + describe")
print(df[["Name","Gehalt"]].head(3))
print("\ndescribe:")
print(df[["Alter","Gehalt"]].describe().round(1))
# LOESUNG: df[["Sp1","Sp2"]] waehlt mehrere Spalten.

# AUFGABE 4: Filtern
print("\nAUFGABE 4: Filtern")
berliner = df[df["Stadt"] == "Berlin"]
print("Berliner:\n", berliner)
gut = df[(df["Gehalt"] > 3500) & (df["Alter"] < 35)]
print("\nGut verdienend und jung:\n", gut)
# LOESUNG: & (und), | (oder) - kein 'and'/'or'.

# AUFGABE 5: Neue Spalten
print("\nAUFGABE 5: Neue Spalten")
df["Jahresgehalt"] = df["Gehalt"] * 12
df["Netto"]        = (df["Jahresgehalt"] * 0.80 / 12).round(2)
print(df[["Name","Gehalt","Netto"]])
# LOESUNG: Neue Spalte = Berechnung aus vorhandenen Spalten.

# AUFGABE 6: Sortieren
print("\nAUFGABE 6: Sortieren")
print(df.sort_values("Gehalt", ascending=False)[["Name","Gehalt"]])
# LOESUNG: sort_values(spalte, ascending=False) = absteigend.

# AUFGABE 7: Fehlende Werte
print("\nAUFGABE 7: Fehlende Werte")
df2 = df.copy()
df2.loc[[1,3], "Gehalt"] = np.nan
print("Fehlende:\n", df2.isnull().sum())
df2["Gehalt"] = df2["Gehalt"].fillna(df2["Gehalt"].mean().round(0))
print("Nach fillna:", df2["Gehalt"].values)
# LOESUNG: fillna(wert) ersetzt NaN. isnull().sum() zaehlt Luecken.

# AUFGABE 8: groupby
print("\nAUFGABE 8: groupby")
stats = df.groupby("Stadt")["Gehalt"].agg(["mean","min","max","count"])
stats.columns = ["Mittelwert","Min","Max","Anzahl"]
print(stats.round(0))
# LOESUNG: groupby(spalte)[ziel].agg([...]) aggregiert nach Kategorie.

# AUFGABE 9: CSV schreiben und lesen
print("\nAUFGABE 9: CSV")
df[["Name","Alter","Gehalt","Stadt"]].to_csv("mitarbeiter.csv", index=False)
df_neu = pd.read_csv("mitarbeiter.csv")
print("Aus CSV:", df_neu.shape, "Zeilen x Spalten")
print(df_neu.dtypes)
# LOESUNG: to_csv(pfad, index=False) | read_csv(pfad).

# AUFGABE 10: apply
print("\nAUFGABE 10: apply")
def stufe(g):
    if g < 3500:   return "Junior"
    elif g < 4500: return "Mid"
    else:          return "Senior"
df["Stufe"] = df["Gehalt"].apply(stufe)
print(df[["Name","Gehalt","Stufe"]])
# LOESUNG: apply(funktion) wendet die Funktion auf jedes Element an.

print("\n" + "=" * 60)
print("Tag 7 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
