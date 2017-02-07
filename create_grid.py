

import json

xsize = 0.5
ysize = 0.5

xmin = -180
xmax = 180 - xsize

ymin = -90 + ysize
ymax = 90

ncols = (xmax - xmin) / xsize
nrows = (ymax - ymin) / ysize

feature_list = []

for r in xrange(xmin, xmax, xsize):
    for c in xrange(ymax, ymin, ysize):


    b_xmin =
    b_xmax =
    b_ymin =
    b_ymax =

    geom = {
        "type": "Polygon",
        "coordinates": [ [
            env[0],
            env[1],
            env[2],
            env[3],
            env[0]
        ] ]
    }

    props = {

    }

    feature = {
        "type": "Feature",
        "properties": props,
        "geometry": geom
    }


    feature_list.append(feature)


geo_out = {
    "type": "FeatureCollection",
    "features": feature_list
}

geo_path = "/path/to/output.geojson"
geo_file = open(geo_path, "w")
json.dump(geo_out, geo_file)
geo_file.close()

