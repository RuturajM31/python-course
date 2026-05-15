# tag08_fortgeschrittene.py
# Lerntag 8 - Matplotlib: Fortgeschrittene Visualisierungen
# Thema: twinx, GridSpec, Heatmap, Fehlerbalken, 3D, Animation
# Ausfuehren in Spyder: F5

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

print("=" * 60)
print("LERNTAG 8 - Matplotlib fuer Fortgeschrittene")
print("=" * 60)

# AUFGABE 1: twinx - zwei Y-Achsen
print("\nAUFGABE 1: twinx")
x = np.arange(12)
temp = [3,4,8,14,19,23,25,24,20,14,8,4]
nied = [55,45,52,48,60,70,65,72,58,50,62,68]
fig, ax1 = plt.subplots(figsize=(9,4)); ax2 = ax1.twinx()
ax1.plot(x, temp, "r-o", label="Temp C"); ax2.bar(x, nied, alpha=0.4, color="steelblue")
ax1.set_ylabel("Temperatur C", color="red"); ax2.set_ylabel("Niederschlag mm", color="steelblue")
ax1.set_xticks(x); ax1.set_xticklabels(["J","F","M","A","M","J","J","A","S","O","N","D"])
plt.title("Klimadiagramm"); plt.tight_layout()
plt.savefig("plot_08f_01.png", dpi=100); plt.show()
# LOESUNG: twinx() erzeugt zweite Y-Achse mit gemeinsamer X-Achse.

# AUFGABE 2: GridSpec
print("\nAUFGABE 2: GridSpec")
np.random.seed(1)
fig = plt.figure(figsize=(10,6)); gs = gridspec.GridSpec(2,2)
ax_top = fig.add_subplot(gs[0,:]); ax_bl = fig.add_subplot(gs[1,0]); ax_br = fig.add_subplot(gs[1,1])
x = np.linspace(0,10,200)
ax_top.plot(x, np.sin(x)*np.exp(-x/5), color="purple"); ax_top.set_title("Gedaempfter Sinus")
ax_bl.hist(np.random.randn(300), bins=20, color="teal"); ax_bl.set_title("Histogramm")
ax_br.scatter(*np.random.randn(2,100), alpha=0.5, color="tomato"); ax_br.set_title("Streuung")
plt.tight_layout(); plt.savefig("plot_08f_02.png", dpi=100); plt.show()
# LOESUNG: GridSpec(rows,cols) + add_subplot(gs[r,c]).

# AUFGABE 3: Heatmap mit imshow
print("\nAUFGABE 3: Heatmap")
np.random.seed(2); corr = np.corrcoef(np.random.randn(50,4).T)
labels = ["Umsatz","Kosten","Gewinn","Kunden"]
fig, ax = plt.subplots(figsize=(5,4))
im = ax.imshow(corr, cmap="RdBu_r", vmin=-1, vmax=1); plt.colorbar(im, ax=ax)
ax.set_xticks(range(4)); ax.set_yticks(range(4))
ax.set_xticklabels(labels); ax.set_yticklabels(labels)
for i in range(4):
    for j in range(4): ax.text(j,i,f"{corr[i,j]:.2f}",ha="center",va="center",fontsize=9)
plt.title("Korrelationsmatrix"); plt.tight_layout()
plt.savefig("plot_08f_03.png", dpi=100); plt.show()

# AUFGABE 4: Fehlerbalken
print("\nAUFGABE 4: Fehlerbalken")
x = np.arange(1,7); y = np.array([2.3,3.1,4.0,3.7,5.2,4.8]); ye = np.array([0.3,0.4,0.2,0.5,0.3,0.4])
fig,ax = plt.subplots(); ax.errorbar(x,y,yerr=ye,fmt="o-",capsize=5,color="navy",ecolor="gray")
ax.set_title("Messwerte + Fehlerbalken"); ax.grid(alpha=0.4)
plt.tight_layout(); plt.savefig("plot_08f_04.png", dpi=100); plt.show()

