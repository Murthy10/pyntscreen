import pytest
from PIL import Image
from pyntscreen import Application


@pytest.fixture(scope='module')
def app():
    return Application()


@pytest.fixture(scope='module')
def image():
    return Image.new("RGBA", (50, 50), "blue")


def test_bbox(app):
    bbox = app._build_bbox()
    assert type(bbox) is tuple


def test_has_mouse_moved_enough(app):
    assert not app._has_mouse_moved_enough()


def test_right_image_size(app, image):
    assert app._right_image_size(image)


def test_not_right_image_size(app):
    image = Image.new("RGBA", (50, 51), "blue")
    assert not app._right_image_size(image)


def test_directory_does_exists(app):
    assert app._is_directory('/')


def test_directory_does_not_exists(app):
    assert not app._is_directory('asdf')
