from PIL import Image as Img


class Image:
    def __init__(self, image_path: str):
        self.image = Img.open(image_path)

    def resize(self, new_width: int, new_height: int):
        resize = self.image.resize((new_width, new_height))
        resize.save(fp=f'assets/resized.{self.image.format}')

    def show(self):
        """
        show the selected image
        :return:
        """
        self.image.show()