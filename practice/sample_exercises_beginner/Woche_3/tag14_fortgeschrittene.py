# tag14_fortgeschrittene.py
# Lerntag 14 - Zeitreihenanalyse: Fortgeschrittene Methoden
# Thema: Dekomposition, EWMA, ADF-Test, Holt-Winters-Forecast, ACF/PACF
# Ausfuehren in Spyder: F5
# Benoetigt: pip install statsmodels

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

print("=" * 60)
print("LERNTAG 14 - Zeitreihen fortgeschritten")
print("=" * 60)
np.random.seed(42)

n     = 365 * 2
datum = pd.date_range("2022-01-01", periods=n, freq="D")
trend   = np.linspace(200, 350, n)
saison  = 50 * np.sin(2*np.pi*np.arange(n)/365)
rauschen= np.random.randn(n) * 15
ts = pd.Series((trend+saison+rauschen).round(2), index=datum, name="Umsatz")

# AUFGABE 1: Seasonal Decompose
print("\nAUFGABE 1: Seasonal Decompose")
result = seasonal_decompose(ts, model="additive", period=365)
fig, axes = plt.subplots(4,1,figsize=(11,9),sharex=True)
for ax, comp, name in zip(axes,
    [ts, result.trend, result.seasonal, result.resid],
    ["Original","Trend","Saison","Residuen"]):
    ax.plot(comp, lw=1, color="steelblue")
    ax.set_ylabel(name); ax.grid(alpha=0.3)
axes[0].set_title("Zeitreihen-Dekomposition (Trend + Saison + Residuen)")
plt.tight_layout(); plt.savefig("plot_14f_01.png", dpi=100); plt.show()
# LOESUNG: seasonal_decompose trennt Zeitreihe in Trend, Saison und Residuen.

# AUFGABE 2: EWMA
print("\nAUFGABE 2: EWMA")
fig, ax = plt.subplots(figsize=(11,4))
ax.plot(ts.index, ts, alpha=0.25, color="gray", lw=0.7, label="Original")
for span, col in [(7,"steelblue"),(30,"navy"),(90,"red")]:
    ax.plot(ts.ewm(span=span).mean(), lw=1.5, color=col, label=f"EWMA {span}T")
ax.set_title("Exponentiell gewichteter Durchschnitt (EWMA)")
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.savefig("plot_14f_02.png", dpi=100); plt.show()
# LOESUNG: ewm(span=n).mean() gewichtet juengere Werte staerker als aeltere.

# AUFGABE 3: ACF und PACF
print("\nAUFGABE 3: ACF/PACF")
ts_w = ts.resample("W").mean()
fig, (ax1,ax2) = plt.subplots(2,1,figsize=(11,6))
plot_acf( ts_w.dropna(), lags=52, ax=ax1, title="ACF (Wochenwerte, lags=52)")
plot_pacf(ts_w.dropna(), lags=26, ax=ax2, title="PACF")
plt.tight_layout(); plt.savefig("plot_14f_03.png", dpi=100); plt.show()
# LOESUNG: ACF-Peak bei lag=52 bestaetigt Jahressaisonalitaet.

# AUFGABE 4: Holt-Winters Forecast
print("\nAUFGABE 4: Holt-Winters")
ts_m  = ts.resample("ME").mean()
train = ts_m[:-6]; test = ts_m[-6:]
model = ExponentialSmoothing(train, trend="add", seasonal="add", seasonal_periods=12)
fit   = model.fit()
fcast = fit.forecast(6)
mae   = (test - fcast).abs().mean()
print(f"MAE: {mae:.2f} EUR")
fig, ax = plt.subplots(figsize=(11,4))
ax.plot(train.index, train, label="Training",    color="steelblue")
ax.plot(test.index,  test,  label="Tatsaechlich",color="green",  lw=2)
ax.plot(fcast.index, fcast, label="Forecast",    color="red", linestyle="--", lw=2)
ax.set_title(f"Holt-Winters Forecast 6 Monate (MAE={mae:.1f})")
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.savefig("plot_14f_04.png", dpi=100); plt.show()
# LOESUNG: ExponentialSmoothing(trend='add', seasonal='add') = Holt-Winters.

# AUFGABE 5: ADF-Stationaritaetstest
print("\nAUFGABE 5: ADF-Test")
res = adfuller(ts.dropna())
print(f"ADF-Statistik: {res[0]:.4f}")
print(f"p-Wert:        {res[1]:.4f}")
print(f"Stationaer?    {'Nein' if res[1]>0.05 else 'Ja'}")
diff1 = ts.diff().dropna()
res2  = adfuller(diff1)
print(f"Nach 1. Diff.: p={res2[1]:.4f} -> {'Stationaer' if res2[1]<=0.05 else 'Nein'}")
# LOESUNG: p < 0.05 = stationaer. Differenzierung schafft Stationaritaet.

# AUFGABE 6: Saisonaler Index
print("\nAUFGABE 6: Saisonaler Index")
df2 = ts.to_frame()
df2["Monat"] = df2.index.month
gesamt_mittel = df2["Umsatz"].mean()
sais = df2.groupby("Monat")["Umsatz"].mean() / gesamt_mittel
monate = ["Jan","Feb","Mrz","Apr","Mai","Jun","Jul","Aug","Sep","Okt","Nov","Dez"]
sais.index = monate
print(sais.round(3).to_string())
# LOESUNG: Monatsmittel / Gesamtmittel = saisonaler Faktor.

# AUFGABE 7: Jaehrliche Wachstumsrate
print("\nAUFGABE 7: Wachstum")
ts_j = ts.resample("YE").sum()
for j, w in zip(ts_j.index.year[1:], ts_j.pct_change().dropna()*100):
    print(f"  {j}: {w:+.1f}%")

# AUFGABE 8: Rollende Korrelation
print("\nAUFGABE 8: Rollende Korrelation")
ts2 = ts * 0.6 + pd.Series(np.random.randn(n)*30, index=datum)
roll_corr = ts.rolling(90).corr(ts2)
fig, ax = plt.subplots(figsize=(11,3))
ax.plot(roll_corr.index, roll_corr, color="purple", lw=1)
ax.axhline(0, color="black", lw=0.5); ax.set_ylim(-1,1)
ax.set_title("Rollende Korrelation (90 Tage)"); ax.grid(alpha=0.3)
plt.tight_layout(); plt.savefig("plot_14f_08.png", dpi=100); plt.show()

# AUFGABE 9: Z-Score Normierung
print("\nAUFGABE 9: Z-Score")
ts_z = (ts - ts.mean()) / ts.std()
print(f"Mittelwert (normiert): {ts_z.mean():.4f}")
print(f"Std (normiert):        {ts_z.std():.4f}")
print(f"Ausreisser |z|>2.5:    {(ts_z.abs()>2.5).sum()}")

# AUFGABE 10: Monatsbericht
print("\nAUFGABE 10: Monatsbericht")
bericht = pd.DataFrame({
    "Monat":      monate,
    "Mittel_EUR": df2.groupby("Monat")["Umsatz"].mean().round(1).values,
    "Sais_Index": sais.values.round(3),
})
print(bericht.to_string(index=False))
bericht.to_csv("zeitreihe_bericht.csv", index=False)
plt.close("all")
print("Gespeichert: zeitreihe_bericht.csv + Plots")

print("\n" + "=" * 60)
print("Tag 14 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
