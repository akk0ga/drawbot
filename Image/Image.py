from PIL import Image as Img
from PIL import ImageColor


class Image:
    def __init__(self, image_path: str):
        self.image = Img.open(image_path)

    def resize(self, new_height: int = 100, get_path: bool = False) -> str:
        """
        resize and save image, you can get the path of resized image with get_path True
        :param get_path:
        :param new_height:
        :return: str
        """
        new_width = int(new_height / self.image.height * self.image.width)
        resize = self.image.resize((new_width, new_height))
        resize.save(fp=f'assets/resized.{self.image.format}')
        if get_path:
            return f'assets/resized.{self.image.format}'

    def show(self):
        """
        show the selected image
        :return:
        """
        self.image.show()

    def get_color(self):
        """
        get color from the image
        :return:
        """
        pass

    def set_path(self, image_path: str):
        self.image = Img.open(image_path)

    path = property(fset=set_path)
