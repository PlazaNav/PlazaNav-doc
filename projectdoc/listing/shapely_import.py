# convert to WKB
wkbfab = osmium.geom.WKBFactory()
wkb = wkbfab.create_linestring(osmium_area)

# load into shapely object
shapely_area = shapely.wkb.loads(wkb, hex=True)
