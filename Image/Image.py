from PIL import Image as Img


class Image:
    def __init__(self, image_path: str):
        self.image = Img.open(image_path)

    def show_image(self):
        """
        show the selected image
        :return:
        """
        self.image.show()
