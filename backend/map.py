import os
import pandas as pd
import folium
from folium.plugins import HeatMap

csv_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "fake_data.csv")
)
df = pd.read_csv(csv_path)

m = folium.Map(location = [49.22691073805821, -123.12734878115373], zoom_start =12, tiles="CartoDB Positron")

fg = folium.FeatureGroup(name="Icon collection", show=False).add_to(m)
folium.Marker(location=(49.22691073805821, -123.12734878115373), popup = "Vancouver").add_to(fg)

# multiple overlays from datasets example
# folium.GeoJson(sidewalk_data, name="Sidewalks").add_to(m)
# folium.HeatMap(data=lighting_data, name="Lighting Heatmap").add_to(m)
# folium.LayerControl(collapsed=False).add_to(m)

#heat map
heat_data = df[["latitude", "longitude", "weight"]].values.tolist()
hm = HeatMap(heat_data, min_opacity=0.05, max_opacity=0.8, radius=15, blur=10, gradient={0.2: 'purple', 0.4: 'yellow', 0.8: 'orange'})
hm.add_to(m)

folium.LayerControl().add_to(m)

m.save("../website/public/maps/map.html")
