import json, os
p = "../web/public/data/jezero_grid.json"
g = json.load(open(p))
vals = [v for row in g for v in row if v is not None]
total = len(g) * len(g[0])
print("Grid:", len(g[0]), "x", len(g))
print("Empty (null) cells: %.2f%%" % (100 * (total - len(vals)) / total))
print("Elevation min/max/mean:", min(vals), max(vals), round(sum(vals) / len(vals), 1))
print("File size: %.1f MB" % (os.path.getsize(p) / 1e6))