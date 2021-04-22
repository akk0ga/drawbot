import time
from PIL import Image
from mouse.Mouse import Mouse


class Paint:
    # define position and rgb code for color
    # 0 -> color name
    # 1 -> position on screen
    # 2 -> rgb code
    __color_list: dict = {
        'classic': {
            0: ('black', (881, 61), (0, 0, 0)),
            765: ('white', (883, 84), (255, 255, 255)),
            585: ('light grey', (902, 81), (195, 195, 195)),
            381: ('grey', (901, 59), (127, 127, 127)),
            394: ('brown', (925, 82), (185, 122, 87)),
            157: ('dark red', (926, 61), (136, 0, 21)),
            630: ('pink', (946, 83), (255, 174, 201)),
            301: ('red', (945, 61), (237, 28, 36)),
            470: ('gold', (967, 83), (255, 201, 14)),
            421: ('orange', (969, 60), (255, 127, 39)),
            643: ('light yellow', (991, 83), (239, 228, 176)),
            497: ('yellow', (989, 60), (255, 242, 0)),
            440: ('light green', (1011, 81), (181, 230, 29)),
            287: ('green', (1011, 58), (34, 177, 76)),
            604: ('sky blue', (1034, 83), (153, 217, 234)),
            395: ('blue', (1034, 59), (0, 162, 232)),
            448: ('blue gray', (1056, 85), (112, 146, 190)),
            339: ('indigo', (1056, 59), (63, 72, 204)),
            622: ('lavender', (1078, 82), (200, 191, 231)),
            400: ('purple', (1077, 59), (163, 73, 164))
        },
        '3d': {
            0: ('black', (1806, 871), (0, 0, 0), 0),
            765: ('white', (1697, 875), (255, 255, 255)),
            585: ('light grey', (1732, 871), (195, 195, 195)),
            264: ('grey', (1767, 874), (88, 88, 88)),
            393: ('brown', (1876, 944), (185, 122, 86)),
            163: ('dark red', (1837, 874), (136, 0, 27)),
            630: ('pink', (1844, 943), (255, 174, 201)),
            301: ('red', (1874, 876), (237, 28, 36)),
            470: ('gold', (1733, 902), (255, 201, 14)),
            421: ('orange', (1695, 908), (255, 127, 39)),
            655: ('light yellow', (1767, 904), (253, 236, 166)),
            497: ('yellow', (1803, 906), (255, 242, 0)),
            440: ('light green', (1843, 911), (181, 230, 29)),
            287: ('green', (1881, 911), (34, 177, 76)),
            646: ('sky_blue', (1690, 946), (140, 255, 251)),
            411: ('blue', (1735, 944), (0, 168, 243)),
            339: ('indigo', (1771, 946), (63, 72, 204)),
            400: ('purple', (1805, 943), (163, 73, 164))
        }
    }

    __brush_available: dict = {
        'classic': ('brush', 'calligraphy', 'air-brush'),
        '3d': ('marker', 'calligraphy', 'pen', 'pastel')
    }

    def __init__(self, mode: str = 'classic', brush: str = 'brush'):
        """
        mode represent the paint version\n
        brush represent the brush choose to draw\n

        mode is equal to:\n
        - classic (basic paint)
        - 3d (if you use paint 3d)

        brush available for classic mode:\n
        - brush
        - calligraphy
        - air-brush

        brush available for 3d mode:\n
        - marker
        - calligraphy
        - pen
        - pastel

        :param mode:
        """
        self.mouse = Mouse()
        self.mode = mode

        # define color list to use
        if mode in self.__color_list:
            self.color: dict = self.__color_list[mode]
        else:
            raise Exception('the mode you choose is not available please select one between: classic, 3d')

        # define brush to use
        if brush in self.__brush_available[mode]:
            self.brush = brush
        else:
            raise Exception('the brush select is not available for this mode')

    def define_draw_zone(self) -> tuple:
        """
        define width and height for the draw to do
        in the tuple value are (width, height, position were start draw)
        :return: tuple
        """
        self.mouse.wait_click(message='select top left angle')
        p1 = self.mouse.position
        self.mouse.wait_click(message='select bottom right angle')
        p2 = self.mouse.position

        return p1, p2

    def draw_shape(self, size: tuple, start_to: tuple, image):
        """
        draw shape
        :param image:
        :param start_to:
        :param size:
        """

        start_width, start_height = start_to
        self.mouse.move(x=start_to[0], y=start_to[1])
        pixel: list = [0, 0]  # x, y

        img = image.load()

        # define draw width and height
        width = image.width + start_width
        height = image.height + start_height

        for y in range(start_height, height):
            if pixel[0] != 0:
                pixel[0] = 0
            for x in range(start_width, width):
                total: int = 0
                for value in img[pixel[0], pixel[1]]:
                    total = total + value
                pixel[0] = pixel[0] + 1
                if total != 765:
                    self.select_color(color=total)
                    self.mouse.move(x=x, y=y)
                    self.mouse.click()
                    time.sleep(1 / 1000)
            pixel[1] = pixel[1] + 1
            self.mouse.release_button()

    def test_draw_shape(self, size: tuple, start_to: tuple, image):
        """
        draw shape
        :param image:
        :param start_to:
        :param size:
        """
        current_color: int = 0
        pixel: list = [0, 0]  # get pixel position on the image x, y
        image_load = image.get_pixel()  # get image info and load it to get pixel

        # define draw width and height
        start_width, start_height = start_to
        image_width, image_height = image.get_size()
        width = image_width + start_width
        height = image_height + start_height

        # set mouse to start position
        self.mouse.move(x=start_width, y=start_height)

        # get each color key and verify all pixel for this color
        for color in self.color:
            pixel[1] = 0
            pixel[0] = 0
            for y in range(start_height, height):
                pixel[0] = 0
                for x in range(start_width, width):
                    r, g, b = image_load[pixel[0], pixel[1]]
                    total_color_value = r+g+b
                    if total_color_value != 765 and color != 765:
                        if current_color != color:
                            current_color = color
                            self.select_color(color=color)
                        else:
                            if total_color_value == current_color:
                                self.mouse.click()
                                time.sleep(0.001)
                    self.mouse.move(x=x, y=y)

                    pixel[0] += 1
                pixel[1] += 1

    def select_color(self, color: int):
        """
        select color on paint
        :param color: int
        """
        x, y = self.__color_list[self.mode][color][1]
        self.mouse.move(x=x, y=y)
        time.sleep(0.05)
        self.mouse.click()

    def define_color(self, pixel_list: list) -> list:
        """
        update image color
        :param pixel_list:
        :return:
        """
        paint_color = self.__color_list[self.mode]  # get color to compare for select mode

        for pixel in range(0, len(pixel_list)):
            r, g, b = pixel_list[pixel]
            correct_diff = None
            correct_rgb = None

            for color in paint_color:
                cr, cg, cb = paint_color[color][2]
                difference = abs(r - cr) + abs(g - cg) + abs(b - cb)

                if correct_diff is None and correct_rgb is None:
                    correct_diff = difference
                    correct_rgb = [cr, cg, cb]
                else:
                    if difference < correct_diff:
                        correct_diff = difference
                        correct_rgb = [cr, cg, cb]
            pixel_list[pixel] = (correct_rgb[0], correct_rgb[1], correct_rgb[2])

        return pixel_list

    def list_available_colors(self):
        """
        print the list of available color
        :return:
        """
        print(f'total: {len(self.color)}')
        for color in self.color:
            print(color)

    def color_info(self, color: str):
        """
        print color info screen pos + rgb code
        :return:
        """
        global key
        find: bool = False

        for key in self.__color_list['classic']:
            if color == self.__color_list['classic'][key][0]:
                find = True
                key = key
                break
        if find:
            print(
                f'name: {self.__color_list["classic"][key][0]}\nposition on screen: {self.__color_list["classic"][key][1]}\nrgb: {self.__color_list["classic"][key][2]}')
        else:
            raise Exception('no color find')
