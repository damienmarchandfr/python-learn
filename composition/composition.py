from typing import Tuple
from PIL import Image, ImageDraw, ImageFont
import os
from random import randrange

class Avatar:

    def __init__(self) -> None:

        self._p = os.path.dirname(__file__)

        self._mouth_image = self._getMouthImage()
        self._border_image = self._getBorderImage()
        self._eyes_image = self._getEyesImage()

        self._border_image.paste(self._mouth_image, (0, 0), self._mouth_image)
        self._border_image.paste(self._eyes_image,(0,0),self._eyes_image)

    def _getBorderImage(self):
        BORDERS = ['border-circle.png','border-square.png']
        index = randrange(0,len(BORDERS))
        return Image.open(self._p+'/'+BORDERS[index])

    def _getMouthImage(self):
        MOUTHS = ['mouth-neutral.png','mouth-sad.png','mouth-smile.png']
        index = randrange(0,len(MOUTHS))
        return Image.open(self._p+'/'+MOUTHS[index])

    def _getEyesImage(self):
        EYES = ['eyes-big.png','eyes-cross.png','eyes-rounded.png','eyes-serious.png','eyes-triangle.png','eyes-lol.png']    
        index = randrange(0,len(EYES))
        return Image.open(self._p+'/'+EYES[index])

    def save_image(self, path: str):
        self._border_image.save(path)


a = Avatar()
a.save_image('tewt.png')
