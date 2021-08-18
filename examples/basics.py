import polygongrid as pg

# desired bounds
bounds = (-180, 180, -90, 90)

# accepts input of either step sizes (resolution) or dimension sizes (number of items in each dimension)
# if both provided, they must agree
step_size = (10, 10)
dim_size = (36, 18)

my_grid = pg.PolygonGrid(bounds, step_size=step_size, dim_size=dim_size, properties="grid")

my_grid.build_grid()

my_grid.output_to_geojson("examples/example.geojson")

# Run time: 0.0295 seconds