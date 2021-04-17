from PIL import Image as Img


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
        resize.save(fp=f'assets/resized.png')
        if get_path:
            return f'assets/resized.png'

    def show(self):
        """
        show the selected image
        :return:
        """
        self.image.show()

    def update_color(self, colors: list):
        """
        create new image with paint color
        :return:
        """
        pixel = 0
        load_image = self.image.load()
        for y in range(0, self.image.height):
            for x in range(0, self.image.width):
                load_image[x, y] = colors[pixel]
                pixel += 1
        self.image.save(fp='assets/resized.png')

    def get_color(self) -> list:
        """
        get color from the image in matrix
        :return: list
        """
        return list(self.image.getdata())

    def set_path(self, image_path: str):
        self.image = Img.open(image_path)

    path = property(fset=set_path)
