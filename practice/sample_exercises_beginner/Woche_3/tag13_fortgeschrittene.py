# tag13_fortgeschrittene.py
# Lerntag 13 - Datum und Zeit: Fortgeschrittene Techniken
# Thema: Zeitzonen (pytz), DatetimeIndex, Zeitreihen, Geschaeftstage, Dekomposition
# Ausfuehren in Spyder: F5

from datetime import datetime, date, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytz

print("=" * 60)
print("LERNTAG 13 - Datum/Zeit fuer Fortgeschrittene")
print("=" * 60)

# AUFGABE 1: Zeitzonen mit pytz
print("\nAUFGABE 1: Zeitzonen")
utc    = pytz.utc
berlin = pytz.timezone("Europe/Berlin")
ny     = pytz.timezone("America/New_York")
jetzt_utc    = datetime.now(utc)
jetzt_berlin = jetzt_utc.astimezone(berlin)
jetzt_ny     = jetzt_utc.astimezone(ny)
for name, dt in [("UTC",jetzt_utc),("Berlin",jetzt_berlin),("New York",jetzt_ny)]:
    print(f"  {name:<10}: {dt.strftime('%Y-%m-%d %H:%M %Z')}")
# LOESUNG: datetime.now(pytz.utc) -> .astimezone(andere_zone) fuer Umrechnung.

# AUFGABE 2: Pandas DatetimeIndex
print("\nAUFGABE 2: DatetimeIndex")
idx = pd.date_range("2024-01-01", "2024-12-31", freq="D")
print(f"Tage 2024:        {len(idx)}")
print(f"Wochentage (Mo-Fr): {(idx.dayofweek < 5).sum()}")
print(f"Monatserste:       {(idx.day == 1).sum()}")
# LOESUNG: .dayofweek, .day, .month usw. fuer vektorisierte Datumsoperationen.

# AUFGABE 3: Zeitreihe + resample
print("\nAUFGABE 3: Zeitreihe")
np.random.seed(42)
df = pd.DataFrame({
    "Temperatur": 10 + 12*np.sin(np.linspace(0,2*np.pi,365)) + np.random.randn(365)*3
}, index=pd.date_range("2024-01-01", periods=365, freq="D"))
monat = df.resample("ME").agg({"Temperatur": ["mean","min","max"]}).round(1)
monat.index = monat.index.strftime("%b")
print(monat)
# LOESUNG: resample("ME").agg() fasst nach Monat-Ende zusammen.

# AUFGABE 4: Geschaeftstage
print("\nAUFGABE 4: Geschaeftstage")
feiertage = [date(2024,1,1),date(2024,4,19),date(2024,10,3),date(2024,12,25)]
bdays = pd.bdate_range("2024-01-01","2024-12-31")
feiertag_idx = pd.DatetimeIndex([pd.Timestamp(d) for d in feiertage])
arbeitstage = bdays.difference(feiertag_idx)
print(f"Arbeitstage 2024 (ohne 4 Feiertage): {len(arbeitstage)}")
# LOESUNG: bdate_range = nur Mo-Fr. .difference() entfernt gegebene Daten.

# AUFGABE 5: Zeitzone in Zeitreihe
print("\nAUFGABE 5: Zeitzone in Zeitreihe")
idx_utc = pd.date_range("2024-06-01", periods=24, freq="h", tz="UTC")
ts_utc  = pd.Series(np.random.randint(100,200,24), index=idx_utc)
ts_ber  = ts_utc.tz_convert("Europe/Berlin")
print("UTC -> Berlin (erste 3 Stunden):")
for u, b, v in zip(ts_utc.index[:3], ts_ber.index[:3], ts_utc.values[:3]):
    print(f"  UTC {u.hour:02d}:00 -> Berlin {b.hour:02d}:00  Wert={v}")
# LOESUNG: .tz_convert() rechnet gesamte Zeitreihe in andere Zeitzone um.

# AUFGABE 6: Rollende Statistiken
print("\nAUFGABE 6: Rolling")
df["MA7"]  = df["Temperatur"].rolling(7,  center=True).mean()
df["MA30"] = df["Temperatur"].rolling(30, center=True).mean()
df["Anomalie"] = df["Temperatur"] - df["MA30"]
print("Groesste Anomalien:")
print(df["Anomalie"].abs().nlargest(5).round(2))
# LOESUNG: rolling(n, center=True) zentriert das Fenster auf den aktuellen Wert.

# AUFGABE 7: Shift und Differenz
print("\nAUFGABE 7: Shift/Diff")
df["Temp_vor1"] = df["Temperatur"].shift(1)
df["Delta_1T"]  = df["Temperatur"].diff(1)
df["Delta_7T"]  = df["Temperatur"].diff(7)
print(df[["Temperatur","Temp_vor1","Delta_1T","Delta_7T"]].iloc[6:11].round(2))
# LOESUNG: shift(n) = Wert n Perioden frueherer. diff(n) = Differenz.

# AUFGABE 8: Plot Zeitreihe mit Moving Averages
print("\nAUFGABE 8: Plot")
fig, ax = plt.subplots(figsize=(11,4))
ax.plot(df.index, df["Temperatur"], alpha=0.35, color="gray",      lw=0.7, label="Tagesmittel")
ax.plot(df.index, df["MA7"],        color="navy",                  lw=1.5, label="MA 7T")
ax.plot(df.index, df["MA30"],       color="darkgreen",             lw=2,   label="MA 30T")
ax.set_title("Temperaturverlauf 2024 mit gleitenden Mittelwerten")
ax.set_ylabel("°C"); ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.savefig("plot_13f_08.png", dpi=100); plt.show()

# AUFGABE 9: Quartalsvergleich
print("\nAUFGABE 9: Quartale")
df["Quartal"] = df.index.quarter
q = df.groupby("Quartal")["Temperatur"].agg(["mean","min","max"]).round(1)
q.index = ["Q1","Q2","Q3","Q4"]
print(q)

# AUFGABE 10: ISO-Wochen-Aggregation
print("\nAUFGABE 10: Wochenaggregation")
df["ISO_Woche"] = df.index.isocalendar().week
wochen = df.groupby("ISO_Woche")["Temperatur"].mean().round(1)
fig, ax = plt.subplots(figsize=(11,3))
ax.bar(wochen.index, wochen.values, color="steelblue", width=0.8)
ax.set_title("Wochenmittel Temperatur 2024"); ax.set_xlabel("KW"); ax.set_ylabel("°C")
ax.grid(axis="y", alpha=0.3); plt.tight_layout()
plt.savefig("plot_13f_10.png", dpi=100); plt.show()
plt.close("all")
print("Plots gespeichert.")

print("\n" + "=" * 60)
print("Tag 13 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
