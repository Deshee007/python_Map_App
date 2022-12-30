import folium
import pandas

# A BASIC MAP APPLICATION

data_file = pandas.read_csv("Volcanoes.txt")
latitude = list(data_file["LAT"])
longitude = list(data_file["LON"])
elevations = list(data_file["ELEV"])
names = list(data_file["NAME"])


def get_color(height):
    if height <= 1500:
        return "green"
    elif 1500 < height < 2500:
        return "orange"
    else:
        return "red"


my_map = folium.Map(location=[38.5, -99.9], zoom_start=6, tiles="Stamen Terrain")

# points =[[38.5, -99.9], [37.6, -95]]
feature_group = folium.FeatureGroup(name="Map Features")
for lat, lon, ele, name in zip(latitude, longitude, elevations, names):
    feature_group.add_child(folium.CircleMarker(location=(lat, lon), radius=7,
                                                popup=name + " " + str(ele) + "m"), fill=True,
                            fillcolor=get_color(ele), color="grey")
# Can also use popup=folium.Popup(str(ele), parse_html=True)

my_map.add_child(feature_group)
my_map.add_child(folium.LayerControl())
my_map.save("Map1.html")
