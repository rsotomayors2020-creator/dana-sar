import os, glob, numpy as np, rasterio
from rich import print
from asf_tools import water_map

RAW = "data/raw"
DEM = "data/dem/dem.tif"
OUT = "data/results"

def pick_rtc(prefix, pol):
    # Elige el primer GeoTIFF que contenga el patrón. Cambia esto si tu nombre difiere.
    cands = glob.glob(os.path.join(RAW, f"*{prefix}*{pol}*.tif"))
    return cands[0] if cands else None

def main():
    os.makedirs(OUT, exist_ok=True)

    vv = pick_rtc("post", "VV")
    vh = pick_rtc("post", "VH")
    if vv is None or vh is None:
        raise FileNotFoundError("No se encontró RTC post VV/VH en data/raw/*.tif. Renombra o ajusta patrones.")

    if not os.path.exists(DEM):
        raise FileNotFoundError(f"Falta DEM: {DEM}")

    print("[bold cyan]Generando mapa de inundación con water_map (VV+VH)...[/]")
    wm = water_map.create_water_map(vv_path=vv, vh_path=vh)
    flood = wm.array.astype(rasterio.uint8)
    profile = wm.profile
    out_flood = os.path.join(OUT, "flood_extent.tif")
    with rasterio.open(out_flood, "w", **profile) as dst:
        dst.write(flood, 1)
    print(f"[green]OK:[/] {out_flood}")

    print("[bold cyan]Generando clases HAND (placeholder por percentiles de DEM dentro de inundación)...[/]")
    with rasterio.open(DEM) as dsrc, rasterio.open(out_flood) as fsrc:
        dem = dsrc.read(1, masked=True)
        flood = fsrc.read(1)
        prof = fsrc.profile.copy()
        prof.update(dtype=rasterio.uint8, nodata=0)

        # Clases relativas (1=baja, 2=media, 3=alta). Sustituir por HAND real si tenéis tiempo.
        classes = np.zeros_like(flood, dtype=np.uint8)
        if np.ma.is_masked(dem):
            dem_arr = dem.filled(np.nan)
        else:
            dem_arr = dem

        # Evitar NaN en percentiles
        valid = np.isfinite(dem_arr)
        p30 = np.nanpercentile(dem_arr[valid], 30)
        p60 = np.nanpercentile(dem_arr[valid], 60)

        classes[(flood == 1) & (dem_arr <= p30)] = 3
        classes[(flood == 1) & (dem_arr > p30) & (dem_arr <= p60)] = 2
        classes[(flood == 1) & (dem_arr > p60)] = 1

        out_hand = os.path.join(OUT, "hand_class.tif")
        with rasterio.open(out_hand, "w", **prof) as dst:
            dst.write(classes, 1)
        print(f"[green]OK:[/] {out_hand}")

if __name__ == "__main__":
    main()
