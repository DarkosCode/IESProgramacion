import seaborn
import matplotlib.pyplot as plt

def mapa_calor(df):
    # cmap Reds Blues Greens coolwarm viridis plasma magma cividis
    seaborn.heatmap(df.select_dtypes("number").corr(),annot=True, cmap="cividis")
    plt.show()