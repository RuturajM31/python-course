# tag15_anfaenger.py
# Lerntag 15 - Abschluss: Datenpipeline Anfaenger
# Thema: Daten generieren -> bereinigen -> analysieren -> visualisieren
# Ausfuehren in Spyder: F5

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
np.random.seed(99)

print("=" * 60)
print("LERNTAG 15 - Abschluss-Pipeline fuer Anfaenger")
print("=" * 60)

# AUFGABE 1: Datensatz erstellen
print("\nAUFGABE 1: Datensatz erstellen")
n = 200
df = pd.DataFrame({
    "ID":        range(1, n+1),
    "Alter":     np.random.randint(18, 65, n),
    "Gehalt":    np.random.normal(3500, 800, n).round(0),
    "Erfahrung": np.random.randint(0, 30, n),
    "Abteilung": np.random.choice(["IT","HR","Finance","Sales","Logistik"], n),
    "Geschlecht":np.random.choice(["m","w"], n, p=[0.55,0.45]),
})
df["Gehalt"] = (df["Gehalt"] + df["Erfahrung"] * 80).round(0)
df.to_csv("datensatz_mitarbeiter.csv", index=False)
print(df.shape); print(df.dtypes)
# LOESUNG: Realistische Daten mit korrelierten Variablen simulieren.

# AUFGABE 2: Einlesen und pruefen
print("\nAUFGABE 2: Einlesen + Pruefen")
df2 = pd.read_csv("datensatz_mitarbeiter.csv")
print(df2.describe()[["Alter","Gehalt","Erfahrung"]].round(1))
print(f"\nDuplikate: {df2.duplicated().sum()}")
print(f"Fehlende:  {df2.isnull().sum().sum()}")
# LOESUNG: .describe() und .isnull() fuer erste Datenpruefung.

# AUFGABE 3: Filtern
print("\nAUFGABE 3: Filtern")
senior = df2[(df2["Alter"] > 45) & (df2["Gehalt"] > 4000)]
print(f"Senior + gut bezahlt: {len(senior)}")
print(senior[["ID","Alter","Gehalt","Abteilung"]].head(5).to_string(index=False))

# AUFGABE 4: Neue Kategorien
print("\nAUFGABE 4: Kategorisierung")
df2["Altersgruppe"] = pd.cut(df2["Alter"],
    bins=[17,29,39,49,65], labels=["18-29","30-39","40-49","50-65"])
df2["Gehalt_kl"] = pd.cut(df2["Gehalt"],
    bins=[0,3000,4000,5500,99999], labels=["<3k","3k-4k","4k-5.5k",">5.5k"])
print(df2["Altersgruppe"].value_counts().sort_index())

# AUFGABE 5: Groupby-Analyse
print("\nAUFGABE 5: Groupby")
abt = df2.groupby("Abteilung").agg(
    Anzahl=("ID","count"),
    Gehalt_Mittel=("Gehalt","mean"),
    Alter_Mittel=("Alter","mean")
).round(1)
print(abt.sort_values("Gehalt_Mittel", ascending=False))

# AUFGABE 6: Balkenplot
print("\nAUFGABE 6: Plot Gehalt")
fig, ax = plt.subplots(figsize=(8,4))
abt["Gehalt_Mittel"].sort_values().plot(kind="barh", ax=ax, color="steelblue")
ax.set_title("Durchschnittsgehalt je Abteilung"); ax.set_xlabel("EUR")
plt.tight_layout(); plt.savefig("plot_15_06.png", dpi=100); plt.show()

# AUFGABE 7: Heatmap Korrelation
print("\nAUFGABE 7: Korrelation")
corr = df2[["Alter","Gehalt","Erfahrung"]].corr()
fig, ax = plt.subplots(figsize=(5,4))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, ax=ax)
ax.set_title("Korrelationsmatrix"); plt.tight_layout()
plt.savefig("plot_15_07.png", dpi=100); plt.show()
print(corr.round(3))

# AUFGABE 8: Scatterplot
print("\nAUFGABE 8: Scatterplot")
fig, ax = plt.subplots(figsize=(8,5))
for abt_name in df2["Abteilung"].unique():
    sub = df2[df2["Abteilung"]==abt_name]
    ax.scatter(sub["Erfahrung"], sub["Gehalt"], label=abt_name, alpha=0.55, s=30)
ax.set_title("Erfahrung vs. Gehalt nach Abteilung")
ax.set_xlabel("Erfahrungsjahre"); ax.set_ylabel("Gehalt EUR")
ax.legend(); plt.tight_layout(); plt.savefig("plot_15_08.png", dpi=100); plt.show()

# AUFGABE 9: Violinplot
print("\nAUFGABE 9: Violinplot")
fig, ax = plt.subplots(figsize=(9,4))
sns.violinplot(x="Abteilung", y="Gehalt", hue="Geschlecht",
               data=df2, split=True, palette="Set2", ax=ax)
ax.set_title("Gehaltsverteilung nach Abteilung und Geschlecht")
plt.tight_layout(); plt.savefig("plot_15_09.png", dpi=100); plt.show()

# AUFGABE 10: Abschlussbericht
print("\nAUFGABE 10: Bericht")
print("=" * 50)
print(f"Mitarbeiter gesamt:    {len(df2)}")
print(f"Durchschnittsalter:    {df2['Alter'].mean():.1f} Jahre")
print(f"Durchschnittsgehalt:   {df2['Gehalt'].mean():.0f} EUR")
print(f"Gehaltsrange:          {df2['Gehalt'].min():.0f} - {df2['Gehalt'].max():.0f} EUR")
print(f"Groesste Abteilung:    {df2['Abteilung'].value_counts().idxmax()}")
print(f"Beste Abt. (Gehalt):   {abt['Gehalt_Mittel'].idxmax()}")
plt.close("all")

print("\n" + "=" * 60)
print("Tag 15 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("Glueckwunsch - Kurs abgeschlossen!")
print("=" * 60)
