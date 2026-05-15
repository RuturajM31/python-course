# woche3_mini4_fortgeschrittene_zeitreihen_forecast.py
# MINIPROJEKT WOCHE 3 - Fortgeschrittene (2/2)
# Titel: Zeitreihen-Analyse & Forecast-Vergleich
# Thema: Dekomposition + Holt-Winters + ARIMA-Vorbereitung + Report (Lerntage 13-15)
# Ausfuehren in Spyder: F5
# Benoetigt: pip install statsmodels pandas matplotlib numpy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from datetime import datetime

print("=" * 60)
print("MINIPROJEKT W3/4 (Fortgeschrittene): Zeitreihen-Forecast")
print("=" * 60)
np.random.seed(42)

# --- SCHRITT 1: Realistische Absatzzeitreihe simulieren ---
print("\n1) Erzeuge Absatz-Zeitreihe (3 Jahre monatlich)...")

n_monate = 36
datum    = pd.date_range("2022-01-01", periods=n_monate, freq="MS")

# Trend + Saison + Zyklik + Rauschen
trend    = np.linspace(1000, 1600, n_monate)
saison   = 200 * np.sin(2*np.pi*np.arange(n_monate)/12 - np.pi/2)  # Peak im Sommer
zyklik   = 80  * np.sin(2*np.pi*np.arange(n_monate)/24)
rauschen = np.random.normal(0, 40, n_monate)

# Ausreisser einfuegen (z.B. Corona-Einbruch, Promo-Peak)
sondereffekte = np.zeros(n_monate)
sondereffekte[15] = -300   # Einbruch
sondereffekte[28] =  250   # Aktionspeak

absatz = (trend + saison + zyklik + rauschen + sondereffekte).clip(100).round(0)
ts = pd.Series(absatz, index=datum, name="Absatz")

print(ts.to_string())
ts.to_csv("zeitreihe_absatz.csv")

# --- SCHRITT 2: Explorative Analyse ---
print("\n2) Explorative Analyse:")
print(f"   Perioden:          {len(ts)}")
print(f"   Mittelwert:        {ts.mean():.0f}")
print(f"   Trend (Anfang):    {ts.iloc[:6].mean():.0f}  ->  Ende: {ts.iloc[-6:].mean():.0f}")
print(f"   Saisonale Ampli.:  {ts.max()-ts.min():.0f}")
print(f"   Ausreisser (<500): {(ts<500).sum()}")

# ADF-Stationaritaetstest
adf_res = adfuller(ts)
print(f"\n   ADF-Test:")
print(f"     Statistik: {adf_res[0]:.4f}")
print(f"     p-Wert:    {adf_res[1]:.4f}  -> {'Stationaer' if adf_res[1]<0.05 else 'NICHT stationaer'}")

diff_ts = ts.diff().dropna()
adf_diff = adfuller(diff_ts)
print(f"   Nach Differenzierung: p={adf_diff[1]:.4f} -> {'Stationaer' if adf_diff[1]<0.05 else 'nicht stationaer'}")

# --- SCHRITT 3: Seasonal Decomposition ---
print("\n3) Seasonal Decompose...")
result = seasonal_decompose(ts, model="additive", period=12)

# --- SCHRITT 4: Drei Forecast-Modelle ---
print("\n4) Trainiere Forecast-Modelle...")

TRAIN_N = 30
FORECAST_N = 6
train = ts.iloc[:TRAIN_N]
test  = ts.iloc[TRAIN_N:]

# Modell A: Simple Exponential Smoothing (Basis)
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
m_ses   = SimpleExpSmoothing(train).fit(optimized=True)
f_ses   = m_ses.forecast(FORECAST_N)

# Modell B: Holt (Trend, keine Saison)
from statsmodels.tsa.holtwinters import Holt
m_holt  = Holt(train).fit(optimized=True)
f_holt  = m_holt.forecast(FORECAST_N)

# Modell C: Holt-Winters (Trend + Saison)
m_hw    = ExponentialSmoothing(train, trend="add", seasonal="add", seasonal_periods=12).fit()
f_hw    = m_hw.forecast(FORECAST_N)

def mae(actual, predicted):
    return np.mean(np.abs(actual.values - predicted.values))

def mape(actual, predicted):
    return np.mean(np.abs((actual.values - predicted.values) / actual.values)) * 100

print(f"\n   {'Modell':<20} {'MAE':>8} {'MAPE':>8}")
print(f"   {'-'*38}")
for name, fcast in [("SES", f_ses), ("Holt", f_holt), ("Holt-Winters", f_hw)]:
    print(f"   {name:<20} {mae(test,fcast):>8.1f} {mape(test,fcast):>7.2f}%")

bestes_modell = "Holt-Winters"
bester_fcast  = f_hw

# --- SCHRITT 5: 12-Monats-Ausblick ---
print("\n5) 12-Monats-Ausblick (Holt-Winters)...")
m_final   = ExponentialSmoothing(ts, trend="add", seasonal="add", seasonal_periods=12).fit()
forecast12= m_final.forecast(12)
konfidenz = forecast12.std() * 1.96

