import numpy
import plotly
from plotly import graph_objs, io

plotly.io.orca.config.executable = r'C:\Users\ArthurGo\AppData\Local\Programs\orca\orca.exe'
N = 100
x = numpy.random.rand(N)
y = numpy.random.rand(N)
colors = numpy.random.rand(N)
sz = numpy.random.rand(N)*30

fig = graph_objs.Figure()
fig.add_scatter(x=x,
                y=y,
                mode='markers',
                marker={'size': sz,
                        'color': colors,
                        'opacity': 0.6,
                        'colorscale': 'Viridis'
                        }
                )
plotly.offline.plot(fig, filename='pointChart.html')

