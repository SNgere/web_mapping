import folium


min_lat = -4.77352
max_lat = 5.01439
min_lon = 30.09155
max_lon = 45.75806

map = folium.Map(location=[-0.02, 37.91], zoom_start=7)

map.options["minZoom"] = 7
map.options["maxBounds"] = [[min_lat, min_lon], [max_lat, max_lon]]

folium.TileLayer(
    "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    name="Satellite",
    show=False,
    attr="Google",
).add_to(map)


folium.GeoJson(
    "ken_bound.geojson",
    style_function=lambda feature: {
        "color": "#FF0000",
        "weight": 3,
    },
    control=False,
).add_to(map)


folium.GeoJson(
    "interland_bound.geojson",
    style_function=lambda feature: {
        "color": "#FF0000",
        "weight": 3,
    },
    control=False,
).add_to(map)

folium.LayerControl(position="bottomright", collapsed=False).add_to(map)


map.save("map.html")
