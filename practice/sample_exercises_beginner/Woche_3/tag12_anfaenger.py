# tag12_anfaenger.py
# Lerntag 12 - Web-Scraping: Grundlagen (Anfaenger)
# Thema: requests + BeautifulSoup, Tags, Attribute, CSS-Selektoren
# Ausfuehren in Spyder: F5

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("LERNTAG 12 - Web-Scraping fuer Anfaenger")
print("=" * 60)

URL = "https://books.toscrape.com/"

# AUFGABE 1: HTML laden
print("\nAUFGABE 1: HTML laden")
r = requests.get(URL, timeout=10)
print(f"Status: {r.status_code}")
print(f"HTML-Laenge: {len(r.text)} Zeichen")
# LOESUNG: requests.get(url).text gibt HTML als String.

# AUFGABE 2: BeautifulSoup erstellen
print("\nAUFGABE 2: BeautifulSoup")
soup = BeautifulSoup(r.text, "html.parser")
print(f"Seitentitel: {soup.title.string}")
print(f"Anzahl h3-Tags: {len(soup.find_all('h3'))}")
# LOESUNG: BeautifulSoup(html, 'html.parser') -> soup.title, soup.find_all() usw.

# AUFGABE 3: Buchtitel lesen
print("\nAUFGABE 3: Buchtitel")
titel = [h3.a["title"] for h3 in soup.find_all("h3")]
print(f"Gefundene Buecher: {len(titel)}")
for t in titel[:5]:
    print(f"  - {t}")
# LOESUNG: tag["attribut"] liest HTML-Attribute aus.

# AUFGABE 4: Preise
print("\nAUFGABE 4: Preise")
preise_raw = [p.text for p in soup.select("p.price_color")]
preise = [float(p.replace("Â","").replace("£","").strip()) for p in preise_raw]
print(f"Preise (erste 5): {preise[:5]}")
print(f"Durchschnittspreis: £{sum(preise)/len(preise):.2f}")
# LOESUNG: soup.select("css.selektor") nutzt CSS-Selektoren.

# AUFGABE 5: Sterne-Bewertung
print("\nAUFGABE 5: Sterne")
stern_map = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
sterne = [stern_map.get(p["class"][1], 0) for p in soup.select("p.star-rating")]
print(f"Sterne (erste 10): {sterne[:10]}")
# LOESUNG: CSS-Klassen geben Bewertung als Wort (One/Two/.../Five).

# AUFGABE 6: Verfuegbarkeit
print("\nAUFGABE 6: Verfuegbarkeit")
verfueg = [p.text.strip() for p in soup.select("p.instock")]
print(f"'In Stock'-Eintraege: {len(verfueg)}")
# LOESUNG: select("p.instock") - Punkt steht fuer CSS-Klasse.

# AUFGABE 7: DataFrame erstellen
print("\nAUFGABE 7: DataFrame")
df = pd.DataFrame({"Titel": titel, "Preis": preise, "Sterne": sterne})
print(df.head(5).to_string(index=False))
print(f"\nTeuerste 3:")
print(df.nlargest(3,"Preis")[["Titel","Preis","Sterne"]].to_string(index=False))
# LOESUNG: Gescrapte Listen direkt als DataFrame-Spalten nutzen.

# AUFGABE 8: Filtern
print("\nAUFGABE 8: Filtern")
fuenf_sterne = df[df["Sterne"]==5]
print(f"5-Sterne-Buecher: {len(fuenf_sterne)}")
print(fuenf_sterne[["Titel","Preis"]].to_string(index=False))
# LOESUNG: df[df["Spalte"]==Wert] wie bei jedem DataFrame.

# AUFGABE 9: Links extrahieren
print("\nAUFGABE 9: Links")
links = [a["href"] for a in soup.select("article.product_pod a")]
print(f"Buch-Links gesamt: {len(links)}")
print(f"Beispiel: {links[0]}")
# LOESUNG: soup.select("article a") findet alle Links in Artikel-Tags.

# AUFGABE 10: CSV + Plot
print("\nAUFGABE 10: CSV + Plot")
df.to_csv("buecher.csv", index=False)
print("buecher.csv gespeichert.")
df["Sterne"].value_counts().sort_index().plot(kind="bar", color="gold", edgecolor="white")
plt.title("Stern-Verteilung der gescrapten Buecher")
plt.xlabel("Sterne"); plt.ylabel("Anzahl"); plt.tight_layout()
plt.savefig("plot_12_10.png", dpi=100); plt.show()

print("\n" + "=" * 60)
print("Tag 12 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
