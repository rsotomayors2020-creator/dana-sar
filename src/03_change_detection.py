import os, glob, numpy as np, rasterio
from skimage.filters import threshold_otsu
from rich import print

RAW = "data/raw"
OUT = "data/results"

def pick(pattern):
    cands = glob.glob(os.path.join(RAW, f"*{pattern}*.tif"))
    return cands[0] if cands else None

def to_db(arr):
    return 10.0*np.log10(np.clip(arr, 1e-6, None))

def main():
    os.makedirs(OUT, exist_ok=True)

    pre_vv  = pick("pre_VV")
    post_vv = pick("post_VV")
    if pre_vv is None or post_vv is None:
        raise FileNotFoundError("Faltan archivos pre_VV*.tif y/o post_VV*.tif en data/raw/. Ajusta los nombres/patrones.")

    with rasterio.open(pre_vv) as a, rasterio.open(post_vv) as b:
        pre = a.read(1).astype(np.float32)
        post = b.read(1).astype(np.float32)
        prof = b.profile.copy()

    db = to_db(post) - to_db(pre)
    t = threshold_otsu(db[np.isfinite(db)])
    change = (db < t).astype(np.uint8)  # disminuciones fuertes (posible agua)

    prof.update(dtype=rasterio.uint8, nodata=0)
    out_path = os.path.join(OUT, "delta_vv_otsu.tif")
    with rasterio.open(out_path, "w", **prof) as dst:
        dst.write(change, 1)
    print(f"[green]OK:[/] {out_path}")

if __name__ == "__main__":
    main()
