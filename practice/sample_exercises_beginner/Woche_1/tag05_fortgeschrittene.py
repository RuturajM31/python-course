# tag05_fortgeschrittene.py
# Lerntag 5 - Pandas Fortgeschrittene
# Thema: MultiIndex, Pivot, merge/join, apply, window, query, style
# Ausfuehren in Spyder: F5

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("LERNTAG 5 - Pandas Fortgeschrittene")
print("=" * 60)
np.random.seed(42)

n = 300
df = pd.DataFrame({
    "ID":       range(1,n+1),
    "Name":     [f"MA{i:04d}" for i in range(1,n+1)],
    "Abt":      np.random.choice(["IT","HR","Finance","Sales","Logistik"],n),
    "Region":   np.random.choice(["Nord","Sued","West","Ost"],n),
    "Gehalt":   np.random.normal(3800,800,n).clip(2000,7000).round(0),
    "Erfahrung":np.random.randint(0,30,n),
    "Bewertung":np.random.choice(["A","B","C"],n,p=[0.3,0.5,0.2]),
    "Eintrittsdatum": pd.date_range("2010-01-01",periods=n,freq="5D"),
})

# AUFGABE 1: MultiIndex
print("\nAUFGABE 1: MultiIndex")
mi = df.groupby(["Abt","Region"])["Gehalt"].agg(["mean","count"]).round(1)
print(mi.head(8))
print(f"\nIT-Nord: {mi.loc[('IT','Nord'),'mean']:.1f} EUR")
print(f"IT alle Regionen:\n{mi.loc['IT']}")
# LOESUNG: groupby mehrerer Spalten -> MultiIndex. loc[(lvl1,lvl2)] = Zugriff.

# AUFGABE 2: Pivot Table
print("\nAUFGABE 2: Pivot")
pivot = df.pivot_table(values="Gehalt", index="Abt", columns="Region",
                       aggfunc="mean", margins=True, margins_name="Gesamt")
print(pivot.round(0))
# LOESUNG: pivot_table wie Excel-Pivot. margins=True addiert Zeilensummen.

# AUFGABE 3: Merge / Join
print("\nAUFGABE 3: Merge")
abt_info = pd.DataFrame({
    "Abt":    ["IT","HR","Finance","Sales","Logistik"],
    "Leiter": ["Klaus","Petra","Hans","Maria","Joerg"],
    "Budget": [500,200,750,600,350]
})
merged = df.merge(abt_info, on="Abt", how="left")
print(merged[["Name","Abt","Gehalt","Leiter","Budget"]].head(5))
print(f"Shape: {merged.shape}")
# LOESUNG: .merge(df2, on="key", how="left/right/inner/outer") = SQL-Join.

# AUFGABE 4: apply und applymap
print("\nAUFGABE 4: apply")
def gehalt_klasse(g):
    if g < 3000: return "Niedrig"
    if g < 4500: return "Mittel"
    return "Hoch"

df["Gehalt_kl"] = df["Gehalt"].apply(gehalt_klasse)
df["Name_upper"]= df["Name"].apply(str.upper)
df["Punkte"]    = df.apply(lambda row: row["Erfahrung"]*100
                            + (200 if row["Bewertung"]=="A" else
                               100 if row["Bewertung"]=="B" else 0), axis=1)
print(df[["Name","Gehalt","Gehalt_kl","Punkte"]].head(5))
# LOESUNG: .apply(func) auf Series. .apply(func, axis=1) zeilenweise auf DataFrame.

# AUFGABE 5: Rolling Windows
print("\nAUFGABE 5: Rolling")
ts = df.set_index("Eintrittsdatum")["Gehalt"].resample("ME").mean()
ts_df = pd.DataFrame({"Gehalt": ts})
ts_df["MA3"]  = ts.rolling(3).mean()
ts_df["MA6"]  = ts.rolling(6).mean()
ts_df["Std3"] = ts.rolling(3).std()
fig, ax = plt.subplots(figsize=(11,4))
ax.plot(ts_df.index, ts_df["Gehalt"], alpha=0.4, label="Monatlich")
ax.plot(ts_df.index, ts_df["MA3"],  lw=2, label="MA3")
ax.plot(ts_df.index, ts_df["MA6"],  lw=2, label="MA6")
ax.fill_between(ts_df.index,
    ts_df["MA3"]-ts_df["Std3"], ts_df["MA3"]+ts_df["Std3"], alpha=0.15)
