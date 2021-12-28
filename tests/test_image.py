import cv2

from src.image import ImageContainer
from tests.constants import IMAGE_PATH, IMAGE_NAME


img_container = ImageContainer(IMAGE_PATH)
img_container.load()


def test_no_loaded():
    test_img_container = ImageContainer(IMAGE_PATH)
    try:
        test_img_container.image()
        assert False, 'No raising error for not loaded image'
    except ValueError:
        pass


def test_image():
    test_img = cv2.imread(IMAGE_PATH)
    assert (img_container.image() == test_img).all()


def test_image_preview():
    img_shape = img_container.image().shape
    prev_shape = img_container.preview().shape
    ih, iw, _ = img_shape
    ph, pw, _ = prev_shape
    assert abs((ih / iw) - (ph / pw)) < 0.05
    assert ih > ph and iw > pw


def test_image_fname():
    assert IMAGE_NAME == img_container.fname


def test_image_path():
    assert IMAGE_PATH == img_container.path
