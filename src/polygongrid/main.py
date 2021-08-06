
import os
import json
import time
import itertools
from shapely.geometry import box


class PolygonGrid(object):

    def __init__(self, bounds, step_size=None, dim_size=None, properties=None):
        """
        bounds = Required, bbox object or tuple of (xmin, ymin, xmax, ymax)
        step_size = Optional, tuple of x and y step sizes (resolution). Either step_size or dim_size must be provided
        dim_size = Optional, tuple of x and y dimension sizes. Either step_size or dim_size must be provided
        properties = Optional, str or list of properties to be added to each grid feature's properties.
            Options include:
                grid -  add cell id and row and column index to properties
                center - lon, lat coordinates of the center of the cell
                bounds or box - bounding box (xmin, xmax, ymin, ymax) of the cell
                all - all of the above
        """

        # validate inputs

        if not properties:
            self.properties = []
        else:
            self.properties = properties

        if len(bounds) != 4:
            raise ValueError("bounds must be a tuple of length 4")

        self.xmin, self.xmax, self.ymin, self.ymax = bounds


        if step_size:
            if isinstance(step_size, (tuple, list)) and len(step_size) == 1:
                step_size = step_size[0]
            if isinstance(step_size, (int, float)):
                xstep = ystep = step_size
            elif len(step_size) == 2:
                xstep, ystep = step_size
            else:
                raise ValueError(f"Invalid step size(s) provide ({step_size})")


            self.xmax = self.xmax - xstep
            self.ymin = self.ymin + ystep

            ncols = int((self.xmax - self.xmin) / xstep) + 1
            nrows = int((self.ymax - self.ymin) / ystep) + 1


        if dim_size:
            if len(dim_size) == 2 and all(map(lambda x: isinstance(x, int), dim_size)):
                xdim, ydim = dim_size
                dim_xstep = (self.xmax - self.xmin) / (xdim - 1)
                dim_ystep = (self.ymax - self.ymin) / (ydim - 1)
            else:
                raise ValueError(f"Invalid dim_size: ({dim_size}) \n\tMust provide size for 2 dimensions as integers. ")

            if step_size and (ncols, nrows) != (xdim, ydim) and (xstep, ystep) != (dim_xstep, dim_ystep):
                raise ValueError(f"Step size and dimension sizes both provided, but do not result in matching dimensions or step sizes. \n\t Step size: {step_size} produces dimension {ncols}, {nrows}\n\tDim size: {dim_size} produces step size {dim_xstep}, {dim_ystep}")
            else:
                ncols, nrows = (xdim, ydim)
                xstep, ystep = dim_xstep, dim_ystep




        if step_size or dim_size:
            self.xstep, self.ystep = xstep, ystep
            self.ncols, self.nrows = ncols, nrows
            # generate iterable for all col and row pairings
            # start in top left and go row by row
            self.index_iter = itertools.product(range(ncols), range(nrows))
        # elif index_list:
        #     # must be iterable containing tuples of (x,y) indexes
        #     index_iter = index_list
        # elif coord_list:
        #     # must be iterable containing tuples of (lon, lat) coordinates
        #     index_iter = coord_list
        else:
            raise ValueError("Must provide either step size or dimension size")



    def build_geojson(self):
        self.geojson = {
            "type": "FeatureCollection",
            "features": self.feature_list
        }


    def output_to_geojson(self, path):
        self.build_geojson()
        with open(path, "w") as dst:
            json.dump(self.geojson, dst)


    def build_grid(self):
        tstart = time.time()
        self.feature_list = list(self.gen_grid())
        print("Run time: {} seconds".format(round(time.time() - tstart, 4)))


    def gen_grid(self):
        for c, r in self.index_iter:

            cell_id = (r * self.ncols) + c

            y = self.ymax - (r * self.ystep)
            x = self.xmin + (c * self.xstep)

            b_xmin = x
            b_xmax = x + self.xstep
            b_ymin = y - self.ystep
            b_ymax = y

            bounds = (b_xmin, b_ymin, b_xmax, b_ymax)

            shp = box(*bounds)

            props = {}

            if any([i in self.properties for i in ["all", "grid"]]):
                props.update({
                    "cell_id": cell_id,
                    "row": r,
                    "column": c,
                })

            if any([i in self.properties for i in ["all", "center"]]):
                props.update({
                    "xcenter": b_xmin + (b_xmax - b_xmin) / 2,
                    "ycenter": b_ymax - (b_ymax - b_ymin) / 2,
                })

            if any([i in self.properties for i in ["all", "bounds", "box"]]):
                props.update({
                    "xmin": b_xmin,
                    "ymin": b_ymin,
                    "xmax": b_xmax,
                    "ymax": b_ymax
                })

            feature = {
                "type": "Feature",
                "properties": props,
                "geometry": shp.__geo_interface__
            }

            yield feature




