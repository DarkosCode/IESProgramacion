import matplotlib.pyplot as plt

def piramide_poblacional(hombres, mujeres):
    bins = list(range(0, 90, 10))
    hombres_counts = []
    mujeres_counts = []
    for i in range(len(bins)-1):
        low, high = bins[i], bins[i+1]
        hombres_counts.append(sum((low <= e < high) for e in hombres))
        mujeres_counts.append(sum((low <= e < high) for e in mujeres))
    y = [low + (bins[1]-bins[0])/2 for low in bins[:-1]]
    plt.barh(y, [-c for c in hombres_counts], height=10, color="blue", alpha=0.6, label="Hombres", edgecolor="black")
    plt.barh(y, mujeres_counts, height=10, color="red", alpha=0.6, label="Mujeres", edgecolor="black")
    plt.axvline(0, color="black", linewidth=1)
    plt.xticks(range(-3, 4, 1))
    plt.yticks(range(0, 91, 10))
    plt.ylim(0, 90)
    plt.xlabel("Frecuencia")
    plt.ylabel("Edad")
    plt.title("Pirámide poblacional")
    plt.legend()
    plt.show()