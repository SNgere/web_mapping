import folium


min_lat = -4.77352
max_lat = 5.01439
min_lon = 30.09155
max_lon = 45.75806

map = folium.Map(location=[-0.02, 37.91], zoom_start=7)

map.options["minZoom"] = 7
map.options["maxBounds"] = [[min_lat, min_lon], [max_lat, max_lon]]

map.save("map.html")
