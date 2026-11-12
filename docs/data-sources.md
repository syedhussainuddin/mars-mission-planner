# Data sources record

One entry per dataset we actually use. Fill this in as you go (PRD section 4.1).

## Elevation (Tasks 1 and 2)

- **Dataset title:** High-Resolution Imaging Science Experiment Digital Terrain Model Mosaic for Mars Sample Return Terrain Relative Navigation
- **Identifier / file:** MSR_hirise_soc_003_DTM_MOLATopography_DeltaGeoid_1m_Eqc_latTs0_lon0_Blend40.tif (DOI 10.5066/P13CPYYU)
- **Mission / instrument:** Mars Reconnaissance Orbiter, HiRISE (8 stereo pairs), aligned to MOLA and the Mars 2020 CTX DTM
- **Archive or distributor:** USGS Astrogeology Science Center
- **Official source URL:** https://astrogeology.usgs.gov/search/map/mars-sample-return-terrain-relative-navigation-hirise-dtm-mosaic
- **Retrieval date:** (write the date you downloaded it)
- **License:** CC0 1.0
- **Publication date:** 2024-08-16
- **Area covered:** 77.0578 to 77.3808 E, 18.1356 to 18.5880 N (western Jezero rim and floor)
- **Cell size:** 1 m, 19,144 x 26,816 cells, float32, one band
- **CRS:** Equirectangular, central meridian 0, standard parallel 0, Mars 2000 sphere radius 3,396,190 m
- **Bounds in CRS (metres):** left 4567580, bottom 1074986, right 4586724, top 1101802
- **Latitude / longitude convention:** spherical datum, so planetocentric equals planetographic; longitude east-positive
- **Elevation units:** metres, vertical reference Mars 2000
- **No-data value:** -32767
- **Processing steps:** cropped to bounds 4573152 1084394 4581152 1092394 and averaged down to a 500 x 500 grid (about 16 m cells) with data-prep/crop_dem.py, no-data cells saved as null
- **Output files:** web/public/data/jezero_grid.json and jezero_grid_meta.json
- **Used by feature:** slope grid, A* routing, elevation profile
- **Known limitations:** stereo-derived heights have random noise that can exaggerate slope; faint seams and block artifacts; hand-edited areas are smoother; vertical offsets under 2.3 m (99th percentile), larger on the Jezero crater rim
- **Measured, derived or modelled:** derived (from HiRISE stereo imagery)

## Fallback decision

If the preferred DEM could not be used, record what you chose instead and why.
