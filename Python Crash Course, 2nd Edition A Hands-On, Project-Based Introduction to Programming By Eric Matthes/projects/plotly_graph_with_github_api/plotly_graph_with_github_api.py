import requests
import json
from plotly.graph_objs import Bar
from plotly import offline

response=requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars')
contents=response.json()
items=contents['items']
owner, url, stars=[], [], []
for item in items:
    owner.append(f"<a herf={item['html_url']} target=_self>{item['owner']['login']}</a>")
    url.append(item['html_url'])
    stars.append(item['stargazers_count'])
data=[{"type":"bar", "x":owner, "y":stars, "hovertext":url, "opacity":0.6, "marker":{"color":"rgb(255, 0, 0)", "line":{"width":1.5, "color":"rgb(25, 25, 25)"}}}]
fig={"data":data}
offline.plot(fig, filename="dump/api.html", auto_open=False)