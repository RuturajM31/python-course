# tag13_anfaenger.py
# Lerntag 13 - Datum und Zeit: Grundlagen (Anfaenger)
# Thema: datetime, date, timedelta, strftime, strptime, calendar
# Ausfuehren in Spyder: F5

from datetime import datetime, date, timedelta
import calendar

print("=" * 60)
print("LERNTAG 13 - Datum und Zeit fuer Anfaenger")
print("=" * 60)

# AUFGABE 1: Aktuelles Datum und Uhrzeit
print("\nAUFGABE 1: Jetzt")
jetzt = datetime.now()
heute = date.today()
print(f"datetime.now(): {jetzt}")
print(f"date.today():   {heute}")
print(f"Jahr={jetzt.year}, Monat={jetzt.month}, Tag={jetzt.day}, Stunde={jetzt.hour}")
# LOESUNG: datetime.now() gibt Datum+Uhrzeit. date.today() nur das Datum.

# AUFGABE 2: Datum manuell erstellen
print("\nAUFGABE 2: Datum erstellen")
geburtstag = date(1990, 6, 15)
termin     = datetime(2024, 12, 24, 18, 30, 0)
print(f"Geburtstag: {geburtstag}")
print(f"Termin:     {termin}")
# LOESUNG: date(jahr, monat, tag) | datetime(jahr, monat, tag, std, min, sek)

# AUFGABE 3: strftime - Datum formatieren
print("\nAUFGABE 3: strftime")
d = datetime(2024, 7, 15, 14, 30)
formate = ["%d.%m.%Y", "%Y-%m-%d", "%A, %d. %B %Y", "%d/%m/%y %H:%M"]
for f in formate:
    print(f"  '{f}':  {d.strftime(f)}")
# LOESUNG: %d=Tag, %m=Monat, %Y=vierstelliges Jahr, %H=Stunde, %M=Minute

# AUFGABE 4: strptime - String -> Datum
print("\nAUFGABE 4: strptime")
texte = [("15.07.2024",         "%d.%m.%Y"),
         ("2024-07-15 14:30",   "%Y-%m-%d %H:%M"),
         ("15/07/24",           "%d/%m/%y")]
for t, f in texte:
    d = datetime.strptime(t, f)
    print(f"  '{t}' -> {d}")
# LOESUNG: strptime(string, format) wandelt String in datetime um.

# AUFGABE 5: timedelta - Zeitabstand
print("\nAUFGABE 5: timedelta")
h = date.today()
in30  = h + timedelta(days=30)
vor7  = h - timedelta(weeks=1)
print(f"Heute:         {h}")
print(f"In 30 Tagen:   {in30}")
print(f"Vor 1 Woche:   {vor7}")
# LOESUNG: timedelta(days=n / weeks=n) addieren oder subtrahieren.

# AUFGABE 6: Altersberechnung
print("\nAUFGABE 6: Alter berechnen")
def alter(geb: date) -> int:
    h = date.today()
    return h.year - geb.year - ((h.month, h.day) < (geb.month, geb.day))

personen = [("Anna", date(1990,6,15)), ("Ben", date(2000,12,31)), ("Cara", date(1985,1,1))]
for name, geb in personen:
    print(f"  {name}: {alter(geb)} Jahre")
# LOESUNG: Tuple-Vergleich prueft, ob Geburtstag dieses Jahr schon war.

# AUFGABE 7: Wochentag und Kalenderwoche
print("\nAUFGABE 7: Wochentag")
tage_namen = ["Mo","Di","Mi","Do","Fr","Sa","So"]
for d in [date(2024,1,1), date(2024,7,4), date(2024,12,25)]:
    wt  = tage_namen[d.weekday()]
    kw  = d.isocalendar().week
    print(f"  {d}: {wt} (KW {kw})")
# LOESUNG: .weekday() = 0 (Mo) bis 6 (So). .isocalendar().week = Kalenderwoche.

# AUFGABE 8: Kalender ausgeben
print("\nAUFGABE 8: Kalender")
print(calendar.month(2024, 12))
# LOESUNG: calendar.month(jahr, monat) gibt formatierten Monatskalender.

# AUFGABE 9: Zeitdifferenz berechnen
print("\nAUFGABE 9: Zeitdifferenz")
start = datetime(2024, 1, 1, 9, 0)
ende  = datetime(2024, 3, 15, 17, 30)
diff  = ende - start
tage   = diff.days
stunden = diff.seconds // 3600
minuten = (diff.seconds % 3600) // 60
print(f"Von {start.date()} bis {ende.date()}: {tage} Tage, {stunden}h {minuten}min")
# LOESUNG: datetime - datetime ergibt timedelta. .days und .seconds verfuegbar.

# AUFGABE 10: Countdown bis naechstes Ereignis
print("\nAUFGABE 10: Countdown")
def naechstes(monat, tag):
    h = date.today()
    d = date(h.year, monat, tag)
    if d < h: d = date(h.year+1, monat, tag)
    return d, (d - h).days

ereignisse = [("Weihnachten",12,25),("Neujahr",1,1),("Valentinstag",2,14)]
for name, m, t in ereignisse:
    datum, tage = naechstes(m, t)
    print(f"  {name:<15}: {datum}  (in {tage} Tagen)")
# LOESUNG: Falls Datum bereits vergangen -> naechstes Jahr nehmen.

print("\n" + "=" * 60)
print("Tag 13 - Anfaenger: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
