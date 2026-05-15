# tag10_fortgeschrittene.py
# Lerntag 10 - Regular Expressions: Fortgeschrittene Muster
# Thema: Lookahead, Non-greedy, benannte Gruppen, VERBOSE, Backreferences
# Ausfuehren in Spyder: F5

import re
from collections import Counter

print("=" * 60)
print("LERNTAG 10 - Regular Expressions fuer Fortgeschrittene")
print("=" * 60)

# AUFGABE 1: Lookahead und Lookbehind
print("\nAUFGABE 1: Lookahead / Lookbehind")
text = "Preis: 49EUR, Bonus: $100, Rabatt: 15EUR, Strafe: $20"
print("Vor EUR:", re.findall(r"\d+(?=EUR)", text))
print("Nach $: ", re.findall(r"(?<=\$)\d+", text))
# LOESUNG: (?=X) positiver Lookahead. (?<=X) positiver Lookbehind.

# AUFGABE 2: Non-greedy Matching
print("\nAUFGABE 2: Non-greedy")
html = "<b>Fett</b> und <i>kursiv</i> und <b>auch fett</b>"
print("Greedy:    ", re.findall(r"<.+>", html))
print("Non-greedy:", re.findall(r"<.+?>", html))
# LOESUNG: .+? matcht so wenig wie moeglich.

# AUFGABE 3: Benannte Gruppen
print("\nAUFGABE 3: Benannte Gruppen")
muster = r"(?P<jahr>\d{4})-(?P<monat>\d{2})-(?P<tag>\d{2})"
for d in ["2024-07-15","1999-12-31","2000-01-01"]:
    m = re.match(muster, d)
    if m: print(f"  {d} -> Jahr={m.group('jahr')}, Monat={m.group('monat')}, Tag={m.group('tag')}")
# LOESUNG: (?P<name>...) -> .group("name") statt Zahlenindex.

# AUFGABE 4: re.compile fuer Performance
print("\nAUFGABE 4: re.compile")
pat = re.compile(r"(\d{4}-\d{2}-\d{2})\s(ERROR|WARNING|INFO):\s(.+)")
for z in ["2024-01-15 ERROR: Datenbankfehler","2024-01-15 INFO: Server gestartet",
          "2024-01-16 WARNING: Speicher niedrig","2024-01-16 ERROR: Netzwerkausfall"]:
    m = pat.match(z)
    if m: print(f"  Datum={m.group(1)}, Level={m.group(2)}, Msg={m.group(3)}")

# AUFGABE 5: Backreferences - Doppelwoerter
print("\nAUFGABE 5: Backreferences")
for t in ["Das ist ist ein Test.","Alles ok.","Er sagte sagte es."]:
    m = re.search(r"\b(\w+)\s+\1\b", t)
    print(f"  {'Doppel: '+m.group(1) if m else 'OK':<20}  '{t}'")
# LOESUNG: \1 referenziert Inhalt der ersten Gruppe erneut.

# AUFGABE 6: re.VERBOSE
print("\nAUFGABE 6: re.VERBOSE")
tel_pat = re.compile(r"""
    ^(\+49|0)         # Laendervorwahl
    \s*               # optionales Leerzeichen
    (\d{2,5})         # Ortsvorwahl
    [\s/\-]?          # Trenner
    (\d{3,12})        # Rufnummer
    $
""", re.VERBOSE)
for n in ["+49 89 12345678","089/1234567","+49 30-9876543","keine_nummer"]:
    print(f"  '{n}': {'OK' if tel_pat.match(n) else 'UNGUELTIG'}")

# AUFGABE 7: re.sub mit Funktion
print("\nAUFGABE 7: sub mit Funktion")
def c2f(m): return f"{float(m.group(1))*9/5+32:.1f}F"
text = "0C, 22C und -5C."
print("In Fahrenheit:", re.sub(r"(-?\d+(?:\.\d+)?)C", c2f, text))

# AUFGABE 8: URL-Parser
print("\nAUFGABE 8: URL-Parser")
pat = re.compile(r"(?P<prot>https?)://(?P<domain>[\w.-]+)(?P<pfad>/[\w./\-?=&]*)?")
for url in ["https://www.example.com/path/page","http://blog.test.org/artikel?id=42"]:
    m = pat.match(url)
    if m: print(f"  Proto={m.group('prot')}, Domain={m.group('domain')}, Pfad={m.group('pfad') or '/'}")

# AUFGABE 9: Woerthaeufigkeiten
print("\nAUFGABE 9: Woerthaeufigkeiten")
text = """Python ist eine verbreitete Sprache. Python eignet sich fuer Daten.
Viele Entwickler nutzen Python. Python, Python!"""
top5 = Counter(re.findall(r"\b[a-zA-Z]+\b", text.lower())).most_common(5)
for w,n in top5: print(f"  '{w}': {n}x")

# AUFGABE 10: Passwort-Validierung
print("\nAUFGABE 10: Passwort-Validierung")
def pruefe(pw):
    regeln = {
        ">=8 Zeichen":    len(pw)>=8,
        "Grossbuchstabe": bool(re.search(r"[A-Z]",pw)),
        "Kleinbuchstabe": bool(re.search(r"[a-z]",pw)),
        "Zahl":           bool(re.search(r"\d",pw)),
        "Sonderzeichen":  bool(re.search(r"[!@#$%^&*()\-_=+]",pw)),
    }
    ok = all(regeln.values())
    print(f"  '{pw}': {'GUELTIG' if ok else 'UNGUELTIG'}")
    for r,v in regeln.items(): print(f"    {'OK' if v else '--'} {r}")
pruefe("abc"); pruefe("Sicher1!")

print("\n" + "=" * 60)
print("Tag 10 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
