import json, os
from rich import print
from asf_search import geo_search

AOI = "data/aoi/aoi.geojson"
MAX_RESULTS = 10

# TODO: AJUSTAR FECHAS PRE/POST A TU EVENTO
DATE_PRE_START  = "2025-09-10"
DATE_PRE_END    = "2025-09-20"
DATE_POST_START = "2025-09-29"
DATE_POST_END   = "2025-10-03"

def load_aoi(path):
    with open(path) as f:
        return json.load(f)

def search_and_download(label, start, end):
    aoi = load_aoi(AOI)
    print(f"[bold cyan]Buscando escenas {label} ({start} → {end})...[/]")
    results = geo_search(
        geojson=aoi,
        platform="Sentinel-1",
        processingLevel="RTC",     # si devuelve 0, probad 'GRD' y generad RTC en HyP3
        start=start, end=end,
        maxResults=MAX_RESULTS
    )
    if not results:
        print(f"[yellow]Sin resultados {label}. Probad GRD + HyP3 RTC.[/]")
        return
    os.makedirs("data/raw", exist_ok=True)
    for r in results:
        # Nota: algunos resultados devuelven .zip con varios GeoTIFF dentro.
        out_dir = "data/raw"
        print(f"↓ {label}: {r.properties.get('fileID')}")
        r.download(path=out_dir)

def main():
    if not os.path.exists(AOI):
        raise FileNotFoundError(f"Falta AOI: {AOI}")
    search_and_download("pre", DATE_PRE_START, DATE_PRE_END)
    search_and_download("post", DATE_POST_START, DATE_POST_END)
    print("[green]Descarga completada (si hubo resultados).[/]")

if __name__ == "__main__":
    main()