ax.legend(); ax.grid(alpha=0.3)
ax.set_title("Gehalt-Zeitreihe mit rolling MA")
plt.tight_layout(); plt.savefig("plot_05f_05.png", dpi=100); plt.show()
# LOESUNG: .rolling(n).mean()/.std() = gleitendes Fenster.

# AUFGABE 6: query() und eval()
print("\nAUFGABE 6: query / eval")
result = df.query("Gehalt > 4500 and Erfahrung >= 10 and Bewertung == 'A'")
print(f"Top-Mitarbeiter (>{4500} EUR, >=10 Jahre, Note A): {len(result)}")
print(result[["Name","Abt","Gehalt","Erfahrung"]].head(5))
df.eval("Bonus = Gehalt * 0.1 * (Erfahrung / 10)", inplace=True)
print(f"Bonus-Spalte OK: {df['Bonus'].describe().round(0)}")
# LOESUNG: .query("ausdr") = SQL-WHERE als String. .eval() berechnet neue Spalten.

# AUFGABE 7: Kategorische Daten
print("\nAUFGABE 7: Categoricals")
df["Bewertung_cat"] = pd.Categorical(df["Bewertung"],
    categories=["C","B","A"], ordered=True)
print(df["Bewertung_cat"].value_counts())
print(df[df["Bewertung_cat"] >= "B"].shape[0], "Mitarbeiter mit B oder besser")
# LOESUNG: pd.Categorical(..., ordered=True) erlaubt Vergleiche (<,>).

# AUFGABE 8: Stack und Unstack
print("\nAUFGABE 8: Stack / Unstack")
mi2 = df.groupby(["Bewertung","Abt"])["Gehalt"].mean().round(0)
unstacked = mi2.unstack("Abt").fillna(0)
print(unstacked.astype(int))
# LOESUNG: .unstack() pivotiert inneren Index zu Spalten. .stack() umgekehrt.

# AUFGABE 9: Explode und String-Methoden
print("\nAUFGABE 9: String-Methoden")
test_df = pd.DataFrame({"Mitarbeiter": ["Anna Meier","Bob Mueller","Cara Schmidt"]})
test_df["Vorname"] = test_df["Mitarbeiter"].str.split().str[0]
test_df["Nachname"]= test_df["Mitarbeiter"].str.split().str[-1]
test_df["Initial"] = test_df["Vorname"].str[0] + "." + test_df["Nachname"].str[0] + "."
test_df["Email"]   = test_df["Vorname"].str.lower() + "@firma.de"
print(test_df)
# LOESUNG: .str.split(), .str[0], .str.lower() = Pandas String-Accessor.

# AUFGABE 10: Vollstaendige Analyse
print("\nAUFGABE 10: Zusammenfassung")
summary = pd.DataFrame({
    "Anzahl":   df.groupby("Abt")["ID"].count(),
    "Ø Gehalt": df.groupby("Abt")["Gehalt"].mean().round(0),
    "Ø Erf":    df.groupby("Abt")["Erfahrung"].mean().round(1),
    "% Note A": (df.groupby("Abt")["Bewertung"].apply(lambda x:(x=="A").mean())*100).round(1),
    "Ø Bonus":  df.groupby("Abt")["Bonus"].mean().round(0),
})
print(summary.sort_values("Ø Gehalt", ascending=False))
summary.to_csv("abteilungsanalyse.csv")
plt.close("all")
print("\nabteilungsanalyse.csv gespeichert.")
# LOESUNG: Alles kombiniert: groupby + apply + agg + to_csv.

print("\n" + "=" * 60)
print("Tag 5 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
