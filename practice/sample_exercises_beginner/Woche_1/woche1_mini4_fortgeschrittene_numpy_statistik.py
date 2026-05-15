# woche1_mini4_fortgeschrittene_numpy_statistik.py
# MINIPROJEKT WOCHE 1 - Fortgeschrittene (2/2)
# Titel: Statistische Datenanalyse mit NumPy und Pandas
# Thema: NumPy, Pandas, Visualisierung, Hypothesentests (Lerntage 4-5)
# Ausfuehren in Spyder: F5

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import stats

print("=" * 60)
print("MINIPROJEKT W1/4 (Fortgeschrittene): Statistische Analyse")
print("=" * 60)
np.random.seed(42)

# --- SCHRITT 1: Datensatz simulieren ---
print("\n1) Erstelle Produktionsdatensatz (Fabrik-Simulation)...")

N_SCHICHTEN   = 90   # 3 Monate, 1 Schicht/Tag
MASCHINEN     = ["M1","M2","M3","M4"]
SCHICHTTYPEN  = ["Frueh","Spaet","Nacht"]

records = []
for tag in range(N_SCHICHTEN):
    datum     = pd.Timestamp("2024-01-01") + pd.Timedelta(days=tag)
    schicht   = SCHICHTTYPEN[tag % 3]
    for maschine in MASCHINEN:
        # Verschiedene Maschinen haben verschiedene Grundleistungen
        basis = {"M1":950,"M2":1020,"M3":880,"M4":1100}[maschine]
        # Schichteffekte
        effekt = {"Frueh":1.05,"Spaet":1.00,"Nacht":0.92}[schicht]
        # Wochen-Trend: langsame Verbesserung
        trend  = 1 + tag * 0.001
        # Rauschen
        rausch = np.random.normal(1.0, 0.06)
        # Gelegentliche Ausfaelle
        ausfall = 0.7 if np.random.random() < 0.04 else 1.0
        produktion = round(basis * effekt * trend * rausch * ausfall)
        ausschuss  = round(np.random.beta(2,20) * produktion)
        laufzeit   = round(np.random.normal(7.8, 0.4), 2)  # Stunden
        records.append({
            "Datum":      datum,
            "Maschine":   maschine,
            "Schicht":    schicht,
            "Produktion": produktion,
            "Ausschuss":  ausschuss,
            "Laufzeit_h": laufzeit,
            "KW":         datum.isocalendar().week,
            "Monat":      datum.month,
        })

df = pd.DataFrame(records)
df["Ausschuss_pct"] = (df["Ausschuss"]/df["Produktion"]*100).round(2)
df["Effizienz"]     = (df["Produktion"]/df["Laufzeit_h"]).round(1)
df.to_csv("produktion_daten.csv", index=False)
print(f"   {len(df)} Datensaetze erstellt")
print(df.describe()[["Produktion","Ausschuss_pct","Effizienz"]].round(2))

# --- SCHRITT 2: Deskriptive Statistik ---
print("\n2) Deskriptive Statistik je Maschine:")
masch_stats = df.groupby("Maschine").agg(
    Prod_Mittel =("Produktion",    "mean"),
    Prod_Std    =("Produktion",    "std"),
    Prod_Min    =("Produktion",    "min"),
    Prod_Max    =("Produktion",    "max"),
    Aussch_Mittel=("Ausschuss_pct","mean"),
    Effizienz   =("Effizienz",     "mean"),
).round(2)
print(masch_stats)

# --- SCHRITT 3: Hypothesentest ---
print("\n3) Hypothesentests:")
# H0: Frühschicht und Nachtschicht haben gleiche Produktion
frueh  = df[df["Schicht"]=="Frueh"]["Produktion"].values
nacht  = df[df["Schicht"]=="Nacht"]["Produktion"].values
t_stat, p_val = stats.ttest_ind(frueh, nacht)
print(f"   t-Test Frueh vs. Nacht:")
print(f"     t={t_stat:.4f}, p={p_val:.4f}")
print(f"     Ergebnis: {'Signifikanter Unterschied!' if p_val<0.05 else 'Kein signifikanter Unterschied.'}")

# Korrelation Laufzeit <-> Produktion
corr, p_corr = stats.pearsonr(df["Laufzeit_h"], df["Produktion"])
print(f"\n   Korrelation Laufzeit/Produktion: r={corr:.3f}, p={p_corr:.4f}")

# Normalitaetstest (Shapiro-Wilk auf Stichprobe)
stichprobe = np.random.choice(df["Produktion"].values, 50)
stat_sw, p_sw = stats.shapiro(stichprobe)
print(f"\n   Shapiro-Wilk (Normalitaet Produktion): W={stat_sw:.4f}, p={p_sw:.4f}")
print(f"     -> {'Normalverteilt (p>=0.05)' if p_sw>=0.05 else 'Nicht normalverteilt (p<0.05)'}")

# --- SCHRITT 4: Zeitverlauf ---
print("\n4) Wochentrend berechnen...")
wochen = df.groupby(["KW","Maschine"])["Produktion"].mean().unstack()
print(wochen.tail(4).round(0))

