# !pip install pydeck
# https://pydeck.gl/gallery/column_layer.html
import pandas as pd
import pydeck as pdk

url = 'https://account.geodir.co/resources/file/recursos/geodir-ubigeo-inei.xlsx' 
# Actualizado: 15/01/2019
df = pd.read_excel(url)
df = df[['Departamento', 'Distrito', 'Provincia', 'X', 'Y', 'Poblacion']]


# Initial view
view = pdk.ViewState(
    latitude=-10,
    longitude=-75,
    zoom=6,
    pitch=40, # Inclinación
    min_zoom=5.5,
    max_zoom=8.5,
    bearing=2, # Rotación
)

# Layers
layer = pdk.Layer(
    'ColumnLayer',
    data=df,
    get_position=['X', 'Y'], # Longitud, Latitud
    get_elevation='Poblacion',
    elevation_scale=0.3,
    radius=5_000,
    get_fill_color=[120, 250, 120],
    pickable=True,
    auto_highlight=True,
)

# Map
deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view,
    map_provider='carto',
    map_style='dark',
)

deck.to_html('Resultados/map.html')