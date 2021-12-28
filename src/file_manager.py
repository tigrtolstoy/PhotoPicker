import os
import cv2
import shutil


class FileManager:
    PATH_NOT_EXISTS = 'Path [{}] does not exists'
    NOT_FILE_ERROR = '[{}] is not file!'

    def __init__(self):
        self.__working_dir = None

    def set_working_dir(self, path):
        if self.is_dir(path):
            self.__working_dir = path
        else:
            err_msg = self.PATH_NOT_EXISTS.format(path)
            raise ValueError(err_msg)

    def copy_file(self, source_path, copy_path):
        if not self.is_file(source_path):
            err_msg = self.NOT_FILE_ERROR.format(source_path)
            raise ValueError(err_msg)
        shutil.copyfile(source_path, copy_path)

    def get_files_list(self, dir=None):
        if dir is None:
            dir = self.__working_dir
        return os.listdir(dir)

    def is_path_exists(self, path):
        exists = self.is_dir(path) or self.is_file(path)
        return exists

    def is_dir(self, path):
        return os.path.isdir(path)

    def is_file(self, path):
        return os.path.isfile(path)

    @property
    def working_dir(self):
        return self.__working_dir
        

class FilesQueue:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def get(self):
        if not self.empty():
            return self.__items.pop(0)
        return None

    def empty(self):
        return not bool(self.size())

    def size(self):
        return len(self.__items)

    def copy(self):
        return self.__items[:]
