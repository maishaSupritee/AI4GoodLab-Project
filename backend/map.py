import os
import pandas as pd
import folium
from folium.plugins import HeatMap

csv_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "output1.csv")
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
weight_map = {1:7, 2:6, 3:5, 4:4, 5:3, 6:2, 0:1} #made up classification weights for clusters, 1 = worst, 7 = best
df['weight'] = df['k=7 clustering'].map(weight_map)
heat_data = df[["latitude", "longitude", "weight"]].dropna().values.tolist()
hm = HeatMap(heat_data, min_opacity=0.05, max_opacity=1.0, radius=15, blur=20, gradient={0.2: 'blue', 0.4: 'cyan', 0.6: 'lime', 0.8: 'yellow', 1.0: 'red'})   

hm.add_to(m)

folium.LayerControl().add_to(m)

m.save("../website/public/maps/map.html")
