import os
import pytest
import polygongrid as PG


def test_bad_args():
    with pytest.raises(Exception):
        PG((-180, 180, -90, 90), step_size=(1,2,3))
