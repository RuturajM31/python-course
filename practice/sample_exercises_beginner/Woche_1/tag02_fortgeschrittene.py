# tag02_fortgeschrittene.py
# Lerntag 2 - Kontrollstrukturen und Funktionen: Fortgeschritten
# Thema: Closures, Dekoratoren, Generatoren, Lambda, functools
# Ausfuehren in Spyder: F5

import time
import functools

print("=" * 60)
print("LERNTAG 2 - Kontrollstrukturen/Funktionen Fortgeschrittene")
print("=" * 60)

# AUFGABE 1: Lambda-Funktionen
print("\nAUFGABE 1: Lambda")
quadrat   = lambda x: x**2
addiere   = lambda x, y: x + y
in_bereich= lambda x, a, b: a <= x <= b

print(f"quadrat(7) = {quadrat(7)}")
print(f"addiere(3,4) = {addiere(3,4)}")
personen = [("Anna",32),("Zoe",25),("Max",41),("Ben",28)]
sortiert = sorted(personen, key=lambda p: p[1])
print(f"Nach Alter: {sortiert}")
# LOESUNG: lambda args: ausdruck - einzeilige anonyme Funktion.

# AUFGABE 2: Closures
print("\nAUFGABE 2: Closures")
def multiplikator(faktor):
    def inner(zahl):
        return zahl * faktor
    return inner

mal3  = multiplikator(3)
mal10 = multiplikator(10)
print(f"mal3(7)  = {mal3(7)}")
print(f"mal10(5) = {mal10(5)}")
# LOESUNG: inner() "merkt" sich faktor aus dem aeusseren Scope -> Closure.

# AUFGABE 3: Dekoratoren
print("\nAUFGABE 3: Dekoratoren")
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        ende   = time.perf_counter()
        print(f"  {func.__name__}() dauerte {(ende-start)*1000:.3f} ms")
        return result
    return wrapper

@timer
def summe_bis(n):
    return sum(range(n+1))

print(f"Ergebnis: {summe_bis(1_000_000)}")
# LOESUNG: Dekorator = Funktion, die andere Funktion umhuellt (@-Syntax).

# AUFGABE 4: Generatoren
print("\nAUFGABE 4: Generatoren")
def fibonacci(max_wert):
    a, b = 0, 1
    while a <= max_wert:
        yield a
        a, b = b, a+b

fib_liste = list(fibonacci(1000))
print(f"Fibonacci bis 1000: {fib_liste}")

def unendliche_folge(start=0):
    n = start
    while True:
        yield n
        n += 1

gen = unendliche_folge(5)
print(f"Unendlich ab 5 (erste 5): {[next(gen) for _ in range(5)]}")
# LOESUNG: yield gibt Wert zurueck und pausiert. Generator ist speichereffizient.

# AUFGABE 5: functools.lru_cache
print("\nAUFGABE 5: Memoization (lru_cache)")
@functools.lru_cache(maxsize=None)
def fib_cached(n):
    if n < 2: return n
    return fib_cached(n-1) + fib_cached(n-2)

start = time.perf_counter()
ergebnis = fib_cached(35)
dauer = (time.perf_counter()-start)*1000
print(f"fib(35) = {ergebnis}  ({dauer:.3f} ms)")
print(f"Cache-Info: {fib_cached.cache_info()}")
# LOESUNG: @lru_cache speichert Ergebnisse - massive Beschleunigung bei Rekursion.

# AUFGABE 6: Partielle Funktionen
print("\nAUFGABE 6: partial")
from functools import partial

def potenz(basis, exponent):
    return basis ** exponent

quadrat  = partial(potenz, exponent=2)
kubik    = partial(potenz, exponent=3)
zweierpot= partial(potenz, 2)

print(f"quadrat(5)  = {quadrat(5)}")
print(f"kubik(4)    = {kubik(4)}")
print(f"2^10 = {zweierpot(10)}")
# LOESUNG: partial() fixiert Argumente einer Funktion -> neue spezialisierte Funktion.

# AUFGABE 7: Generator Expressions
print("\nAUFGABE 7: Generator Expressions")
import sys
n = 1_000_000
gen_summe  = sum(x**2 for x in range(n))
list_groesse = sys.getsizeof([x**2 for x in range(100)])
gen_groesse  = sys.getsizeof(x**2 for x in range(100))
print(f"Summe x^2 bis {n}: {gen_summe:,}")
print(f"List-Groesse (100 Elemente): {list_groesse} Bytes")
print(f"Gen-Groesse  (100 Elemente): {gen_groesse} Bytes")
# LOESUNG: (ausdruck for ...) = Generator Expression, kein Speicher fuer alle Werte.

# AUFGABE 8: Verschachtelte Funktionen + Nonlocal
print("\nAUFGABE 8: nonlocal")
def zaehler(start=0, schritt=1):
    wert = start
    def erhoehe():
        nonlocal wert
        wert += schritt
        return wert
    def zuruecksetzen():
        nonlocal wert
        wert = start
    def aktuell():
        return wert
    return erhoehe, zuruecksetzen, aktuell

erhoehe, reset, stand = zaehler(0, 5)
for _ in range(4): erhoehe()
print(f"Nach 4x erhoehen (schritt=5): {stand()}")
reset()
print(f"Nach reset: {stand()}")
# LOESUNG: nonlocal erlaubt Zugriff auf Variable aus aeusserem (nicht globalem) Scope.

# AUFGABE 9: Mehrfache Dekoratoren
print("\nAUFGABE 9: Mehrfache Dekoratoren")
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  Aufruf: {func.__name__}({args})")
        result = func(*args, **kwargs)
        print(f"  Ergebnis: {result}")
        return result
    return wrapper

def validiere_positiv(func):
    @functools.wraps(func)
    def wrapper(n):
        if n < 0: raise ValueError(f"n muss >= 0 sein, war: {n}")
        return func(n)
    return wrapper

@logger
@validiere_positiv
def wurzel(n):
    return n ** 0.5

wurzel(16)
try: wurzel(-1)
except ValueError as e: print(f"  Fehler: {e}")
# LOESUNG: Dekoratoren werden von innen nach aussen angewendet (bottom-up).

# AUFGABE 10: Funktionales Programmieren
print("\nAUFGABE 10: Funktional kombiniert")
from functools import reduce

daten = [4, 7, 2, 9, 1, 5, 8, 3, 6]
gefiltert  = list(filter(lambda x: x > 3, daten))
verdoppelt = list(map(lambda x: x*2, gefiltert))
produkt    = reduce(lambda a, b: a*b, gefiltert)

print(f"Original:   {daten}")
print(f"Gefiltert (>3): {gefiltert}")
print(f"Verdoppelt: {verdoppelt}")
print(f"Produkt:    {produkt}")
# Pipeline als Einzeiler:
ergebnis = list(map(lambda x: x**2, filter(lambda x: x%2==0, range(1,11))))
print(f"Quadrate der geraden Zahlen 1-10: {ergebnis}")
# LOESUNG: filter -> map -> reduce = klassische funktionale Pipeline.

print("\n" + "=" * 60)
print("Tag 2 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
