// Task 3: convert between map coordinates and elevation-grid cells.
//
// Contract (from the PRD): coordinates are plain numeric decimal degrees,
//   { lat: 18.38, lon: 77.50 }
// Document the latitude convention and longitude range we agree on here:
//   TODO: latitude convention (planetocentric or planetographic)
//   TODO: longitude range (0..360 east, or -180..180)
//
// The grid and its metadata come from web/public/data/jezero_grid.json and
// jezero_grid_meta.json (made by data-prep/crop_dem.py).

/**
 * Convert a map coordinate to a grid cell.
 * @param {{lat:number, lon:number}} point
 * @param {object} meta  contents of jezero_grid_meta.json
 * @returns {{row:number, col:number} | null}  null if outside the grid
 */
export function latLonToCell(point, meta) {
  // TODO: convert lat/lon into the DEM's CRS, then into row/col using
  // meta.bounds and meta.cell_size. Return null outside the grid.
  throw new Error("latLonToCell is not implemented yet");
}

/**
 * Convert a grid cell back to a map coordinate (cell centre).
 * @param {{row:number, col:number}} cell
 * @param {object} meta
 * @returns {{lat:number, lon:number}}
 */
export function cellToLatLon(cell, meta) {
  // TODO: reverse of latLonToCell.
  throw new Error("cellToLatLon is not implemented yet");
}
