# tag15_fortgeschrittene.py
# Lerntag 15 - Abschluss: End-to-End Pipeline Fortgeschrittene
# Thema: Regex + Datetime + Feature Engineering + ML + Bericht
# Ausfuehren in Spyder: F5

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
import re
from datetime import date

sns.set_theme(style="whitegrid")
np.random.seed(42)

print("=" * 60)
print("LERNTAG 15 - Fortgeschrittene End-to-End Pipeline")
print("=" * 60)

# AUFGABE 1: Rohdaten simulieren (wie aus API)
print("\nAUFGABE 1: Rohdaten (API-Simulation)")
n = 500
raw = [{
    "id":             i,
    "hire_date":      str(date(2010,1,1) + pd.Timedelta(days=int(np.random.randint(0,5000)))),
    "salary_raw":     f"EUR {int(np.random.normal(3500,900)):,}".replace(",",".") + ",00",
    "department":     np.random.choice(["IT","HR","Finance","Sales","Logistik"]),
    "age":            int(np.random.randint(22,62)),
    "experience":     int(np.random.randint(0,35)),
    "performance":    round(np.random.beta(5,2)*100, 1)
} for i in range(1, n+1)]
print(f"Datensaetze: {len(raw)}")
print(f"Beispiel:    {raw[0]}")
# LOESUNG: Typische API-JSON-Struktur mit gemischten Datentypen simulieren.

# AUFGABE 2: Regex-Bereinigung
print("\nAUFGABE 2: Regex-Parsing")
def parse_salary(s):
    m = re.search(r"EUR\s*([\d.]+)", s)
    return float(m.group(1).replace(".","")) if m else np.nan

df = pd.DataFrame(raw)
df["salary"]    = df["salary_raw"].apply(parse_salary)
df["hire_date"] = pd.to_datetime(df["hire_date"])
df["tenure"]    = ((pd.Timestamp.today() - df["hire_date"]).dt.days / 365).round(1)
print(f"Parsing OK: {df['salary'].notna().sum()}/{n}")
print(df[["salary","hire_date","tenure"]].head(3).to_string(index=False))
# LOESUNG: re.search() extrahiert Zahl aus Waehrungsstring.

# AUFGABE 3: Feature Engineering
print("\nAUFGABE 3: Feature Engineering")
df["salary"]   += df["experience"] * 100 + df["performance"] * 20
df["salary"]    = df["salary"].round(0)
df["exp_perf"]  = df["experience"] * df["performance"]
df_enc = pd.get_dummies(df[["salary","age","experience","performance",
                              "tenure","exp_perf","department"]], drop_first=True)
print(f"Feature-Matrix: {df_enc.shape[1]} Spalten")
# LOESUNG: get_dummies() kodiert kategoriale Variable als 0/1-Spalten.

# AUFGABE 4: Lineare Regression
print("\nAUFGABE 4: Lineare Regression")
X = df_enc.drop("salary", axis=1); y = df_enc["salary"]
X_tr,X_te,y_tr,y_te = train_test_split(X,y,test_size=0.2,random_state=42)
scaler = StandardScaler()
X_tr_s = scaler.fit_transform(X_tr); X_te_s = scaler.transform(X_te)
model  = LinearRegression().fit(X_tr_s, y_tr)
y_pred = model.predict(X_te_s)
print(f"MAE: {mean_absolute_error(y_te,y_pred):.0f} EUR")
print(f"R2:  {r2_score(y_te,y_pred):.3f}")
# LOESUNG: StandardScaler normiert Features. LinearRegression().fit() trainiert.

# AUFGABE 5: Vorhersage-Plot
print("\nAUFGABE 5: Plot")
fig, axes = plt.subplots(1,2,figsize=(11,4))
axes[0].scatter(y_te, y_pred, alpha=0.4, color="steelblue", s=20)
lim = [y_te.min(), y_te.max()]
axes[0].plot(lim, lim, "r--", lw=1)
axes[0].set_title("Vorhersage vs. Realitaet")
axes[0].set_xlabel("Tatsaechlich EUR"); axes[0].set_ylabel("Vorhergesagt EUR")
residuen = y_te - y_pred
sns.histplot(residuen, bins=30, kde=True, color="tomato", ax=axes[1])
axes[1].axvline(0, color="navy", lw=1.5); axes[1].set_title("Residuenverteilung")
plt.tight_layout(); plt.savefig("plot_15f_05.png", dpi=100); plt.show()

# AUFGABE 6: Feature Importance
print("\nAUFGABE 6: Feature Importance")
fi = pd.Series(np.abs(model.coef_), index=X.columns).sort_values(ascending=False)
print(fi.head(6).round(2))
fig, ax = plt.subplots(figsize=(8,4))
fi.head(8).plot(kind="barh", ax=ax, color="steelblue"); ax.invert_yaxis()
ax.set_title("Feature Importance (|Koeffizient|)")
plt.tight_layout(); plt.savefig("plot_15f_06.png", dpi=100); plt.show()
# LOESUNG: Absolute Koeffizienten nach StandardScaler = Wichtigkeit.

# AUFGABE 7: Einstellungszeitreihe
print("\nAUFGABE 7: Zeitreihe")
ts_hire = df.set_index("hire_date").resample("QE").size()
fig, ax = plt.subplots(figsize=(11,3))
ax.bar(ts_hire.index, ts_hire.values, width=60, color="steelblue", alpha=0.7)
ax.set_title("Einstellungen pro Quartal"); ax.set_ylabel("Anzahl"); ax.grid(axis="y",alpha=0.3)
plt.tight_layout(); plt.savefig("plot_15f_07.png", dpi=100); plt.show()

# AUFGABE 8: Abteilungs-Dashboard
print("\nAUFGABE 8: Abteilungsvergleich")
abt = df.groupby("department").agg(
    Anzahl=("id","count"),
    Gehalt=("salary","mean"),
    Performance=("performance","mean"),
    Erfahrung=("experience","mean")
).round(1)
print(abt.sort_values("Gehalt", ascending=False))

# AUFGABE 9: Korrelations-Heatmap
print("\nAUFGABE 9: Korrelation")
corr = df[["salary","age","experience","performance","tenure"]].corr()
fig, ax = plt.subplots(figsize=(6,5))
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, ax=ax)
ax.set_title("Korrelationsmatrix")
plt.tight_layout(); plt.savefig("plot_15f_09.png", dpi=100); plt.show()

# AUFGABE 10: Abschlussbericht
print("\nAUFGABE 10: Gesamtbericht")
df.to_csv("pipeline_ergebnis.csv", index=False)
print("=" * 50)
print("PIPELINE-ZUSAMMENFASSUNG")
print(f"Datensaetze:          {len(df)}")
print(f"Feature-Spalten:      {df_enc.shape[1]}")
print(f"Modell R2:            {r2_score(y_te,y_pred):.3f}")
print(f"MAE:                  {mean_absolute_error(y_te,y_pred):.0f} EUR")
print(f"Beste Abt. (Gehalt):  {abt['Gehalt'].idxmax()}")
print(f"Wichtigster Feature:  {fi.idxmax()}")
plt.close("all")
print("Gespeichert: pipeline_ergebnis.csv + alle Plots")

print("\n" + "=" * 60)
print("Tag 15 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("KURS VOLLSTAENDIG ABGESCHLOSSEN - Herzlichen Glueckwunsch!")
print("=" * 60)
