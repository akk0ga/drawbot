from PIL import Image as Img


class Image:
    def __init__(self, image_path: str):
        self.image = Img.open(image_path)

    def resize(self, new_width: int = 100, new_height: int = 100):
        """
        resize and save image
        :param new_width:
        :param new_height:
        :return:
        """
        resize = self.image.resize((new_width, new_height))
        resize.save(fp=f'assets/resized.{self.image.format}')
        return resize

    def show(self):
        """
        show the selected image
        :return:
        """
        self.image.show()

    def set_path(self, image_path: str):
        self.image = Img.open(image_path)

    path = property(fset=set_path)
