import os
import pandas as pd
import folium
from folium.plugins import HeatMap
from branca.colormap import LinearColormap 

csv_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "output1.csv")
)
df = pd.read_csv(csv_path)

m = folium.Map(location = [49.22691073805821, -123.12734878115373], zoom_start =12, tiles="CartoDB Positron")

fg = folium.FeatureGroup(name="Icon collection", show=False).add_to(m)

# multiple overlays from datasets example
# folium.GeoJson(sidewalk_data, name="Sidewalks").add_to(m)
# folium.HeatMap(data=lighting_data, name="Lighting Heatmap").add_to(m)
# folium.LayerControl(collapsed=False).add_to(m)

#heat map
weight_map = {1:7, 2:6, 3:5, 4:4, 5:3, 6:2, 0:1} #made up classification weights for clusters, 1 = worst, 7 = best
df['weight'] = df['k=7 clustering'].map(weight_map)
heat_data = df[["latitude", "longitude", "weight"]].dropna().values.tolist()
hm = HeatMap(heat_data, min_opacity=0.05, max_opacity=1.0, radius=15, blur=20, gradient={0.2: 'blue', 0.4: 'cyan', 0.6: 'lime', 0.8: 'yellow', 1.0: 'red'})   
hm.add_to(m)

#heat map color legend
colormap = LinearColormap(colors=['blue','cyan','lime','yellow','red'], vmin=1, vmax=7,caption="Accessibility Score (1 = best, 7 = worst)")
colormap.add_to(m) 

#pop up markers
for _, row in df.iterrows():
    # Place an invisible marker at each point
    marker = folium.CircleMarker(
        location=(row["latitude"], row["longitude"]),
        radius=8,
        color=None,
        fill=True,
        fill_opacity=0
    )
    # Build a popup from that row’s data
    popup_html = (
        f"Coordinates: {row['latitude']:.6f}, {row['longitude']:.6f} "
        f"Score: {row['weight']}"
    )
    popup = folium.Popup(popup_html, max_width=200, parse_html=True)
    marker.add_child(popup)
    marker.add_to(m)

folium.LayerControl().add_to(m)

m.save("../website/public/maps/map.html")
