"""Task 2: crop a DEM and shrink it into a small grid for the website.

Usage (run from the data-prep/ folder):
    python crop_dem.py ../data/raw/dem.tif
    python crop_dem.py ../data/raw/dem.tif --bounds XMIN YMIN XMAX YMAX --max-size 500

--bounds are in the file's own CRS (use the Bounds printed by inspect_dem.py).
--max-size is the longest side of the output grid in cells.

Outputs (in ../web/public/data/):
    jezero_grid.json       elevation rows, null where there is no data
    jezero_grid_meta.json  bounds, size, cell size, CRS, units, nodata rule
"""
import argparse
import json
import os
import numpy as np
import rasterio
from rasterio.enums import Resampling
from rasterio.windows import from_bounds

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "web", "public", "data")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("dem")
    p.add_argument("--bounds", nargs=4, type=float, metavar=("XMIN", "YMIN", "XMAX", "YMAX"))
    p.add_argument("--max-size", type=int, default=500)
    p.add_argument("--name", default="jezero")
    a = p.parse_args()

    with rasterio.open(a.dem) as src:
        b = a.bounds or list(src.bounds)
        win = from_bounds(*b, transform=src.transform).round_offsets().round_lengths()
        scale = min(1.0, a.max_size / max(win.width, win.height))
        out_w = max(1, int(win.width * scale))
        out_h = max(1, int(win.height * scale))

        data = src.read(1, window=win, out_shape=(out_h, out_w),
                        resampling=Resampling.average, masked=True)
        win_transform = src.window_transform(win)
        cell_x = abs(win_transform.a) * (win.width / out_w)
        cell_y = abs(win_transform.e) * (win.height / out_h)

        rows = [[None if m else round(float(v), 1) for v, m in zip(r, rm)]
                for r, rm in zip(data.data, np.ma.getmaskarray(data))]

        meta = {
            "source_file": os.path.basename(a.dem),
            "crs": src.crs.to_string() if src.crs else None,
            "width": out_w,
            "height": out_h,
            "bounds": {"xmin": b[0], "ymin": b[1], "xmax": b[2], "ymax": b[3]},
            "cell_size": {"x": cell_x, "y": cell_y},
            "elevation_units": "metres (CHECK against the source metadata)",
            "nodata": "cells with no data are null in the grid",
            "origin": "row 0 is the north edge, column 0 is the west edge",
        }

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, a.name + "_grid.json"), "w") as f:
        json.dump(rows, f, separators=(",", ":"))
    with open(os.path.join(OUT_DIR, a.name + "_grid_meta.json"), "w") as f:
        json.dump(meta, f, indent=2)
    print("Wrote %dx%d grid. Cell size ~%.1f x %.1f (CRS units)." % (out_w, out_h, cell_x, cell_y))


if __name__ == "__main__":
    main()
