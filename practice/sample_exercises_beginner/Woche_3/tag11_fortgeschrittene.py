# tag11_fortgeschrittene.py
# Lerntag 11 - Web-Services: Fortgeschrittene API-Nutzung
# Thema: Session, Pagination, DataFrame aus API, Rate-Limiting, Visualisierung
# Ausfuehren in Spyder: F5

import requests
import pandas as pd
import matplotlib.pyplot as plt
import time

print("=" * 60)
print("LERNTAG 11 - Web-Services fuer Fortgeschrittene")
print("=" * 60)

BASE = "https://jsonplaceholder.typicode.com"

# AUFGABE 1: Session fuer mehrere Requests
print("\nAUFGABE 1: Session")
with requests.Session() as s:
    s.headers.update({"User-Agent": "PythonLernbot/1.0"})
    for pid in [1, 2, 3]:
        r = s.get(f"{BASE}/posts/{pid}")
        print(f"  Post {pid}: {r.json()['title'][:45]}")
# LOESUNG: Session() wiederverwendet TCP-Verbindung -> effizienter bei vielen Requests.

# AUFGABE 2: Pagination simulieren
print("\nAUFGABE 2: Pagination")
alle = []
for page in range(1, 4):
    r = requests.get(f"{BASE}/posts", params={"_page": page, "_limit": 5})
    batch = r.json()
    alle.extend(batch)
    print(f"  Seite {page}: {len(batch)} Posts (Gesamt: {len(alle)})")
# LOESUNG: _page und _limit sind gaengige Paginierungsparameter.

# AUFGABE 3: API-Daten in DataFrame
print("\nAUFGABE 3: API -> DataFrame")
r = requests.get(f"{BASE}/users")
df = pd.DataFrame(r.json())
df["city"]    = df["address"].apply(lambda x: x["city"])
df["company"] = df["company"].apply(lambda x: x["name"])
print(df[["id","name","email","city","company"]].to_string(index=False))
# LOESUNG: .apply(lambda x: x['key']) extrahiert Werte aus verschachtelten Dicts.

# AUFGABE 4: Mehrere Endpunkte joinen
print("\nAUFGABE 4: Join")
users = pd.DataFrame(requests.get(f"{BASE}/users").json())[["id","name"]]
posts = pd.DataFrame(requests.get(f"{BASE}/posts").json())
df_join = posts.merge(users, left_on="userId", right_on="id", suffixes=("_post","_user"))
stats = df_join.groupby("name")["id_post"].count().sort_values(ascending=False)
print("Posts pro User (Top 5):")
print(stats.head().to_string())
# LOESUNG: API-Daten als DataFrames laden, mit merge() zusammenfuehren.

# AUFGABE 5: Retry-Logik (Rate-Limiting)
print("\nAUFGABE 5: Retry")
def get_mit_retry(url, max_retries=3, delay=1):
    for i in range(max_retries):
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200: return r
            if r.status_code == 429:
                print(f"  429 - Warte {delay}s..."); time.sleep(delay); delay *= 2
        except Exception as e:
            print(f"  Fehler: {e}")
    return None

r = get_mit_retry(f"{BASE}/posts/42")
if r: print(f"Erfolgreich: {r.json()['title'][:50]}")
# LOESUNG: Exponentielles Backoff bei 429 Too Many Requests.

# AUFGABE 6: Kommentare filtern mit str-Methoden
print("\nAUFGABE 6: Kommentare filtern")
r = requests.get(f"{BASE}/comments")
df_c = pd.DataFrame(r.json())
gmail = df_c[df_c["email"].str.contains("@gmail", na=False)]
print(f"Gmail-Kommentare: {len(gmail)} von {len(df_c)}")
print(df_c["email"].str.extract(r"@(.+)")[0].value_counts().head(5))
# LOESUNG: .str.contains() und .str.extract() auf API-Daten anwenden.

# AUFGABE 7: DELETE-Request
print("\nAUFGABE 7: DELETE")
r = requests.delete(f"{BASE}/posts/5")
print(f"DELETE Status: {r.status_code}, Response: {r.json()}")
# LOESUNG: requests.delete(url). Status 200 = erfolgreich geloescht.

# AUFGABE 8: PUT-Request (Update)
print("\nAUFGABE 8: PUT")
update = {"id":1,"title":"Aktualisierter Titel","body":"Neuer Text","userId":1}
r = requests.put(f"{BASE}/posts/1", json=update)
print(f"PUT Status: {r.status_code}")
print(f"Neuer Titel: {r.json()['title']}")
# LOESUNG: PUT ersetzt komplette Ressource. PATCH nur Teilupdates.

# AUFGABE 9: Todos-Statistik
print("\nAUFGABE 9: Todos-Statistik")
df_t = pd.DataFrame(requests.get(f"{BASE}/todos").json())
stats = df_t.groupby("userId")["completed"].agg(
    erledigt="sum", gesamt="count"
).assign(quote=lambda x: (x["erledigt"]/x["gesamt"]*100).round(1))
print(stats.head(5).to_string())
# LOESUNG: groupby + agg auf API-Daten.

# AUFGABE 10: Visualisierung
print("\nAUFGABE 10: Visualisierung")
df_t2 = pd.DataFrame(requests.get(f"{BASE}/todos").json())
quote = df_t2.groupby("userId")["completed"].mean() * 100
fig, ax = plt.subplots(figsize=(8,4))
quote.plot(kind="bar", ax=ax, color="steelblue", edgecolor="white")
ax.set_title("Erledigungs-Quote nach User-ID"); ax.set_ylabel("%"); ax.set_ylim(0,100)
ax.axhline(50, color="red", linestyle="--", lw=1, label="50%-Linie")
ax.legend(); plt.tight_layout()
plt.savefig("plot_11f_10.png", dpi=100); plt.show()
print("Plot gespeichert: plot_11f_10.png")

print("\n" + "=" * 60)
print("Tag 11 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
