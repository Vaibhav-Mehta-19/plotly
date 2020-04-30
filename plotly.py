#!/usr/bin/env python
# coding: utf-8

# In[88]:


import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo


# In[89]:


x= np.random.randint(1,101,100)
y= np.random.randint(1,101,100)


# In[90]:


scplot = [go.Scatter(x=x,y=y,mode='markers')]
layout = go.Layout(title='my graph')


# In[91]:


fig1 = go.Figure(data=scplot,layout=layout)
fig1


# In[92]:


pyo.plot(fig1,filename='mygraph1.html')


# In[93]:


np.random.seed(1)
N = 50
random_x = np.linspace(0, 1, N)
random_y1 = np.random.randn(N)
random_y0 = random_y1 + 5
random_y2 = random_y1 - 5
fig = go.Figure()
fig.add_trace(go.Scatter(x=random_x, y=random_y0,mode='markers',name='markers',fill='tozeroy'))
fig.add_trace(go.Scatter(x=random_x, y=random_y1,mode='lines+markers',name='lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y2,mode='lines',name='lines'))
pyo.plot(fig, filename="scatterline_filledarea.html")
fig.show()


# In[94]:


animals=['g', 'o', 'm']
fig = go.Figure(data=[go.Bar(name='2', x=animals, y=[20, 14, 23]),go.Bar(name='1', x=animals, y=[12, 18, 29])])
fig.update_layout(barmode='group')
pyo.plot(fig, filename="bar.html")
fig.show()


# In[95]:


import plotly.graph_objects as go
colors = ['lightblue', 'red', 'orange', 'green']
fig = go.Figure(data=[go.Pie(labels=['O2','H2','CO2','N@'],
                             values=[4500,2500,1000,500])])
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
pyo.plot(fig, filename="pie.html")
fig.show()


# In[96]:


import plotly.figure_factory as ff
df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]
fig = ff.create_gantt(df)
pyo.plot(fig, filename="gantt.html")
fig.show()


# In[97]:


fig =go.Figure(go.Sunburst(
    labels=["E", "C", "S","N", "A"],
    parents=["", "E", "E", "S", "S"],
    values=[10, 14, 12, 10, 2],
))
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
pyo.plot(fig, filename="sunburst.html")
fig.show()


# In[98]:


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv')
index_vals = df['class'].astype('category').cat.codes

fig = go.Figure(data=go.Splom(
                dimensions=[dict(label='sepal length',values=df['sepal length']),
                            dict(label='sepal width',values=df['sepal width']),
                            dict(label='petal length',values=df['petal length']),
                            dict(label='petal width',values=df['petal width'])],
                diagonal_visible=False,text=df['class'],marker=dict(color=index_vals,showscale=False,line_color='white', line_width=0.5)
                ))
fig.update_layout(title='Iris Data set',width=600,height=600)
pyo.plot(fig, filename="scatter_matrix.html")
fig.show()


# In[99]:


x = np.random.uniform(-1, 1, size=500)
y = np.random.uniform(-1, 1, size=500)
fig = go.Figure(go.Histogram2dContour(x = x,y = y,colorscale = 'Blues'))
pyo.plot(fig, filename="hist_contour_plot.html")
fig.show()


# In[100]:


fig = go.Figure(data =
    go.Contour(
        z=[[10, 10.625, 12.5, 15.625, 20],
           [5.625, 6.25, 8.125, 11.25, 15.625],
           [2.5, 3.125, 5., 8.125, 12.5],
           [0.625, 1.25, 3.125, 6.25, 10.625],
           [0, 0.625, 2.5, 5.625, 10]],
        x=[-9, -6, -5 , -3, -1], # horizontal axis
        y=[0, 1, 4, 5, 7] # vertical axis
    ))
pyo.plot(fig, filename="contour_plot.html")
fig.show()


# In[101]:


from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",dtype={"fips": str})
fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df.fips, z=df.unemp,
                                    colorscale="Viridis", zmin=0, zmax=12,marker_opacity=0.5, marker_line_width=0))
fig.update_layout(mapbox_style="carto-positron",mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
pyo.plot(fig, filename="mapbox.html")
fig.show()


# In[102]:


fig = go.Figure(data=[go.Mesh3d(x=(70*np.random.randn(100)),y=(55*np.random.randn(100)),z=(40*np.random.randn(100)),opacity=0.5,color='rgba(244,22,100,0.6)')])
fig.update_layout(
    scene = dict(
        xaxis = dict(nticks=4, range=[-100,100],),yaxis = dict(nticks=4, range=[-50,100],),zaxis = dict(nticks=4, range=[-100,100],),),width=700,margin=dict(r=20, l=10, b=10, t=10))
pyo.plot(fig, filename="3dmesh.html")
fig.show()


# In[103]:


t = np.linspace(0, 10, 50)
x, y, z = np.cos(t), np.sin(t), t
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,mode='markers')])
pyo.plot(fig, filename="3dscatter.html")
fig.show()


# In[104]:


X, Y, Z = np.mgrid[-5:5:40j, -5:5:40j, -5:5:40j]
values = X * X * 0.5 + Y * Y + Z * Z * 2
fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=10,
    isomax=50,
    surface_count=5, # number of isosurfaces, 2 by default: only min and max
    colorbar_nticks=5, # colorbar ticks correspond to isosurface values
    caps=dict(x_show=False, y_show=False)
    ))
pyo.plot(fig, filename="isospace.html")
fig.show()


# In[105]:


fig = go.Figure(data=go.Streamtube(x=[0, 0, 0], y=[0, 1, 2], z=[0, 0, 0],
                                   u=[0, 0, 0], v=[1, 1, 1], w=[0, 0, 0]))
pyo.plot(fig, filename="streamtube.html")
fig.show()


# In[106]:


X, Y, Z = np.mgrid[-8:8:40j, -8:8:40j, -8:8:40j]
values = np.sin(X*Y*Z) / (X*Y*Z)
fig = go.Figure(data=go.Volume(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=0.1,
    isomax=0.8,
    opacity=0.1, # needs to be small to see through all surfaces
    surface_count=17, # needs to be a large number for good volume rendering
    ))
pyo.plot(fig, filename="volume.html")
fig.show()


# In[ ]:




