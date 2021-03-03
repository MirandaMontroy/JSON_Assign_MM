import json


infile = open("US_fires_9_14.json", "r")
outfile = open("fires_9_14.json", "w")


# The json.load() funciton converts the data into a format python can work with
# in this case a giant dictionary
fire_data = json.load(infile)

# The json.dump() function takes a json data object and a file object and file.
# The indent=4 arguement tells dump() to format the data using indent

json.dump(fire_data, outfile, indent=4)
brights, lons, lats = [], [], []



counter = 0

for fire in fire_data:
    if fire_data[counter]["brightness"] > 450:
        bright = fire_data[counter]["brightness"]
        lon = fire_data[counter]["longitude"]
        lat = fire_data[counter]["latitude"]

        brights.append(bright)
        lons.append(lon)
        lats.append(lat)

    counter += 1


# print(brights, lons, lats)
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [.02 *b for b in brights],
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="US Fires- 9/14/2020 through 9/20/2020")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="sep14califires.html")
