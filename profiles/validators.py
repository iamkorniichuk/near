from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from PIL import Image


@deconstructible
class ImageRatioValidator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ratio = x / y

    def __call__(self, value):
        image = Image.open(value)
        width, height = image.size
        ratio = width / height
        if ratio != self.ratio:
            raise ValidationError(f"{value} ratio have to be {self.x}x{self.y}.")
