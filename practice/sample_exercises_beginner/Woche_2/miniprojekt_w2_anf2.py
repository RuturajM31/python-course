# miniprojekt_w2_anf2.py
# MINIPROJEKT 2 (Anfaenger) - Woche 2
# Titel: Wetter-Protokoll-Auswertung Juli 2024
# Kombiniert: Pandas + Seaborn + Matplotlib
# Ausfuehren in Spyder: F5
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
np.random.seed(42)

print("=" * 60)
print("MINIPROJEKT 2 - Wetterprotokoll Juli 2024")
print("=" * 60)

# --- 1. Daten simulieren ---
tage  = pd.date_range("2024-07-01","2024-07-31",freq="D")
regen = np.random.choice([True,False], 31, p=[0.3,0.7])
df = pd.DataFrame({
    "Datum":        tage,
    "Temp_max":     np.round(20+10*np.random.rand(31),1),
    "Temp_min":     np.round(12+ 5*np.random.rand(31),1),
    "Niederschlag": np.where(regen, np.round(np.random.exponential(8,31),1), 0),
    "Bewoelkung":   np.random.randint(10,100,31)
})
df.loc[[5,12,20],"Temp_max"] = np.nan  # kuenstliche Luecken

# --- 2. Bereinigung ---
print(f"Fehlende Werte: {df.isnull().sum().sum()}")
df["Temp_max"]    = df["Temp_max"].fillna(round(df["Temp_max"].mean(),1))
df["Temp_mittel"] = ((df["Temp_max"]+df["Temp_min"])/2).round(1)
df["Regen"]       = df["Niederschlag"].apply(lambda x: "Regentag" if x>0 else "Sonnentag")

# --- 3. Statistik ---
print(f"Mittl. Hoechsttemp.: {df['Temp_max'].mean():.1f} C")
print(f"Regentage:           {(df['Niederschlag']>0).sum()}")
print(f"Gesamtniederschlag:  {df['Niederschlag'].sum():.1f} mm")

# --- 4. Visualisierung ---
fig, axes = plt.subplots(2,2, figsize=(12,8))
fig.suptitle("Wetterprotokoll Juli 2024", fontsize=14, fontweight="bold")

axes[0,0].fill_between(df["Datum"],df["Temp_min"],df["Temp_max"],alpha=0.3,color="tomato")
axes[0,0].plot(df["Datum"],df["Temp_mittel"],color="red",label="Mittel")
axes[0,0].set_title("Temperaturverlauf"); axes[0,0].set_ylabel("Grad C")
axes[0,0].legend(); axes[0,0].grid(True,alpha=0.4)
plt.setp(axes[0,0].xaxis.get_majorticklabels(), rotation=30)

axes[0,1].bar(df["Datum"],df["Niederschlag"],color="steelblue",width=0.8)
axes[0,1].set_title("Niederschlag"); axes[0,1].set_ylabel("mm")
plt.setp(axes[0,1].xaxis.get_majorticklabels(), rotation=30)

sns.histplot(df["Temp_max"],bins=10,kde=True,color="tomato",ax=axes[1,0])
axes[1,0].set_title("Verteilung Hoechsttemp.")

sns.boxplot(x="Regen",y="Bewoelkung",data=df,palette=["steelblue","gold"],ax=axes[1,1])
axes[1,1].set_title("Bewoelkung: Regen- vs. Sonnentag")

plt.tight_layout(); plt.savefig("mp2_wetter.png", dpi=150); plt.show()
df.to_csv("wetter_juli.csv", index=False)
print("\nDateien gespeichert: mp2_wetter.png, wetter_juli.csv")
