import os
import pandas as pd
import folium
from folium.plugins import HeatMap
from folium import Html, Popup
from branca.colormap import LinearColormap 

csv_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "output1.csv")
)
df = pd.read_csv(csv_path)

m = folium.Map(location = [49.22691073805821, -123.12734878115373], zoom_start =11, tiles="CartoDB Positron")

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
pavement_cols = [
    'pavement_VERY POOR','pavement_POOR',
    'pavement_FAIR','pavement_GOOD','pavement_VERY GOOD'
]
def pick_pavement(row):
    for col in pavement_cols:
        if row.get(col, 0) == 1:
            # drop the 'pavement_' prefix and title-case
            return col.replace('pavement_', '').title()
    return "Unknown"
df['pavement_text'] = df.apply(pick_pavement, axis=1)

# 2) Construction: yes/no if under_construction == 1
df['construction_text'] = df['under_construction'].map({1: 'Yes', 0: 'No'})

# 3) Curbs: yes/no if you have any curb ramps
df['curbs_text'] = df['curb_ramp_count'].apply(lambda x: 'Yes' if x>0 else 'No')

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
        f"Coordinates: {row['latitude']:.6f}, {row['longitude']:.6f}<br>"
        f"Pavement: {row['pavement_text']}<br>"
        f"Curb Ramps: {row['curbs_text']}<br>"
        f"Streetlight Count: {row['streetlight_count']}<br>"
        f"Construction: {row['construction_text']}<br>"
        f"Score: {row['weight']}"
    )
    html = Html(popup_html, script=True)
    popup = Popup(html, max_width=200)
    marker.add_child(popup)
    marker.add_to(m)

folium.LayerControl().add_to(m)

m.save("../website/public/maps/map.html")
