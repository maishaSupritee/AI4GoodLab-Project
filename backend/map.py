import folium

m = folium.Map(tiles=None)

folium.TileLayer(tiles="OpenStreetMap", overlay=True, name="OpenStreetMap").add_to(m)

fg = folium.FeatureGroup(name="Icon collection", show=False).add_to(m)
folium.Marker(location=(0, 0)).add_to(fg)

# multiple overlays from datasets example
# folium.GeoJson(sidewalk_data, name="Sidewalks").add_to(m)
# folium.HeatMap(data=lighting_data, name="Lighting Heatmap").add_to(m)
# folium.LayerControl(collapsed=False).add_to(m)

folium.LayerControl().add_to(m)

m.save("../website/public/maps/map.html")
