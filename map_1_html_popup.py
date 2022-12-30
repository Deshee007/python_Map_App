import pandas
import folium

my_map = folium.Map(location=[38, -98], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Features")

file = pandas.read_csv("Volcanoes.txt")
lats = list(file["LAT"])
lons = list(file["LON"])
eles = list(file["ELEV"])
names = list(file["NAME"])

html = """
<h4>Volcano Description</h4>
Name: %s 
Height: %s m
"""

html_with_link = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
for lat, lon, ele, name in zip(lats, lons, eles, names):
    iframe = folium.IFrame(html=html_with_link % (name, name, ele), width=200, height=100)
    fg.add_child(folium.Marker(location=[lat, lon], popup=folium.Popup(iframe),
                               icon=folium.Icon(color="red")))
my_map.add_child(fg)
my_map.save("Map1_HTML_popup_version.html")
