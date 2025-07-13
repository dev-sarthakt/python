import json
from plotly.graph_objs import Scattergeo
from plotly import offline

with open('dump/eq_data_30_day_m1.json', 'r') as eq:
    contents=json.load(eq)

mags=[]
lon=[]
lat=[]
title=[]
features=contents["features"]
for feature in features:
    mags.append(feature["properties"]["mag"])
    lon.append(feature["geometry"]["coordinates"][0])
    lat.append(feature["geometry"]["coordinates"][1])
    title.append(feature["properties"]["title"])

data=[Scattergeo(lon=lon, lat=lat, text=title, marker={"size":list(4*mag for mag in mags), "color":mags, "colorscale":"viridis", "reversescale":True, "colorbar":{"title":"Magnitude"}})]
fig={"data":data}
offline.plot(fig, filename="earthquake.html", auto_open=False)