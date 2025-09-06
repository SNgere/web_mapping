import folium
import pandas as pd
import geopandas as gpd
from folium.plugins import MarkerCluster  # MousePosition, GroupedLayerControl,


min_lat = -4.77352
max_lat = 5.01439
min_lon = 30.09155
max_lon = 45.75806

map = folium.Map(location=[-0.02, 37.91], zoom_start=7)

map.options["minZoom"] = 7
map.options["maxBounds"] = [[min_lat, min_lon], [max_lat, max_lon]]


def load_points():
    df = pd.read_csv("sok.csv")
    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326"
    )
    return gdf


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

marker_cluster = MarkerCluster().add_to(map)

gdf = load_points()

for index, row in gdf.iterrows():
    popup_text = f"""
    <div style='width: 250px; font-family: Arial;'>
        <h4 style='margin: 0; color: #2c3e50;'>🏢 {row["Land Registry"]} Office</h4>
        <hr style='margin: 5px 0;'>
        <p><b>📞 Phone:</b> {row["Phone"]}</p>
        <p><b>📧 Email:</b> {row["Email"]}</p>
        <p><b>🕒 Hours:</b> {row["Hours"]}</p>
        <p><b>🔧 Services:</b> {row["Services"]}</p>
        <img src="https://plus.unsplash.com/premium_photo-1664041040572-3d9f11a6fa88?q=80&w=1700&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"; style="width:100%; height:auto; border-radius:4px;">
    </div>
    """
    popup = folium.Popup(popup_text, max_width=250, keep_in_view=False)

    tooltip_text = f"📍 {row['Land Registry']} Survey Office"

    # Set color based on AdmStatus
    if row["Land Registry"] == "Ruaraka":
        icon_color = "red"
    else:
        icon_color = "darkblue"

    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        sticky=True,
        popup=popup,
        tooltip=tooltip_text,
        icon=folium.Icon(
            color=icon_color, icon="building", prefix="fa", icon_color="white"
        ),
    ).add_to(marker_cluster)

folium.LayerControl(position="bottomright", collapsed=False).add_to(map)


map.save("map.html")


# https://unsplash.com/photos/a-red-pin-is-in-a-maze-of-cubes-Zm_MpFBGbDw
