import plotly.express as px
import plotly.io as pio

# browser | colab | iframe | notebook | vscode
pio.renderers.default = "browser"

def histograma(edades):
    fig = px.histogram(edades, nbins=10, range_x=[0,100], title="Histograma con rango definido")
    fig.update_traces(marker={
        "color":"orange",
        "line":{"color":"darkblue", "width":2}
    })
    fig.show()