# tag07_fortgeschrittene.py
# Lerntag 7 - Pandas: Fortgeschrittene Techniken
# Thema: Merge, Pivot, MultiIndex, Rolling, DatetimeIndex
# Ausfuehren in Spyder: F5

import pandas as pd
import numpy as np

print("=" * 60)
print("LERNTAG 7 - Pandas fuer Fortgeschrittene")
print("=" * 60)

# AUFGABE 1: merge
print("\nAUFGABE 1: merge")
df_m = pd.DataFrame({"ID":[1,2,3,4,5],"Name":["Anna","Ben","Cara","Dan","Eva"],"AbtID":[10,20,10,30,20]})
df_a = pd.DataFrame({"AbtID":[10,20,30],"Abteilung":["IT","HR","Finance"]})
print(pd.merge(df_m, df_a, on="AbtID", how="left"))
# LOESUNG: merge(left, right, on=key, how="left/inner/outer/right")

# AUFGABE 2: Pivot Table
print("\nAUFGABE 2: Pivot Table")
np.random.seed(7)
df_vk = pd.DataFrame({
    "Quartal": ["Q1","Q1","Q2","Q2","Q3","Q3","Q4","Q4"],
    "Produkt": ["A","B","A","B","A","B","A","B"],
    "Umsatz":  np.random.randint(50000,150000,8)
})
pt = df_vk.pivot_table(values="Umsatz", index="Quartal",
                        columns="Produkt", aggfunc="sum", margins=True)
print(pt)
# LOESUNG: pivot_table(values, index, columns, aggfunc) - wie Excel-Pivot.

# AUFGABE 3: MultiIndex
print("\nAUFGABE 3: MultiIndex")
idx = pd.MultiIndex.from_arrays([["Nord","Nord","Sued","Sued"],["Q1","Q2","Q1","Q2"]],
                                  names=["Region","Quartal"])
df_mi = pd.DataFrame({"Umsatz":[120,145,98,132],"Kosten":[80,95,65,88]}, index=idx)
print(df_mi)
print("Nord gesamt:", df_mi.loc["Nord"]["Umsatz"].sum())
# LOESUNG: MultiIndex erlaubt hierarchische Indizierung.

# AUFGABE 4: DatetimeIndex + resample
print("\nAUFGABE 4: resample")
np.random.seed(3)
datum = pd.date_range("2024-01-01", periods=90, freq="D")
df_ts = pd.DataFrame({"Umsatz": np.random.randint(1000,5000,90)}, index=datum)
monatlich = df_ts.resample("ME").agg({"Umsatz":["sum","mean","count"]})
monatlich.columns = ["Summe","Mittel","Tage"]
print(monatlich)
# LOESUNG: resample("ME") = Monatsende. agg() mehrere Funktionen.

# AUFGABE 5: Rolling Window
print("\nAUFGABE 5: Rolling Window")
df_ts["MA7"]  = df_ts["Umsatz"].rolling(7).mean().round(0)
df_ts["MA30"] = df_ts["Umsatz"].rolling(30).mean().round(0)
print(df_ts.tail(5))
# LOESUNG: rolling(n).mean() = gleitender Durchschnitt ueber n Perioden.

# AUFGABE 6: .str Methoden
print("\nAUFGABE 6: str-Methoden")
df_str = pd.DataFrame({"Email":["anna@example.com","  BEN@GMAIL.COM  ","cara@test.de","invalid"]})
df_str["clean"]  = df_str["Email"].str.strip().str.lower()
df_str["domain"] = df_str["clean"].str.extract(r"@(.+)")
df_str["ok"]     = df_str["clean"].str.contains(r"^[\w.]+@[\w.]+\.\w{2,}$", na=False)
print(df_str)
# LOESUNG: .str.strip()/.lower()/.extract()/.contains() auf ganzen Serien.

# AUFGABE 7: cut und qcut
print("\nAUFGABE 7: cut + qcut")
np.random.seed(5)
df_n = pd.DataFrame({"Punkte": np.random.randint(0,101,20)})
df_n["Note"]    = pd.cut(df_n["Punkte"],bins=[0,50,65,80,90,101],
                          labels=["Nicht best.","Ausreichend","Befriedigend","Gut","Sehr gut"],right=False)
df_n["Quartil"] = pd.qcut(df_n["Punkte"], q=4, labels=["Q1","Q2","Q3","Q4"])
print(df_n.head(8))
print(df_n["Note"].value_counts().sort_index())
# LOESUNG: cut = feste Grenzen. qcut = gleich grosse Gruppen.

# AUFGABE 8: query
print("\nAUFGABE 8: query")
df2 = pd.DataFrame({"Name":["Anna","Ben","Cara","Dan","Eva"],
                    "Alter":[25,32,28,41,19],"Gehalt":[3200,4500,3800,5200,2900],
                    "Stadt":["Berlin","Hamburg","Berlin","Muenchen","Hamburg"]})
print(df2.query("Alter < 35 and Gehalt > 3000 and Stadt != 'Hamburg'"))
# LOESUNG: query() akzeptiert SQL-aehnliche Strings.

# AUFGABE 9: melt (Wide -> Long)
print("\nAUFGABE 9: melt")
df_w = pd.DataFrame({"Land":["DE","AT","CH"],"2022":[450,120,95],"2023":[480,130,102],"2024":[510,140,108]})
df_l = df_w.melt(id_vars="Land", var_name="Jahr", value_name="Wert")
print(df_l)
# LOESUNG: melt(id_vars=fixe_spalten) transformiert Spalten zu Zeilen.

# AUFGABE 10: Method Chaining
print("\nAUFGABE 10: Method Chaining")
ergebnis = (df2
    .assign(Jahresgehalt=lambda x: x["Gehalt"]*12)
    .query("Alter >= 25")
    .sort_values("Jahresgehalt", ascending=False)
    .reset_index(drop=True)[["Name","Alter","Jahresgehalt"]])
print(ergebnis)
# LOESUNG: Pandas-Methoden sind verkettbar - jede gibt ein neues DataFrame zurueck.

print("\n" + "=" * 60)
print("Tag 7 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
