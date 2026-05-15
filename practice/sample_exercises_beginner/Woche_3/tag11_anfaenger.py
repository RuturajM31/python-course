# tag11_anfaenger.py
# Lerntag 11 - Web-Services und APIs: Grundlagen (Anfaenger)
# Thema: requests, JSON, REST-API, Parameter, Fehlerbehandlung
# Ausfuehren in Spyder: F5

import requests
import json

print("=" * 60)
print("LERNTAG 11 - Web-Services / APIs fuer Anfaenger")
print("=" * 60)

BASE = "https://jsonplaceholder.typicode.com"

# AUFGABE 1: Einfacher GET-Request
print("\nAUFGABE 1: GET-Request")
r = requests.get(f"{BASE}/posts/1")
print(f"Status-Code: {r.status_code}")
print(f"Content-Type: {r.headers['content-type']}")
# LOESUNG: requests.get(url) sendet HTTP-GET. .status_code = 200 bedeutet OK.

# AUFGABE 2: JSON parsen
print("\nAUFGABE 2: JSON parsen")
daten = r.json()
print(f"ID:     {daten['id']}")
print(f"Titel:  {daten['title']}")
print(f"UserID: {daten['userId']}")
# LOESUNG: .json() wandelt JSON-Antwort automatisch in Python-Dict um.

# AUFGABE 3: Liste von Ressourcen
print("\nAUFGABE 3: Liste abrufen")
r = requests.get(f"{BASE}/posts")
posts = r.json()
print(f"Anzahl Posts: {len(posts)}")
print(f"Erster Post:  {posts[0]['title'][:50]}")
# LOESUNG: JSON-Arrays werden als Python-Listen zurueckgegeben.

# AUFGABE 4: Query-Parameter
print("\nAUFGABE 4: Query-Parameter")
r = requests.get(f"{BASE}/posts", params={"userId": 1})
posts_u1 = r.json()
print(f"Posts von userId=1: {len(posts_u1)}")
print(f"URL war: {r.url}")
# LOESUNG: params=dict haengt ?key=value an die URL an.

# AUFGABE 5: Fehlerbehandlung
print("\nAUFGABE 5: Fehlerbehandlung")
urls = [f"{BASE}/posts/1", f"{BASE}/posts/9999", "https://nicht-vorhanden-xyz.de"]
for url in urls:
    try:
        r = requests.get(url, timeout=5)
        print(f"  ...{url[-20:]} -> {r.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"  ...{url[-20:]} -> Verbindungsfehler")
    except requests.exceptions.Timeout:
        print(f"  ...{url[-20:]} -> Timeout")
# LOESUNG: try/except fuer Netzwerkfehler. timeout=5 verhindert langes Warten.

# AUFGABE 6: Verschachtelte JSON-Daten
print("\nAUFGABE 6: Verschachteltes JSON")
r = requests.get(f"{BASE}/users/1")
user = r.json()
print(f"Name:   {user['name']}")
print(f"E-Mail: {user['email']}")
print(f"Stadt:  {user['address']['city']}")
print(f"Firma:  {user['company']['name']}")
# LOESUNG: Verschachtelte Dicts mit user['schluessel']['unterschluessel'] navigieren.

# AUFGABE 7: Alle User durchlaufen
print("\nAUFGABE 7: User-Liste")
r = requests.get(f"{BASE}/users")
for u in r.json()[:5]:
    print(f"  {u['id']:>2}. {u['name']:<25} {u['email']}")
# LOESUNG: JSON-Liste direkt mit for-Schleife iterieren.

# AUFGABE 8: POST-Request
print("\nAUFGABE 8: POST-Request")
neuer_post = {"title": "Mein Lernbeitrag", "body": "Python macht Spass!", "userId": 1}
r = requests.post(f"{BASE}/posts", json=neuer_post)
print(f"Status: {r.status_code}")
print(f"Neue ID: {r.json()['id']}")
# LOESUNG: requests.post(url, json=dict) sendet Daten als JSON-Body.

# AUFGABE 9: Response-Headers lesen
print("\nAUFGABE 9: Headers")
r = requests.get(f"{BASE}/posts/1")
for key in ["content-type", "cache-control", "x-powered-by"]:
    print(f"  {key}: {r.headers.get(key, 'nicht vorhanden')}")
# LOESUNG: r.headers ist ein dict-aehnliches Objekt mit HTTP-Headern.

# AUFGABE 10: JSON in Datei speichern und laden
print("\nAUFGABE 10: JSON speichern")
r = requests.get(f"{BASE}/users")
with open("users.json", "w", encoding="utf-8") as f:
    json.dump(r.json(), f, indent=2, ensure_ascii=False)
with open("users.json") as f:
    geladen = json.load(f)
print(f"Gespeichert + geladen: {len(geladen)} User")
# LOESUNG: json.dump(daten, datei, indent=2) schreibt lesbares JSON.

print("\n" + "=" * 60)
print("Tag 11 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
