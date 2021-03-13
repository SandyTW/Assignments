import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
    data=json.load(response)

spotlist=data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:
    for spot in spotlist:
        url="https:"+spot["file"].split("http:")[1]
        file.write(spot["stitle"]+","+spot["longitude"]+","+spot["latitude"]+","+url+"\n")