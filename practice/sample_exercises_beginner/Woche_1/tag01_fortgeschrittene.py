#tag01_advanced.py
#Learning Day 1 -Python Basics: Advanced Concepts
#Topic: List/Dict Comprehensions, Unpacking, *args/**kwargs, Walrus
#Run in Spyder: F5

print("=" * 60)
print("LERNTAG 1 - Python Grundlagen fuer Fortgeschrittene")
print("=" * 60)

#TASK 1: List Comprehensions
print("\nAUFGABE 1: List Comprehensions")
quadrate  = [x**2 for x in range(1,11)]
gerade    = [x for x in range(1,21) if x%2==0]
wort_laen = [len(w) for w in ["Python","ist","grossartig","und","macht","Spass"]]
print(f"Quadrate 1-10:  {quadrate}")
print(f"Gerade 1-20:    {gerade}")
print(f"Wortlaengen:    {wort_laen}")
#SOLUTION: [expression for element in iterable if condition]
#TASK 2: Dict Comprehensions
print("\nAUFGABE 2: Dict Comprehensions")
worte   = ["apfel","banane","kirsche","dattel","erdbeere"]
laengen = {w: len(w) for w in worte}
quadr_d = {x: x**2 for x in range(1,8)}
umkehr  = {v: k for k, v in laengen.items()}
print(f"Wort-Laengen:  {laengen}")
print(f"x->x^2:        {quadr_d}")
print(f"Umgekehrt:     {umkehr}")
#LOESUNG: {key: value for element in iterable}
#AUFGABE 3: Nested Comprehensions
print("\nAUFGABE 3: Verschachtelt")
matrix  = [[i*j for j in range(1,6)] for i in range(1,6)]
flach   = [x for zeile in matrix for x in zeile]
print("5x5 Multiplikationstabelle:")
for zeile in matrix:
    print(f"  {zeile}")
print(f"Abgeflacht (erste 10): {flach[:10]}")
#SOLUTION: [[...] for i in ...] creates nested list.
#TASK 4: Unpacking
print("\nAUFGABE 4: Unpacking")
a, b, c = (10, 20, 30)
erste, *mitte, letzte = [1,2,3,4,5,6,7]
x, y = y, x = 5, 9   #swap in one line
print(f"a,b,c = {a},{b},{c}")
print(f"erste={erste}, mitte={mitte}, letzte={letzte}")
x, y = 5, 9; x, y = y, x
print(f"Nach swap: x={x}, y={y}")
#SOLUTION: *before variable collects remainder. a,b = b,a exchanges without auxiliary variable.
#TASK 5: *args and **kwargs
print("\nAUFGABE 5: *args / **kwargs")
def summe(*args):
    return sum(args)

def vorstellen(**kwargs):
    return ", ".join(f"{k}={v}" for k,v in kwargs.items())

print(f"summe(1,2,3,4,5) = {summe(1,2,3,4,5)}")
print(f"vorstellen(...) = {vorstellen(name='Anna',alter=28,stadt='Wien')}")
#SOLUTION: *args = any number of pos. Arguments as tuples. **kwargs = as Dict.
#TASK 6: Walrus operator :=
print("\nAUFGABE 6: Walrus-Operator")
import re
texte = ["Bestellung #1234", "Keine ID", "Auftrag #5678", "Ohne Nummer"]
for t in texte:
    if m := re.search(r"#(\d+)", t):
        print(f"  '{t}' -> ID gefunden: {m.group(1)}")
    else:
        print(f"  '{t}' -> keine ID")
#SOLUTION: := assigns value AND checks it at the same time (Python 3.8+).
#TASK 7: zip and enumerate
print("\nAUFGABE 7: zip + enumerate")
namen   = ["Alice","Bob","Carol","Dave"]
punkte  = [85, 92, 78, 96]
for i, (name, p) in enumerate(zip(namen, punkte), start=1):
    note = "A" if p>=90 else "B" if p>=80 else "C"
    print(f"  {i}. {name:<8} {p} Punkte -> Note {note}")
#SOLUTION: zip() combines lists in pairs. enumerate() returns index + value.
#TASK 8: map, filter, sorted with key
print("\nAUFGABE 8: map / filter / sorted")
zahlen = [3,-7,1,-9,4,-6,2,8,-5]
positiv     = list(filter(lambda x: x>0, zahlen))
verdoppelt  = list(map(lambda x: x*2, zahlen))
abs_sort    = sorted(zahlen, key=abs)
print(f"Positiv:   {positiv}")
print(f"Verdoppelt:{verdoppelt}")
print(f"Nach Betrag sortiert: {abs_sort}")
#SOLUTION: filter(func, iter), map(func, iter), sorted(iter, key=func)
#TASK 9: String methods advanced
print("\nAUFGABE 9: Strings fortgeschritten")
csv_zeile = "  Anna ; 28 ; Berlin ; Ingenieurin  "
felder = [f.strip() for f in csv_zeile.split(";")]
print(f"Felder:        {felder}")
print(f"Join:          {' | '.join(felder)}")
text = "the quick brown fox jumps"
print(f"Title-Case:    {text.title()}")
print(f"Wortanzahl:    {len(text.split())}")
print(f"Startswith 'the': {text.startswith('the')}")
#SOLUTION: .split(sep) + list comprehension + .strip() for CSV parsing.
#TASK 10: Nested Dicts + Comprehension
print("\nAUFGABE 10: Verschachtelte Dicts")
mitarbeiter = {
    "A001": {"name":"Klaus","abt":"IT",  "gehalt":4200},
    "A002": {"name":"Petra","abt":"HR",  "gehalt":3800},
    "A003": {"name":"Tom",  "abt":"IT",  "gehalt":4500},
    "A004": {"name":"Sara", "abt":"Sales","gehalt":3600},
}
it_team = {k: v for k,v in mitarbeiter.items() if v["abt"]=="IT"}
print("IT-Team:")
for k,v in it_team.items():
    print(f"  {k}: {v['name']}, {v['gehalt']} EUR")
avg = sum(v["gehalt"] for v in mitarbeiter.values()) / len(mitarbeiter)
print(f"Durchschnittsgehalt: {avg:.0f} EUR")
#SOLUTION: Filter nested dict with comprehension, generator expression for sum.

print("\n" + "=" * 60)
print("Tag 1 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
