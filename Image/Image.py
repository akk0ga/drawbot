from PIL import Image as Img
import requests


class Image:
    def __init__(self, path_type: str = 'url', url: str = '', path: str = ''):
        """
        type is required to define which type used if u want to use a local path or url,
        possible value are:\n
        - url (default)
        - path\n

        url must be the image source (empty if type is path)\n
        path must be the image local path (empty if type is url)\n

        :param path_type:
        :param url:
        :param path:
        """
        if path_type == 'url':
            self.image = Img.open(requests.get(url, stream=True).raw).convert('RGB')
        elif path_type == 'path':
            self.image = Img.open(path).convert('RGB')
        else:
            raise Exception('invalid type choose between url or path')

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

    def get_size(self) -> tuple:
        """
        return the size of image
        :return: tuple
        """
        return self.image.size

    def get_pixel(self):
        return self.image.load()

    def get_colors_value(self) -> tuple:
        """
        return color value present in the image
        :return: tuple
        """
        pixel: list = [0, 0]
        pixel_list: list = self.get_pixel()
        width, height = self.get_size()
        colors: list = []

        for y in range(0, height):
            pixel[0] = 0
            for x in range(0, width):
                r, g, b = pixel_list[x, y]
                total = r + g + b
                if total not in colors:
                    colors.append(total)
                pixel[0] += 1
            pixel[1] += 1

        colors.sort()
        print(colors)
        return tuple(colors)

    def set_path(self, image_path: str):
        self.image = Img.open(image_path)

    path = property(fset=set_path)
