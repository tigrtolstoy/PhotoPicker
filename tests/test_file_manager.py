import os
from cv2 import imread

from src.file_manager import FileManager, FilesQueue
from tests.constants import *


manager = FileManager()
manager.set_working_dir(TEST_DATA_DIR)


def test_file_manager_working_dir():
    assert TEST_DATA_DIR == manager.working_dir

def test_file_manager_is_file():
    assert manager.is_file(IMAGE_PATH)
    assert not manager.is_file(TEST_DATA_DIR)

def test_file_manager_is_dir():
    assert manager.is_dir(TEST_DATA_DIR)
    assert not manager.is_dir(IMAGE_PATH)

def test_file_manager_list_dir():
    files_list = manager.get_files_list()
    assert {'folders', 'images'} == set(files_list)

def test_file_manager_path_exists():
    assert manager.is_path_exists(TEST_DATA_DIR)
    assert not manager.is_path_exists('asdf')

def test_file_manager_copy_remove_file():
    manager.copy_file(IMAGE_PATH, COPY_PATH)
    assert COPY_IMG_NAME in manager.get_files_list(FOLDER_PATH)
    img1 = imread(IMAGE_PATH)
    img2 = imread(COPY_PATH)
    assert (img1 == img2).all()
    manager.remove_file(COPY_PATH)
    assert COPY_IMG_NAME not in manager.get_files_list(FOLDER_PATH)
