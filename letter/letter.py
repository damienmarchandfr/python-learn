from typing import Tuple
from PIL import Image, ImageDraw, ImageFont

class AvatarBuilder:

    def __init__(self) -> None:
        self._letter: str = 'A'
        self._background_color : Tuple = (0, 0, 0)
        self._fill : Tuple = (255,255,255)
        self._font_path : str = 'font_coco_sharp.ttf'
        self._img : Image
        self._font_size : int = 70
        self._margin_x = 0
        

    def set_letter(self,letter: str) -> None:
        if letter is None:
            raise ValueError('Letter must be defined')

        if len(letter) != 1:
            raise ValueError('Value ' + letter + ' is not a valid letter.')

        self._letter = letter


    def set_background_color(self,color : Tuple) -> None:
        self._background_color = color


    def set_letter_color(self,color: Tuple) -> None:
        self._fill = color

    def set_font(self,path: str) -> None:
         self._font_path = path

    def add_margin_x(self,x: int):
        self._margin_x = x

    def _create_image(self):
        size = 90
        fnt = ImageFont.truetype(self._font_path, self._font_size)
        self._img = Image.new('RGB',(size,size),self._background_color)
        draw = ImageDraw.Draw(self._img)
        w, h = draw.textsize(self._letter,fnt)
        draw.text(((size-w)/2,((size-h)/2)+self._margin_x), self._letter, fill=self._fill, font = fnt, align="center")

    def set_font_size(self,font_size : int):
        self._font_size = font_size

    def save_image(self,path: str):
        self._create_image()
        self._img.save(path)