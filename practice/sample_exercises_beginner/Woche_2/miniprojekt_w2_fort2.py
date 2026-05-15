# miniprojekt_w2_fort2.py
# MINIPROJEKT 4 (Fortgeschrittene) - Woche 2
# Titel: Log-Datei-Analyse mit Regular Expressions
# Kombiniert: Regex + Pandas + Seaborn
# Ausfuehren in Spyder: F5
# ============================================================

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
print("=" * 60)
print("MINIPROJEKT 4 - Log-Datei-Analyse")
print("=" * 60)

# Simulierter Apache-Log (50 Zeilen)
log_roh = [
    '192.168.1.1 - - [15/Jan/2024:10:00:01] "GET /index.html HTTP/1.1" 200 1234',
    '10.0.0.5    - - [15/Jan/2024:10:00:05] "POST /login HTTP/1.1" 401 512',
    '192.168.1.2 - - [15/Jan/2024:10:00:10] "GET /about.html HTTP/1.1" 200 890',
    '10.0.0.7    - - [15/Jan/2024:10:01:00] "GET /admin HTTP/1.1" 403 256',
    '192.168.1.1 - - [15/Jan/2024:10:01:30] "GET /kontakt.html HTTP/1.1" 200 765',
    '172.16.0.3  - - [15/Jan/2024:10:02:00] "GET /index.html HTTP/1.1" 200 1234',
    '10.0.0.5    - - [15/Jan/2024:10:02:15] "POST /login HTTP/1.1" 200 340',
    '192.168.1.5 - - [15/Jan/2024:10:02:45] "GET /produkte.html HTTP/1.1" 404 128',
    '172.16.0.3  - - [15/Jan/2024:10:03:00] "DELETE /api/item/5 HTTP/1.1" 405 64',
    '192.168.1.1 - - [15/Jan/2024:10:03:30] "GET /index.html HTTP/1.1" 200 1234',
] * 5

# Regex-Pattern fuer Apache-Log
log_pat = re.compile(
    r'([\d.]+)\s+\S+\s+\S+\s+'
    r'\[([^\]]+)\]\s+'
    r'"(\w+)\s+(\S+)\s+HTTP/[\d.]+"\s+'
    r'(\d{3})\s+(\d+)'
)

rows, fehler = [], 0
for zeile in log_roh:
    m = log_pat.match(zeile.strip())
    if m:
        rows.append({"ip":m.group(1),"zeit":m.group(2),"methode":m.group(3),
                     "pfad":m.group(4),"status":int(m.group(5)),"bytes":int(m.group(6))})
    else:
        fehler += 1

df = pd.DataFrame(rows)
print(f"Geparst: {len(df)} Eintraege, {fehler} Fehler")
print(f"Status-Verteilung:\n{df['status'].value_counts().sort_index()}")
print(f"\nTop-5 IPs:\n{df['ip'].value_counts().head()}")

df["status_kl"] = (df["status"]//100).map({
    2:"2xx Erfolg",3:"3xx Redirect",4:"4xx Fehler",5:"5xx Fehler"})

# Visualisierung
fig, axes = plt.subplots(2,2, figsize=(12,8))
fig.suptitle("Web-Server Log Analyse", fontsize=14, fontweight="bold")

sns.countplot(x="status", data=df, ax=axes[0,0]); axes[0,0].set_title("HTTP-Status-Codes")
df["methode"].value_counts().plot(kind="pie", autopct="%1.0f%%", ax=axes[0,1])
axes[0,1].set_title("HTTP-Methoden"); axes[0,1].set_ylabel("")
df["pfad"].value_counts().head(6).plot(kind="barh", color="steelblue", ax=axes[1,0])
axes[1,0].set_title("Haeufigste Pfade"); axes[1,0].set_xlabel("Aufrufe")
sns.boxplot(x="status_kl", y="bytes", data=df, palette="Set2", ax=axes[1,1])
axes[1,1].set_title("Datenmenge je Status-Klasse")
plt.setp(axes[1,1].xaxis.get_majorticklabels(), rotation=20, ha="right")

plt.tight_layout(); plt.savefig("mp4_loganalyse.png", dpi=150); plt.show()
df.to_csv("log_analyse.csv", index=False)
print("\nDateien gespeichert: mp4_loganalyse.png, log_analyse.csv")
print("Fazit: Regex ermoeglicht strukturierte Extraktion aus unstrukturierten Logs.")
