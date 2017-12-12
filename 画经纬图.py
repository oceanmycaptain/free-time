import plotly.plotly as py
from plotly.graph_objs import *
import numpy as np
import pandas as pd
import plotly
'''根据给的经纬度画出各个经纬度标记的地图并且标记车站站号'''
plotly.tools.set_credentials_file(username='oceanmycaptain',api_key='nWgj08P8DVRGlJNqEiqk')


all_lat = []
all_lon = []
all_sta = []
all_color = []
data = pd.read_excel('C:/Users/a/Desktop/2345.xls')
mapbox_access_token = 'Station'
#print(data['latlon'])
for line1 in data['lat']:
    all_lat.append(line1)
for line2 in data['lon']:
    all_lon.append(line2)
for line3 in data['sta']:
    all_sta.append(line3)
    #all_color.append('red')
data =Data([Scattermapbox(lat = all_lat,lon = all_lon,mode = 'markers',marker = Marker(size=9),text = all_sta)])
layout = Layout(autosize=True,hovermode='closest',mapbox = dict(accesstoken = mapbox_access_token,bearing = 0,center = dict(lat = 120.11,lon = 33.3),pitch = 0,zoom = 10))
fig = dict(data=data,layout = layout)
py.iplot(fig,filename = 'Station')





