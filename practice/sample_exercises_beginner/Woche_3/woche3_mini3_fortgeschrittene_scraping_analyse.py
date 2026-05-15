# woche3_mini3_fortgeschrittene_scraping_analyse.py
# MINIPROJEKT WOCHE 3 - Fortgeschrittene (1/2)
# Titel: Web-Scraping Pipeline mit Analyse & Report
# Thema: BeautifulSoup + Regex + Pandas + Visualisierung (Lerntage 11-13)
# Ausfuehren in Spyder: F5
# Benoetigt: pip install requests beautifulsoup4 pandas matplotlib

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from datetime import datetime

print("=" * 60)
print("MINIPROJEKT W3/3 (Fortgeschrittene): Scraping-Pipeline")
print("=" * 60)

# --- SCHRITT 1: Scraping (books.toscrape.com - legale Uebungsseite) ---
print("\n1) Scrape books.toscrape.com (mehrere Seiten)...")

BASIS_URL = "https://books.toscrape.com/catalogue/"
SEITEN    = 5
buecher   = []

STERN_MAP = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5}

def preis_parsen(text):
    m = re.search(r"[\d.]+", text)
    return float(m.group()) if m else np.nan

def scrape_seite(seite_nr):
    url = f"{BASIS_URL}page-{seite_nr}.html"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        artikel = soup.select("article.product_pod")
        ergebnis = []
        for a in artikel:
            titel  = a.h3.a["title"]
            preis  = preis_parsen(a.select_one(".price_color").text)
            sterne = STERN_MAP.get(a.p["class"][1], 0)
            lager  = "In stock" in a.select_one(".availability").text
            ergebnis.append({"Titel":titel,"Preis":preis,"Sterne":sterne,"Lager":lager,"Seite":seite_nr})
        return ergebnis
    except Exception as e:
        print(f"   Seite {seite_nr} Fehler: {e}")
        return []

for s in range(1, SEITEN+1):
    gefunden = scrape_seite(s)
    buecher.extend(gefunden)
    print(f"   Seite {s}: {len(gefunden)} Buecher")

if not buecher:
    print("   Scraping fehlgeschlagen - Simulationsdaten...")
    np.random.seed(99)
    genres = ["Fiction","Mystery","Science","History","Romance","Thriller"]
    buecher = [{
        "Titel":  f"Buch {i:03d}: {''.join(np.random.choice(list('ABCDEFGH'),5))}",
        "Preis":  round(np.random.uniform(5,55),2),
        "Sterne": np.random.randint(1,6),
        "Lager":  np.random.choice([True,False],p=[0.8,0.2]),
        "Seite":  (i//20)+1,
    } for i in range(1,101)]

df = pd.DataFrame(buecher)
print(f"\n   Gesamt: {len(df)} Buecher gescraped")

# --- SCHRITT 2: Datenbereinigung ---
print("\n2) Bereinigung...")
df = df.dropna(subset=["Preis"])
df["Preis_kl"] = pd.cut(df["Preis"],
    bins=[0,10,20,35,100], labels=["<10","10-20","20-35",">35"])
df["Empfehlung"] = (df["Sterne"] >= 4) & (df["Preis"] < 20)
print(df.describe(include="all").loc[["count","mean","min","max"]].T)

# --- SCHRITT 3: Analyse ---
print("\n3) Analyse:")
print(f"   Ø Preis:           {df['Preis'].mean():.2f} GBP")
print(f"   Median Preis:      {df['Preis'].median():.2f} GBP")
print(f"   Top-Rated (>=4*):  {(df['Sterne']>=4).sum()}")
print(f"   Empfehlungen:      {df['Empfehlung'].sum()}  (>=4*, <20 GBP)")
print(f"   Nicht am Lager:    {(~df['Lager']).sum()}")

print("\n   Preis nach Sterne-Bewertung:")
stern_analyse = df.groupby("Sterne").agg(
    Anzahl=("Titel","count"),
    Ø_Preis=("Preis","mean"),
    Min_Preis=("Preis","min"),
).round(2)
print(stern_analyse)

# --- SCHRITT 4: Dashboard ---
print("\n4) Erstelle Report-Dashboard...")
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
fig.suptitle(f"Buchmarkt-Analyse | books.toscrape.com | {datetime.now().strftime('%d.%m.%Y')}",
             fontsize=13, fontweight="bold")

# Oben links: Preisverteilung nach Stern
sterne_farben = {1:"#d73027",2:"#fc8d59",3:"#fee090",4:"#91bfdb",5:"#4575b4"}
for stern, gruppe in df.groupby("Sterne"):
    axes[0,0].hist(gruppe["Preis"], bins=12, alpha=0.6,
                   label=f"{stern}★", color=sterne_farben.get(stern,"gray"))
axes[0,0].set_title("Preisverteilung je Sternebewertung")
axes[0,0].set_xlabel("Preis (GBP)"); axes[0,0].set_ylabel("Anzahl")
axes[0,0].legend(fontsize=8); axes[0,0].grid(alpha=0.3)

# Oben rechts: Ø Preis je Stern (Balken)
stern_analyse["Ø_Preis"].plot(kind="bar", ax=axes[0,1],
    color=[sterne_farben[s] for s in stern_analyse.index], edgecolor="white")
axes[0,1].set_title("Ø Preis je Sternebewertung")
axes[0,1].set_xlabel("Sterne"); axes[0,1].set_ylabel("GBP")
axes[0,1].tick_params(axis="x", rotation=0); axes[0,1].grid(axis="y", alpha=0.3)

# Unten links: Preiskategorien (Pie)
preiskat = df["Preis_kl"].value_counts().sort_index()
axes[1,0].pie(preiskat.values, labels=preiskat.index,
              autopct="%1.1f%%", startangle=90,
              wedgeprops=dict(width=0.6, edgecolor="white"),
              colors=["#4575b4","#91bfdb","#fc8d59","#d73027"])
axes[1,0].set_title("Buecher je Preiskategorie")

# Unten rechts: Empfehlungen vs Nicht-Empfehlungen
emph = pd.Series({
    "Empfohlen\n(>=4★, <20 GBP)": df["Empfehlung"].sum(),
    "Nicht\nempfohlen":           (~df["Empfehlung"]).sum(),
})
axes[1,1].bar(emph.index, emph.values,
              color=["seagreen","tomato"], edgecolor="white", width=0.5)
axes[1,1].set_title("Empfehlungsquote"); axes[1,1].set_ylabel("Anzahl Buecher")
axes[1,1].grid(axis="y", alpha=0.3)
for i, v in enumerate(emph.values):
    axes[1,1].text(i, v+0.5, str(v), ha="center", fontweight="bold")

plt.tight_layout()
plt.savefig("scraping_report.png", dpi=120)
plt.show()

# --- SCHRITT 5: Top-Empfehlungen ausgeben ---
print("\n5) Top-10 Empfehlungen (>=4 Sterne, guenstig):")
top10 = (df[df["Empfehlung"]]
         .sort_values(["Sterne","Preis"], ascending=[False,True])
         .head(10)
         [["Titel","Sterne","Preis","Lager"]])
print(top10.to_string(index=False))

df.to_csv("buecher_analyse.csv", index=False)
plt.close("all")
print("\n   Gespeichert: buecher_analyse.csv, scraping_report.png")
print("\n" + "=" * 60)
print("Miniprojekt W3/3 abgeschlossen!")
print("=" * 60)
