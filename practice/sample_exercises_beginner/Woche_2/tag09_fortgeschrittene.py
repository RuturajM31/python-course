# tag09_fortgeschrittene.py
# Lerntag 9 - Seaborn: Fortgeschrittene statistische Grafiken
# Thema: FacetGrid, clustermap, kdeplot, jointplot, CI-Band, 300dpi
# Ausfuehren in Spyder: F5

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
sns.set_theme(style="ticks", palette="deep")

print("=" * 60)
print("LERNTAG 9 - Seaborn fuer Fortgeschrittene")
print("=" * 60)
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

# AUFGABE 1: FacetGrid
print("\nAUFGABE 1: FacetGrid")
g = sns.FacetGrid(tips, col="day", col_wrap=2, height=3)
g.map(sns.histplot, "tip", bins=10, color="steelblue")
g.set_titles("{col_name}"); g.figure.suptitle("Trinkgeld je Wochentag", y=1.03)
plt.tight_layout(); plt.savefig("plot_09f_01.png", dpi=100); plt.show()
# LOESUNG: FacetGrid(df, col=kategorie) erzeugt Raster automatisch.

# AUFGABE 2: regplot + residplot
print("\nAUFGABE 2: regplot + residplot")
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,4))
sns.regplot(x="total_bill",y="tip",data=tips,scatter_kws={"alpha":0.4},line_kws={"color":"red"},ax=ax1)
ax1.set_title("Regression")
sns.residplot(x="total_bill",y="tip",data=tips,scatter_kws={"alpha":0.4},ax=ax2)
ax2.set_title("Residuen"); plt.tight_layout()
plt.savefig("plot_09f_02.png", dpi=100); plt.show()

# AUFGABE 3: clustermap
print("\nAUFGABE 3: clustermap")
g = sns.clustermap(iris.drop("species",axis=1),standard_scale=1,cmap="YlOrRd",figsize=(7,6),yticklabels=False)
g.figure.suptitle("Iris - Clustering", y=1.01)
plt.savefig("plot_09f_03.png", dpi=100); plt.show()

# AUFGABE 4: Eigene Palette + Kontext
print("\nAUFGABE 4: Palette + Kontext")
with sns.plotting_context("talk"):
    fig,ax = plt.subplots(figsize=(8,4))
    wt = tips.groupby("day")["total_bill"].mean().reset_index()
    sns.barplot(x="day",y="total_bill",data=wt,palette=sns.color_palette("husl",4),ax=ax)
    ax.set_title("Durchschn. Rechnung (talk-Kontext)"); plt.tight_layout()
    plt.savefig("plot_09f_04.png", dpi=100); plt.show()

# AUFGABE 5: kdeplot - mehrere Gruppen
print("\nAUFGABE 5: kdeplot")
fig,ax = plt.subplots()
for tag in tips["day"].unique():
    sns.kdeplot(tips[tips["day"]==tag]["total_bill"], label=tag, fill=True, alpha=0.25, ax=ax)
ax.set_title("KDE nach Tag"); ax.legend(); plt.tight_layout()
plt.savefig("plot_09f_05.png", dpi=100); plt.show()

# AUFGABE 6: Jointplot
print("\nAUFGABE 6: Jointplot")
g = sns.jointplot(x="total_bill",y="tip",data=tips,kind="reg",height=5,ratio=4,
                  joint_kws={"scatter_kws":{"alpha":0.3}})
g.figure.suptitle("Joint: Rechnung vs. Trinkgeld", y=1.01)
plt.tight_layout(); plt.savefig("plot_09f_06.png", dpi=100); plt.show()

# AUFGABE 7: Heatmap - unteres Dreieck
print("\nAUFGABE 7: Heatmap Maske")
corr = tips.select_dtypes(include="number").corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
fig,ax = plt.subplots(figsize=(5,4))
sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm",
            vmin=-1, vmax=1, linewidths=0.5, ax=ax)
ax.set_title("Korrelation - unteres Dreieck"); plt.tight_layout()
plt.savefig("plot_09f_07.png", dpi=100); plt.show()

# AUFGABE 8: Stripplot + Boxplot kombiniert
print("\nAUFGABE 8: Strip + Box")
fig,axes = plt.subplots(1,2,figsize=(10,4))
sns.stripplot(x="day",y="tip",hue="sex",data=tips,dodge=True,alpha=0.5,ax=axes[0])
axes[0].set_title("Stripplot")
sns.boxplot(x="day",y="tip",hue="sex",data=tips,palette="Set2",ax=axes[1])
axes[1].set_title("Boxplot"); plt.tight_layout()
plt.savefig("plot_09f_08.png", dpi=100); plt.show()

# AUFGABE 9: Zeitreihe mit 95%-CI
print("\nAUFGABE 9: CI-Band")
np.random.seed(9)
df_r = pd.DataFrame({
    "Woche":  list(range(20))*5,
    "Umsatz": (np.tile(np.linspace(100,200,20),5)+np.random.normal(0,15,100)),
    "Rep":    [f"R{i}" for i in range(5) for _ in range(20)]
})
fig,ax = plt.subplots(figsize=(8,4))
sns.lineplot(x="Woche",y="Umsatz",data=df_r,estimator="mean",errorbar=("ci",95),ax=ax)
ax.set_title("Wochenumsatz - Mittelwert + 95%-CI"); plt.tight_layout()
plt.savefig("plot_09f_09.png", dpi=100); plt.show()

# AUFGABE 10: Publikationsqualitaet 300 dpi
print("\nAUFGABE 10: 300 dpi")
with sns.axes_style("white"):
    fig,ax = plt.subplots(figsize=(6,4))
    sns.scatterplot(x="sepal_length",y="petal_length",hue="species",
                    style="species",data=iris,palette="deep",s=60,ax=ax)
    ax.set_title("Iris: Kelch- vs. Bluetenblattlaenge"); sns.despine()
    plt.tight_layout(); plt.savefig("plot_09f_10.png", dpi=300, bbox_inches="tight"); plt.show()
plt.close("all")
print("300-dpi-Datei gespeichert.")

print("\n" + "=" * 60)
print("Tag 9 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
