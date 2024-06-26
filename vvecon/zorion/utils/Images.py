from enum import Enum
from typing import Any, Type

from .Files import FileMaker
from .Theme import ThemeFolder

__all__ = ['Images']


class Images:
    __theme__: Type[Enum] | Enum
    images: FileMaker = NotImplemented

    def __init__(self, theme: Type[Enum] | Enum):
        self.__theme__ = theme

        self.createImages()

    def createImages(self):
        for file_name in self.images.__dict__:
            file = self.images.__getattribute__(file_name)
            if type(file) == str:
                file = (file, 1)
            self.createImage(file, file_name)

    def createImage(self, file: tuple, file_name: str):
        file_path = file[0]
        version = file[1] if len(file) > 1 else 1
        folder = file[2] if len(file) > 2 else ThemeFolder.common

        if not getattr(self, file_name, False):
            setattr(self, file_name, self.imageFile(file_path, version, folder, urlOnly=True))

    def imageFile(self, file: str, version: int, folder: Any, urlOnly: bool = False) -> str:
        if folder == ThemeFolder.theme:
            folder = self.__theme__
        file = f'img/{folder.value}/{file}'
        if urlOnly:
            return file + f'?v={version}'
        return '<img src="{0}" alt="{1}">'.format(
            '{% static ' + file + f'?v={version}' + ' %}',
            file.split('/')[-1].split('.')[0].replace('-', ' ').title(),
        )
