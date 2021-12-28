import cv2
from os.path import split as split_path


class ImageContainer:
    def __init__(self, path, preview_height=100):
        self.__path = path
        self.__preview_height = preview_height

        self.__image = None
        self.__preview = None
        self.__preview_width = None
    
    def _check_image_is_loaded(func):
        def wrapper(obj):
            if obj.__image is None:
                raise ValueError("Image not loaded")
            return func(obj)
        return wrapper
            
    def load(self):
        self.__image = cv2.imread(self.__path)
        self.__preview_width = \
            self.get_preview_width()
        preview_size = (self.__preview_width, self.__preview_height)
        self.__preview = cv2.resize( self.__image, preview_size)

    @_check_image_is_loaded
    def image(self):
        return self.__image.copy()
    
    @_check_image_is_loaded
    def preview(self):
        return self.__preview.copy()
    
    @_check_image_is_loaded
    def get_preview_width(self):
        h, w, _ = self.__image.shape
        w_scale = self.__preview_height / h
        return int(w * w_scale)
    
    @property
    def fname(self):
        _, fname = split_path(self.__path)
        return fname

    @property
    def path(self):
        return self.__path