print(f"   Monat | Forecast | 95%-CI")
for d, v in forecast12.items():
    print(f"   {d.strftime('%b %Y'):>10} | {v:>8.0f} | {v-konfidenz:.0f} - {v+konfidenz:.0f}")

# --- SCHRITT 6: Grosses Dashboard ---
print("\n6) Erstelle Report-Dashboard...")
fig = plt.figure(figsize=(15, 12))
fig.suptitle(f"Zeitreihen-Forecast Report  |  Generiert: {datetime.now().strftime('%d.%m.%Y %H:%M')}",
             fontsize=14, fontweight="bold")
gs = gridspec.GridSpec(3, 2, figure=fig, hspace=0.45, wspace=0.3)

# Plot 1: Original + Decomposition
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(ts.index, ts.values, "o-", lw=1.5, ms=4, color="steelblue", label="Absatz (original)")
ax1.plot(result.trend.index, result.trend.values, lw=2.5, color="red", alpha=0.8, label="Trend")
ax1.fill_between(ts.index,
    ts.values - result.resid.fillna(0).abs(),
    ts.values + result.resid.fillna(0).abs(),
    alpha=0.1, color="steelblue")
ax1.axvline(ts.index[TRAIN_N], color="orange", lw=2, linestyle="--", label="Train/Test Split")
ax1.set_title("Originaldaten mit Trend"); ax1.set_ylabel("Absatz (Einh.)")
ax1.legend(fontsize=9); ax1.grid(alpha=0.3)

# Plot 2: Saisonkomponente
ax2 = fig.add_subplot(gs[1, 0])
ax2.bar(result.seasonal.index, result.seasonal.values,
        color=["tomato" if v<0 else "seagreen" for v in result.seasonal.values],
        alpha=0.8, width=25)
ax2.axhline(0, color="black", lw=0.8)
ax2.set_title("Saisonkomponente"); ax2.set_ylabel("Abweichung"); ax2.grid(alpha=0.3)

# Plot 3: Modellvergleich
ax3 = fig.add_subplot(gs[1, 1])
ax3.plot(train.index, train.values, "o-", color="steelblue", lw=1.5, ms=3, label="Training")
ax3.plot(test.index,  test.values,  "o-", color="black",     lw=2,   ms=4, label="Tatsaechlich")
ax3.plot(f_ses.index,  f_ses.values,  "--", color="orange",  lw=1.5, label=f"SES (MAE={mae(test,f_ses):.0f})")
ax3.plot(f_holt.index, f_holt.values, "--", color="purple",  lw=1.5, label=f"Holt (MAE={mae(test,f_holt):.0f})")
ax3.plot(f_hw.index,   f_hw.values,   "--", color="tomato",  lw=2.5, label=f"HW (MAE={mae(test,f_hw):.0f})")
ax3.set_title("Modellvergleich (Test-Set)"); ax3.legend(fontsize=8); ax3.grid(alpha=0.3)

# Plot 4: 12-Monats-Ausblick
ax4 = fig.add_subplot(gs[2, 0])
ax4.plot(ts.index[-12:], ts.values[-12:], "o-", color="steelblue", lw=2, label="Letztes Jahr")
ax4.plot(forecast12.index, forecast12.values, "s--", color="tomato", lw=2.5, ms=6, label="Forecast 12M")
ax4.fill_between(forecast12.index,
    forecast12.values - konfidenz,
    forecast12.values + konfidenz,
    alpha=0.2, color="tomato", label="95% KI")
ax4.set_title("12-Monats-Forecast (Holt-Winters)")
ax4.legend(fontsize=9); ax4.set_ylabel("Absatz"); ax4.grid(alpha=0.3)

# Plot 5: ACF
ax5 = fig.add_subplot(gs[2, 1])
plot_acf(diff_ts, lags=18, ax=ax5, alpha=0.05)
ax5.set_title("ACF (differenziert)")

plt.savefig("forecast_report.png", dpi=120, bbox_inches="tight")
plt.show()
plt.close("all")

# --- Abschlussbericht ---
print("\n" + "=" * 60)
print("FORECAST-REPORT ZUSAMMENFASSUNG")
print(f"   Datenpunkte:       {len(ts)}")
print(f"   Bestes Modell:     {bestes_modell}")
print(f"   MAE:               {mae(test, bester_fcast):.1f}")
print(f"   MAPE:              {mape(test, bester_fcast):.2f}%")
print(f"   Forecast-Mittel:   {forecast12.mean():.0f}")
print(f"   Erwartetes Wachst: {(forecast12.mean()/ts.mean()-1)*100:.1f}%")
print("Gespeichert: zeitreihe_absatz.csv, forecast_report.png")
print("=" * 60)
print("Miniprojekt W3/4 abgeschlossen!")
print("=" * 60)
