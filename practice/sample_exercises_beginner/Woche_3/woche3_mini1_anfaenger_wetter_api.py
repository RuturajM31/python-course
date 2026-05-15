# woche3_mini1_anfaenger_wetter_api.py
# MINIPROJEKT WOCHE 3 - Anfaenger (1/2)
# Titel: Wetter-Dashboard mit Open-Meteo API
# Thema: REST-API + Pandas + Matplotlib (Lerntage 11-13)
# Ausfuehren in Spyder: F5
# Benoetigt: pip install requests pandas matplotlib

import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date, timedelta

print("=" * 60)
print("MINIPROJEKT W3/1 (Anfaenger): Wetter-Dashboard")
print("=" * 60)

# --- KONFIGURATION ---
# Muenchen als Beispielstadt (kostenlose API, kein Key noetig)
LAT, LON = 48.1372, 11.5755
STADT     = "Muenchen"
TAGE_RUECKBLICK = 14

ende   = date.today()
start  = ende - timedelta(days=TAGE_RUECKBLICK)

# --- SCHRITT 1: Daten von Open-Meteo API laden ---
print(f"\n1) Lade Wetterdaten fuer {STADT} ({start} bis {ende})...")
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude":  LAT,
    "longitude": LON,
    "daily": [
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "windspeed_10m_max",
    ],
    "start_date": str(start),
    "end_date":   str(ende),
    "timezone":   "Europe/Berlin",
}

try:
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    daten = resp.json()["daily"]
    print("   API-Aufruf erfolgreich!")
except Exception as e:
    print(f"   API-Fehler: {e}")
    print("   Verwende Simulationsdaten...")
    import numpy as np
    np.random.seed(7)
    datumsreihe = pd.date_range(start, ende)
    daten = {
        "time":                [str(d.date()) for d in datumsreihe],
        "temperature_2m_max":  (18 + np.random.randn(len(datumsreihe))*4).tolist(),
        "temperature_2m_min":  (10 + np.random.randn(len(datumsreihe))*3).tolist(),
        "precipitation_sum":   (np.random.exponential(1.5, len(datumsreihe))).tolist(),
        "windspeed_10m_max":   (15 + np.random.randn(len(datumsreihe))*5).tolist(),
    }

# --- SCHRITT 2: Daten in DataFrame umwandeln ---
print("\n2) Daten aufbereiten...")
df = pd.DataFrame(daten)
df["time"]   = pd.to_datetime(df["time"])
df.columns   = ["Datum","TempMax","TempMin","Niederschlag","Wind"]
df["TempMittel"] = ((df["TempMax"] + df["TempMin"]) / 2).round(1)
df["Wochentag"]  = df["Datum"].dt.strftime("%a")
df = df.set_index("Datum")

print(df.round(1).to_string())

# --- SCHRITT 3: Statistische Zusammenfassung ---
print("\n3) Statistik:")
print(f"   Temperatur Max:   {df['TempMax'].max():.1f}°C am {df['TempMax'].idxmax().strftime('%d.%m.')}")
print(f"   Temperatur Min:   {df['TempMin'].min():.1f}°C am {df['TempMin'].idxmin().strftime('%d.%m.')}")
print(f"   Ø Temperatur:     {df['TempMittel'].mean():.1f}°C")
print(f"   Gesamt-Regen:     {df['Niederschlag'].sum():.1f} mm")
print(f"   Regentage:        {(df['Niederschlag'] > 0.5).sum()}")
print(f"   Max Windgeschw.:  {df['Wind'].max():.1f} km/h")

# --- SCHRITT 4: Dashboard-Plot ---
print("\n4) Erstelle Dashboard...")
fig, axes = plt.subplots(3, 1, figsize=(11, 9), sharex=True)
fig.suptitle(f"Wetter-Dashboard {STADT}  |  {start.strftime('%d.%m.')} – {ende.strftime('%d.%m.%Y')}",
             fontsize=13, fontweight="bold")

# Teilplot 1: Temperatur
ax1 = axes[0]
ax1.fill_between(df.index, df["TempMin"], df["TempMax"],
                 alpha=0.25, color="tomato", label="Min-Max Bereich")
ax1.plot(df.index, df["TempMittel"], "o-", color="tomato",
         lw=2, ms=5, label="Ø Temperatur")
ax1.axhline(df["TempMittel"].mean(), color="darkred",
            lw=1, linestyle="--", alpha=0.6, label="Perioden-Mittel")
ax1.set_ylabel("Temperatur (°C)")
ax1.legend(fontsize=8); ax1.grid(alpha=0.3)

# Teilplot 2: Niederschlag
ax2 = axes[1]
farben = ["steelblue" if r > 0.5 else "lightblue" for r in df["Niederschlag"]]
ax2.bar(df.index, df["Niederschlag"], color=farben, width=0.7)
ax2.axhline(1.0, color="navy", lw=1, linestyle="--", alpha=0.5)
ax2.set_ylabel("Niederschlag (mm)")
ax2.grid(axis="y", alpha=0.3)

# Teilplot 3: Wind
ax3 = axes[2]
ax3.fill_between(df.index, 0, df["Wind"], alpha=0.4, color="teal")
ax3.plot(df.index, df["Wind"], "s-", color="teal", lw=1.5, ms=4)
ax3.set_ylabel("Wind max (km/h)")
ax3.grid(alpha=0.3)
ax3.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m."))
ax3.xaxis.set_major_locator(mdates.DayLocator(interval=2))
plt.xticks(rotation=30, ha="right")

plt.tight_layout()
plt.savefig("wetter_dashboard.png", dpi=120)
plt.show()

# --- SCHRITT 5: CSV-Export ---
df.round(2).to_csv("wetterdaten.csv")
print("\n5) Gespeichert: wetter_dashboard.png, wetterdaten.csv")

print("\n" + "=" * 60)
print("Miniprojekt W3/1 abgeschlossen!")
print("=" * 60)
