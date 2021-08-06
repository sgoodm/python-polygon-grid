import os
import pytest
import polygongrid as pg


def test_bad_args():
    with pytest.raises(Exception):
        pg.PolygonGrid()

    with pytest.raises(Exception):
        pg.PolygonGrid((-180, 180, -90, 90))

    with pytest.raises(Exception):
        pg.PolygonGrid((-180, 90), step_size=(0.5, 0.5), dim_size=(720, 360))

    with pytest.raises(Exception):
        pg.PolygonGrid((-180, 180, -90, 90), step_size=(1,2,3))

    with pytest.raises(Exception):
        pg.PolygonGrid((-180, 180, -90, 90), step_size=(0.5, 0.5), dim_size=(360, 180))

    with pytest.raises(Exception):
        pg.PolygonGrid((-180, 180, -90, 90), dim_size=(360.5, 180.5))

    with pytest.raises(Exception):
        pg.PolygonGrid((-180, 180, -90, 90), dim_size=(1, 360, 180))

    with pytest.raises(Exception):
        pg.PolygonGrid((-90, 90, -90, 90), dim_size=(180))


def test_valid_args():
    pg.PolygonGrid((-180, 180, -90, 90), step_size=(0.5, 0.5), properties=['all'])
    pg.PolygonGrid((-180, 180, -90, 90), step_size=(0.5, 0.5))
    pg.PolygonGrid((-180, 180, -90, 90), step_size=(0.5))
    pg.PolygonGrid((-180, 180, -90, 90), step_size=[0.5])
    pg.PolygonGrid((-180, 180, -90, 90), step_size=0.5)
    pg.PolygonGrid((-180, 180, -90, 90), dim_size=(720, 360))


def test_version():
    pg.__version__


def test_build_grid():
    my_pg = pg.PolygonGrid((-180, 180, -90, 90), step_size=(10, 10), properties=['all'])
    my_pg.build_grid()


def test_output_to_geojson():
    my_pg = pg.PolygonGrid((-180, 180, -90, 90), step_size=(10, 10), properties=['all'])
    my_pg.build_grid()
    example_path = "tests/test.geojson"
    if os.path.isfile(example_path):
        os.remove(example_path)
    my_pg.output_to_geojson(example_path)