# AUFGABE 5: fill_between
print("\nAUFGABE 5: fill_between")
np.random.seed(3); x = np.linspace(0,10,100); y = 2*x+1
fig,ax = plt.subplots()
ax.scatter(x, y+np.random.normal(0,2,100), s=10, alpha=0.4, color="gray")
ax.plot(x,y,color="blue",label="Regressionslinie")
ax.fill_between(x,y-5,y+5,alpha=0.2,color="blue",label="95%-Band")
ax.legend(); plt.tight_layout(); plt.savefig("plot_08f_05.png", dpi=100); plt.show()

# AUFGABE 6: Logarithmische Achsen
print("\nAUFGABE 6: Log-Skala")
x = np.arange(1,21); y = 2**x
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,4))
ax1.plot(x,y,"b-o"); ax1.set_title("Lineare Y-Achse"); ax1.grid(True)
ax2.semilogy(x,y,"r-o"); ax2.set_title("Log Y-Achse"); ax2.grid(True,which="both")
plt.suptitle("2^x: linear vs. log"); plt.tight_layout()
plt.savefig("plot_08f_06.png", dpi=100); plt.show()

# AUFGABE 7: Polarplot (Windrose)
print("\nAUFGABE 7: Polarplot")
richtungen = np.linspace(0,2*np.pi,9)[:-1]; staerken = [6,8,5,9,7,4,3,6]
fig,ax = plt.subplots(subplot_kw={"projection":"polar"})
ax.bar(richtungen,staerken,width=2*np.pi/8,alpha=0.7,color="steelblue")
ax.set_xticks(richtungen); ax.set_xticklabels(["N","NO","O","SO","S","SW","W","NW"])
ax.set_title("Windrose",va="bottom"); plt.tight_layout()
plt.savefig("plot_08f_07.png", dpi=100); plt.show()

# AUFGABE 8: Style-Sheet
print("\nAUFGABE 8: Style-Sheet")
with plt.style.context("seaborn-v0_8-whitegrid"):
    fig,ax = plt.subplots(); np.random.seed(10)
    for i in range(3): ax.plot(np.cumsum(np.random.randn(50)),label=f"Linie {i+1}")
    ax.legend(); ax.set_title("Zufallspfade (seaborn)")
    plt.tight_layout(); plt.savefig("plot_08f_08.png", dpi=100); plt.show()

# AUFGABE 9: 3D-Surface
print("\nAUFGABE 9: 3D-Surface")
x = np.linspace(-5,5,60); y = np.linspace(-5,5,60)
X,Y = np.meshgrid(x,y); Z = np.sin(np.sqrt(X**2+Y**2))
fig = plt.figure(); ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X,Y,Z,cmap="viridis",alpha=0.85)
ax.set_title("z = sin(sqrt(x2+y2))"); plt.tight_layout()
plt.savefig("plot_08f_09.png", dpi=100); plt.show()

# AUFGABE 10: FuncAnimation
print("\nAUFGABE 10: FuncAnimation")
from matplotlib.animation import FuncAnimation
fig,ax = plt.subplots(); x = np.linspace(0,4*np.pi,200)
line, = ax.plot(x,np.sin(x)); ax.set_ylim(-1.5,1.5); ax.grid(True)
ax.set_title("Wandernder Sinus")
def update(f): line.set_ydata(np.sin(x-f*0.2)); return line,
ani = FuncAnimation(fig,update,frames=50,interval=60,blit=True)
try:
    ani.save("plot_08f_10_anim.gif",writer="pillow",fps=20)
    print("GIF gespeichert.")
except Exception as e:
    print(f"GIF-Export: {e}  -> plt.show() statt dessen."); plt.show()
plt.close("all")

print("\n" + "=" * 60)
print("Tag 8 - Fortgeschrittene: Alle 10 Aufgaben abgeschlossen!")
print("=" * 60)