# --- SCHRITT 5: Dashboard ---
print("\n5) Erstelle Analyse-Dashboard...")
fig = plt.figure(figsize=(15,11))
fig.suptitle("Produktionsanalyse Dashboard | Jan–Mrz 2024",
             fontsize=14, fontweight="bold")
gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.5, wspace=0.35)

farben = {"M1":"#4575b4","M2":"#91bfdb","M3":"#fc8d59","M4":"#d73027"}

# Plot 1: Woechentrend je Maschine (oben, ganzer Bereich)
ax1 = fig.add_subplot(gs[0, :])
for maschine in MASCHINEN:
    w_serie = df[df["Maschine"]==maschine].groupby("KW")["Produktion"].mean()
    ax1.plot(w_serie.index, w_serie.values, "o-", lw=2, ms=5,
             color=farben[maschine], label=maschine)
ax1.set_title("Wochentrend Produktion je Maschine")
ax1.set_xlabel("Kalenderwoche"); ax1.set_ylabel("Ø Stueck/Schicht")
ax1.legend(fontsize=9); ax1.grid(alpha=0.3)

# Plot 2: Boxplot Produktion je Maschine
ax2 = fig.add_subplot(gs[1, 0])
daten_masch = [df[df["Maschine"]==m]["Produktion"].values for m in MASCHINEN]
bp = ax2.boxplot(daten_masch, labels=MASCHINEN, patch_artist=True)
for patch, m in zip(bp["boxes"], MASCHINEN):
    patch.set_facecolor(farben[m]); patch.set_alpha(0.7)
ax2.set_title("Produktionsverteilung"); ax2.set_ylabel("Stueck")
ax2.grid(axis="y", alpha=0.3)

# Plot 3: Ausschuss je Schicht
ax3 = fig.add_subplot(gs[1, 1])
schicht_aussch = df.groupby("Schicht")["Ausschuss_pct"].mean()
farben_s = ["#4575b4","#fc8d59","#d73027"]
ax3.bar(schicht_aussch.index, schicht_aussch.values,
        color=farben_s, edgecolor="white")
ax3.set_title("Ø Ausschuss je Schicht (%)"); ax3.set_ylabel("%")
ax3.grid(axis="y", alpha=0.3)

# Plot 4: Scatterplot Laufzeit vs. Effizienz
ax4 = fig.add_subplot(gs[1, 2])
for m in MASCHINEN:
    sub = df[df["Maschine"]==m]
    ax4.scatter(sub["Laufzeit_h"], sub["Effizienz"],
                color=farben[m], alpha=0.4, s=15, label=m)
z = np.polyfit(df["Laufzeit_h"], df["Effizienz"], 1)
xlin = np.linspace(df["Laufzeit_h"].min(), df["Laufzeit_h"].max(), 100)
ax4.plot(xlin, np.polyval(z,xlin), "k--", lw=1.5)
ax4.set_title(f"Laufzeit vs. Effizienz (r={corr:.2f})")
ax4.set_xlabel("Laufzeit (h)"); ax4.set_ylabel("Stueck/h")
ax4.legend(fontsize=7); ax4.grid(alpha=0.3)

# Plot 5: Histogramm + Normalverteilung
ax5 = fig.add_subplot(gs[2, 0])
alle_prod = df["Produktion"].values
ax5.hist(alle_prod, bins=25, density=True, color="steelblue",
         edgecolor="white", alpha=0.7, label="Daten")
mu, sigma = alle_prod.mean(), alle_prod.std()
x_norm = np.linspace(alle_prod.min(), alle_prod.max(), 200)
ax5.plot(x_norm, stats.norm.pdf(x_norm,mu,sigma), "r-", lw=2,
         label=f"N({mu:.0f},{sigma:.0f})")
ax5.set_title("Produktionsverteilung (alle)"); ax5.legend(fontsize=8)
ax5.grid(alpha=0.3)

# Plot 6: Heatmap Maschine x Schicht
ax6 = fig.add_subplot(gs[2, 1:])
pivot = df.pivot_table(values="Produktion", index="Maschine",
                        columns="Schicht", aggfunc="mean")
im = ax6.imshow(pivot.values, cmap="RdYlGn", aspect="auto")
ax6.set_xticks(range(len(pivot.columns))); ax6.set_xticklabels(pivot.columns)
ax6.set_yticks(range(len(pivot.index)));  ax6.set_yticklabels(pivot.index)
for i in range(len(pivot.index)):
    for j in range(len(pivot.columns)):
        ax6.text(j, i, f"{pivot.values[i,j]:.0f}", ha="center",
                 va="center", fontsize=11, fontweight="bold")
fig.colorbar(im, ax=ax6, shrink=0.8, label="Ø Produktion")
ax6.set_title("Heatmap: Ø Produktion je Maschine x Schicht")

plt.savefig("produktion_dashboard.png", dpi=120, bbox_inches="tight")
plt.show()
plt.close("all")

print("\nGespeichert: produktion_daten.csv, produktion_dashboard.png")
print("\n" + "=" * 60)
print("Miniprojekt W1/4 abgeschlossen!")
print("=" * 60)
