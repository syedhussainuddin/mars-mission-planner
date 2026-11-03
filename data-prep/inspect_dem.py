"""Task 1: check that a DEM (elevation) file is usable.

Usage (run from the data-prep/ folder):
    python inspect_dem.py ../data/raw/your_file.tif

Prints the facts the PRD asks us to record: CRS, cell size, bounds, units/dtype,
no-data value. Reads only a small sample, so it is safe on huge files.
"""
import sys
import numpy as np
import rasterio


def main(path):
    with rasterio.open(path) as src:
        print("File:        ", path)
        print("CRS:         ", src.crs)
        print("Size (cols x rows):", src.width, "x", src.height)
        print("Cell size (x, y):  ", src.res, "(units of the CRS, usually metres)")
        print("Bounds:      ", src.bounds)
        print("Bands:       ", src.count, "| dtype:", src.dtypes[0])
        print("NoData value:", src.nodata)
        print("Units tag:   ", src.units[0] if src.units else None)

        # Read a 500x500 block from the middle of the file
        size = 500
        r0 = max(0, src.height // 2 - size // 2)
        c0 = max(0, src.width // 2 - size // 2)
        win = rasterio.windows.Window(c0, r0, min(size, src.width), min(size, src.height))
        sample = src.read(1, window=win).astype("float64")

        if src.nodata is not None:
            valid = sample[sample != src.nodata]
        else:
            valid = sample[np.isfinite(sample)]

        print("\nSample block (middle of file):")
        if valid.size == 0:
            print("  No valid cells in this block. Try another part of the file.")
        else:
            print("  Valid cells: %.1f%%" % (100 * valid.size / sample.size))
            print("  Min / max / mean:", valid.min(), valid.max(), round(valid.mean(), 2))

        print("\nChecks:")
        if src.crs is None:
            print("  WARNING: no CRS found. We cannot map lat/lon to cells without it.")
        if src.dtypes[0] == "uint8":
            print("  WARNING: uint8 data looks like an image, not elevation in metres.")
        if valid.size and valid.min() > -10000 and valid.max() < 10000:
            print("  OK: values look like plausible elevations in metres.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python inspect_dem.py path/to/dem.tif")
    main(sys.argv[1])
