import rasterio
import numpy as np
import geopandas as gpd
import pandas as pd
from rasterio import features

FLOOD   = "data/results/flood_extent.tif"
ROADS   = "data/aoi/roads.gpkg"
BRIDGES = "data/aoi/bridges.gpkg"
OUTCSV  = "data/impact/impacto_infra.csv"

def main():
    with rasterio.open(FLOOD) as src:
        band = src.read(1)
        transform = src.transform
        resx = src.res[0]

    roads = gpd.read_file(ROADS)
    bridges = gpd.read_file(BRIDGES)
    roads = roads.to_crs(4326) if roads.crs is None else roads
    bridges = bridges.to_crs(roads.crs) if bridges.crs != roads.crs else bridges

    # Buffer mínimo para rasterizar líneas (en metros si CRS proyectado; si geográfico, conviene reproyectar a UTM)
    # Para simplicidad, asumimos ya en CRS proyectado. Si no, reproyectar a EPSG adecuado antes.
    roads_buf = roads.copy()
    try:
        roads_buf["geometry"] = roads_buf.geometry.buffer(5)
    except Exception:
        # Si el CRS no es proyectado, avisa:
        print("Aviso: reproyecta carreteras a un CRS proyectado para un buffer fiable (p.ej., EPSG:25830).")

    with rasterio.open(FLOOD) as src:
        roads_r = features.rasterize(
            ((geom, 1) for geom in roads_buf.geometry if geom is not None),
            out_shape=src.shape,
            transform=src.transform,
            fill=0,
            dtype="uint8"
        )
        flood = src.read(1)

    affected = (flood == 1) & (roads_r == 1)
    km = (affected.sum() * resx) / 1000.0  # aproximación

    # Puentes afectados: muestrear valor de flood bajo cada punto/línea
    bridges_aff = 0
    with rasterio.open(FLOOD) as src:
        for _, row in bridges.iterrows():
            geom = row.geometry
            # si es punto
            if geom.geom_type == "Point":
                col, rowpx = ~src.transform * (geom.x, geom.y)
                col, rowpx = int(col), int(rowpx)
                if 0 <= rowpx < src.height and 0 <= col < src.width:
                    if src.read(1)[rowpx, col] == 1:
                        bridges_aff += 1
            else:
                # para líneas: rasterizar y chequear intersección
                br_r = features.rasterize([(geom, 1)], out_shape=src.shape, transform=src.transform, fill=0)
                if np.any((br_r == 1) & (src.read(1) == 1)):
                    bridges_aff += 1

    out = pd.DataFrame([{
        "km_carretera_afectada": round(km, 3),
        "num_puentes_afectados": int(bridges_aff)
    }])
    out.to_csv(OUTCSV, index=False)
    print(f"[green]OK:[/] {OUTCSV}")

if __name__ == "__main__":
    main()
