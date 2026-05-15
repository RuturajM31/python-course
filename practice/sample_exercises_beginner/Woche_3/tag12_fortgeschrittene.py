# tag12_fortgeschrittene.py
# Lerntag 12 - Web-Scraping: Fortgeschrittene Techniken
# Thema: Mehrseitiges Scraping, Kategorien, Detailseiten, Regex, Ethics
# Ausfuehren in Spyder: F5

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re, time

sns.set_theme(style="whitegrid")
print("=" * 60)
print("LERNTAG 12 - Web-Scraping fuer Fortgeschrittene")
print("=" * 60)

BASE = "https://books.toscrape.com/"
stern_map = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5}

# AUFGABE 1: Mehrseitiges Scraping (3 Seiten)
print("\nAUFGABE 1: Mehrseitiges Scraping")
def scrape_seite(url):
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    rows = []
    for article in soup.select("article.product_pod"):
        rows.append({
            "titel":  article.h3.a["title"],
            "preis":  float(re.sub(r"[^\d.]","",article.select_one("p.price_color").text)),
            "sterne": stern_map.get(article.select_one("p.star-rating")["class"][1],0),
        })
    naechste = soup.select_one("li.next a")
    return rows, (BASE + "catalogue/" + naechste["href"]) if naechste else None

alle, url, seite = [], BASE, 1
while url and seite <= 3:
    zeilen, url = scrape_seite(url)
    alle.extend(zeilen)
    print(f"  Seite {seite}: {len(zeilen)} Buecher (Gesamt: {len(alle)})")
    seite += 1; time.sleep(0.5)

df = pd.DataFrame(alle)
print(f"Gesamt gescrapt: {len(df)} Buecher")
# LOESUNG: while-Schleife folgt "naechste Seite"-Links.

# AUFGABE 2: Statistische Analyse
print("\nAUFGABE 2: Analyse")
print(df.describe()[["preis","sterne"]].round(2))
print("\nPreis nach Sterne:")
print(df.groupby("sterne")["preis"].agg(["mean","min","max","count"]).round(2))

# AUFGABE 3: Kategorien scrapen
print("\nAUFGABE 3: Kategorien")
r = requests.get(BASE, timeout=10)
soup = BeautifulSoup(r.text, "html.parser")
kategorien = [(a.text.strip(), BASE+a["href"])
              for a in soup.select("ul.nav-list a")]
print(f"Kategorien: {len(kategorien)}")
for name, _ in kategorien[:8]:
    print(f"  {name}")
# LOESUNG: ul.nav-list enthaelt alle Navigationslinks als Liste.

# AUFGABE 4: Buchdetails - Einzelseite
print("\nAUFGABE 4: Buchdetails")
r0 = requests.get(BASE, timeout=10)
s0 = BeautifulSoup(r0.text, "html.parser")
buch_url = BASE + "catalogue/" + s0.select_one("article.product_pod a")["href"]
r2 = requests.get(buch_url, timeout=10)
s2 = BeautifulSoup(r2.text, "html.parser")
info = {row.th.text: row.td.text for row in s2.select("table.table tr")}
for k, v in info.items():
    print(f"  {k}: {v}")
# LOESUNG: Tabellen auf Detailseiten als Dict einlesen.

# AUFGABE 5: Visualisierung
print("\nAUFGABE 5: Plots")
fig, (ax1, ax2) = plt.subplots(1,2,figsize=(11,4))
sns.histplot(df["preis"], bins=20, kde=True, color="steelblue", ax=ax1)
ax1.set_title("Preisverteilung")
sns.boxplot(x="sterne", y="preis", data=df, palette="YlOrRd", ax=ax2)
ax2.set_title("Preis nach Sternezahl")
plt.tight_layout(); plt.savefig("plot_12f_05.png", dpi=100); plt.show()

# AUFGABE 6: Regex direkt auf HTML
print("\nAUFGABE 6: Regex")
r = requests.get(BASE, timeout=10)
preise_regex = re.findall(r"£(\d+\.\d+)", r.text)
print(f"Preise via Regex: {preise_regex[:5]}")
print(f"Teuerster Preis: £{max(float(p) for p in preise_regex):.2f}")
# LOESUNG: re.findall() direkt auf .text als Alternative zu BeautifulSoup.

# AUFGABE 7: User-Agent setzen
print("\nAUFGABE 7: Browser-Header")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120"}
r = requests.get(BASE, headers=headers, timeout=10)
print(f"Status mit Browser-UA: {r.status_code}")
# LOESUNG: Manche Server blockieren Python-Standard-UA. Browser-UA hilft.

# AUFGABE 8: robots.txt pruefen
print("\nAUFGABE 8: robots.txt (ethisches Scraping)")
r = requests.get("https://books.toscrape.com/robots.txt", timeout=10)
print(r.text[:200])
# LOESUNG: robots.txt VOR dem Scrapen lesen - ethische Pflicht!

# AUFGABE 9: Kategorienanzahl
print("\nAUFGABE 9: Buecher je Kategorie")
for kat, kurl in kategorien[1:5]:
    try:
        rk = requests.get(kurl, timeout=8)
        sk = BeautifulSoup(rk.text, "html.parser")
        anz = sk.select_one("form.form-horizontal strong")
        print(f"  {kat:<20} {anz.text if anz else '?':>4} Buecher")
        time.sleep(0.3)
    except: pass

# AUFGABE 10: Export mit Wechselkurs
print("\nAUFGABE 10: Export")
df["preis_eur"] = (df["preis"] * 1.17).round(2)
df.to_csv("buecher_komplett.csv", index=False)
print(f"buecher_komplett.csv: {len(df)} Zeilen")
print(df[["titel","preis","preis_eur","sterne"]].head(4).to_string(index=False))
plt.close("all")

print("\n" + "=" * 60)
print("Tag 12 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
