# Data preparation

Python scripts that turn raw NASA data into the small files the website loads.

- **Output goes to** `web/public/data/` (slope grid, weather samples, place names). Only small processed files are committed.
- **Raw downloads go in** `data/raw/` at the repo root. Create this folder locally. Do NOT commit it (GitHub rejects files over 100 MB). Add these lines to `.gitignore`:

```
data/raw/
__pycache__/
.venv/
```

## For every data source, record

Original mission/instrument, archive or distributor, product ID, coverage, spatial resolution, coordinate system, time coverage, file format, processing steps, and which feature uses it. See `docs/Data_Sources_and_Integration_Plan.docx`.

## Planned scripts

- Convert the elevation file into a slope grid (numpy, rasterio)
- Extract a small sample of Perseverance MEDA readings (temperature, pressure) into JSON
- Filter USGS place names for the study area (optional)
