# tag09_anfaenger.py
# Lerntag 9 - Seaborn: Statistische Visualisierung (Anfaenger)
# Thema: histplot, boxplot, barplot, scatterplot, heatmap, pairplot
# Ausfuehren in Spyder: F5

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
sns.set_theme(style="whitegrid")

print("=" * 60)
print("LERNTAG 9 - Seaborn fuer Anfaenger")
print("=" * 60)
tips = sns.load_dataset("tips")

# AUFGABE 1: Datensatz erkunden
print("\nAUFGABE 1: tips-Datensatz")
print(tips.head()); tips.info()
# LOESUNG: sns.load_dataset("name") laedt Beispiel-DataFrames direkt.

# AUFGABE 2: histplot mit KDE
print("\nAUFGABE 2: histplot")
fig,ax = plt.subplots()
sns.histplot(tips["total_bill"], bins=20, kde=True, color="steelblue", ax=ax)
ax.set_title("Verteilung Rechnungsbetraege"); plt.tight_layout()
plt.savefig("plot_09_02.png", dpi=100); plt.show()
# LOESUNG: kde=True ueberlagert Kerndichteschaetzung.

# AUFGABE 3: Boxplot
print("\nAUFGABE 3: Boxplot")
fig,ax = plt.subplots()
sns.boxplot(x="day", y="tip", data=tips, palette="Set2", ax=ax)
ax.set_title("Trinkgeld nach Wochentag"); plt.tight_layout()
plt.savefig("plot_09_03.png", dpi=100); plt.show()

# AUFGABE 4: Barplot mit Fehlerbalken
print("\nAUFGABE 4: barplot")
fig,ax = plt.subplots()
sns.barplot(x="sex", y="total_bill", data=tips, palette="pastel",
            estimator="mean", errorbar="sd", ax=ax)
ax.set_title("Mittlerer Rechnungsbetrag nach Geschlecht"); plt.tight_layout()
plt.savefig("plot_09_04.png", dpi=100); plt.show()

# AUFGABE 5: Scatterplot mit hue + style
print("\nAUFGABE 5: scatterplot")
fig,ax = plt.subplots()
sns.scatterplot(x="total_bill", y="tip", hue="time", style="smoker",
                data=tips, alpha=0.7, ax=ax)
ax.set_title("Rechnung vs. Trinkgeld"); plt.tight_layout()
plt.savefig("plot_09_05.png", dpi=100); plt.show()

# AUFGABE 6: Violinplot
print("\nAUFGABE 6: violinplot")
fig,ax = plt.subplots()
sns.violinplot(x="time", y="tip", data=tips, palette="muted", inner="quartile", ax=ax)
ax.set_title("Trinkgeld nach Tageszeit"); plt.tight_layout()
plt.savefig("plot_09_06.png", dpi=100); plt.show()

# AUFGABE 7: Korrelations-Heatmap
print("\nAUFGABE 7: Heatmap")
corr = tips.select_dtypes(include="number").corr()
fig,ax = plt.subplots(figsize=(5,4))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, ax=ax)
ax.set_title("Korrelationsmatrix"); plt.tight_layout()
plt.savefig("plot_09_07.png", dpi=100); plt.show()

# AUFGABE 8: countplot
print("\nAUFGABE 8: countplot")
fig,ax = plt.subplots()
sns.countplot(x="day", hue="sex", data=tips, palette="Set1", ax=ax)
ax.set_title("Gaeste nach Tag und Geschlecht"); plt.tight_layout()
plt.savefig("plot_09_08.png", dpi=100); plt.show()

# AUFGABE 9: lineplot mit CI
print("\nAUFGABE 9: lineplot")
np.random.seed(5)
df_ts = pd.DataFrame({
    "Tag":    list(range(30))*3,
    "Umsatz": np.random.normal(500,80,90)+np.tile(np.linspace(0,100,30),3),
    "Filiale":["A"]*30+["B"]*30+["C"]*30
})
fig,ax = plt.subplots(figsize=(8,4))
sns.lineplot(x="Tag", y="Umsatz", hue="Filiale", data=df_ts, ax=ax)
ax.set_title("Tagesumsatz je Filiale"); plt.tight_layout()
plt.savefig("plot_09_09.png", dpi=100); plt.show()

# AUFGABE 10: pairplot
print("\nAUFGABE 10: pairplot")
g = sns.pairplot(tips[["total_bill","tip","size","sex"]], hue="sex",
                 palette="Set1", plot_kws={"alpha":0.5})
g.figure.suptitle("Pairplot tips", y=1.02)
plt.tight_layout(); plt.savefig("plot_09_10.png", dpi=100); plt.show()
plt.close("all")

print("\n" + "=" * 60)
print("Tag 9 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
