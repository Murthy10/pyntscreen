import pytest
from pyntscreen import Application


@pytest.fixture(scope='module')
def app():
    return Application()


def test_bbox(app):
    bbox = app._build_bbox()
    assert type(bbox) is tuple


def test_has_mouse_moved_enough(app):
    assert not app._has_mouse_moved_enough()
