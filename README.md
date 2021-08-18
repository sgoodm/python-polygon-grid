# polygon-grid

Creates a regular grid of polygons based on input bounding box and resolution or dimensions.

[![build badge](https://github.com/sgoodm/python-polygon-grid/actions/workflows/test-with-coverage.yml/badge.svg)](https://github.com/sgoodm/python-polygon-grid/actions/workflows/test-and-coverage.yml)
[![Coverage Status](https://coveralls.io/repos/github/sgoodm/python-polygon-grid/badge.svg?branch=master)](https://coveralls.io/github/sgoodm/python-polygon-grid?branch=master)
[![Downloads](https://static.pepy.tech/personalized-badge/polygongrid?period=total&units=international_system&left_color=lightgrey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/polygongrid)



## Example

The below example generates a polygon grid over the entire world, where each grid cell is 10x10 decimal degrees.

```
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

```

Resulting polygon grid on top of imagery:

![Stylized Example Result](https://github.com/sgoodm/python-polygon-grid/blob/master/examples/styled_example_result.png)

Note: while the transparency of the image only shows the edges, all outputs are polygons, and not lines.



## Installation


### Using pip

The latest version of polygon-grid is [available on PyPi](https://pypi.org/project/polygongrid/), and can be installed with Pip:
```
pip install polygongrid
```

If you'd like to install the latest development (alpha) release, there may be a newer version on [TestPyPi](https://test.pypi.org/project/polygongrid/):
```
pip install -i https://test.pypi.org/simple/ polygongrid
```

### From source

To install this package from source, first clone this repository, then use pip to install:
```
git clone git@github.com:sgoodm/python-polygon-grid.git
cd python-polygon-grid
pip install .
```



## Contribute

New issues are always welcome, and if you'd like to make a change, fork the repo and submit a pull request.


### Testing and Coverage

We use Pytest and Coveralls to run unit tests and track code coverage of tests. If you submit code, please make sure it passes existing tests and adds relevant testing coverage for new features.

You can run tests and coverage checks locally, or you can fork the repository and utilize GitHub actions and Coveralls. To use GitHub actions and Coveralls, you'll need to add your forked repo to your own Coverall accounts and add you Coveralls token to your repository as a GitHub Secret (see below).


To run tests and coverage checks locally, you can use the following commands:
```
pip install pytest coverage
coverage run -m pytest ./
coverage html
```

### GitHub Secrets

There are three GitHub Secrets required to enable all of our GitHub Actions:
1. COVERALLS_REPO_TOKEN - this is the API token for Coveralls, used for publishing code coverage reports
2. TEST_PYPI_API_TOKEN - this is the API token for TestPyPi, needed for publishing alpha releases
3. PYPI_API_TOKEN - this is the API token for PyPi, needed for publishing releases

Note: contributors do not need PyPi tokens; if you create a new release in a forked repo it will trigger a GitHub action that will attempt to publish to PyPi and fail.