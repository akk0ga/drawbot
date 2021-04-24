import time
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
        },
        'skribble': {
            0: ('black', (586, 919), (0, 0, 0), 0),
            765: ('white', (586, 894), (255, 255, 255)),
            579: ('light grey', (606, 894), (193, 193, 193)),
            228: ('grey', (610, 918), (76, 76, 76)),
            134: ('dark red', (635, 918), (116, 11, 7)),
            269: ('red', (632, 894), (239, 19, 11)),
            368: ('orange', (657, 895), (255, 113, 0)),
            250: ('dark orange', (658, 919), (194, 56, 0)),
            483: ('yellow', (682, 893), (255, 228, 0)),
            394: ('dark yellow', (682, 919), (232, 162, 0)),
            204: ('green', (704, 896), (0, 204, 0)),
            101: ('dark green', (703, 919), (0, 85, 16)),
            433: ('sky blue', (729, 892), (0, 178, 255)),
            244: ('ocean blue', (730, 920), (0, 86, 158)),
            277: ('blue', (753, 891), (35, 31, 211)),
            123: ('dark blue', (751, 918), (14, 8, 101)),
            249: ('purple', (777, 894), (163, 0, 86)),
            190: ('dark purple', (776, 919), (85, 0, 105)),
            505: ('pink', (801, 893), (211, 124, 170)),
            287: ('brown', (822, 893), (160, 82, 45)),
            160: ('dark brown', (827, 918), (99, 48, 13)),
        }
    }

    __brush_available: dict = {
        'classic': ('brush', 'calligraphy', 'air-brush'),
        'skribble': ('brush', 'calligraphy', 'air-brush'),
        '3d': ('marker', 'calligraphy', 'pen', 'pastel')
    }

    def __init__(self, mode: str = 'classic', brush: str = 'brush', details: int = 2):
        """
        mode represent the paint version\n
        brush represent the brush choose to draw\n
        details represent the precision of the draw is the value is 1 it draw each pixel if 2 it draw all pair pixel
        etc etc \n

        mode is equal to:\n
        - classic (basic paint)
        - 3d (if you use paint 3d)
        - skribble (if you use skribble.io)

        brush available for classic mode:\n
        - brush
        - calligraphy
        - air-brush

        brush available for 3d mode:\n
        - marker
        - calligraphy
        - pen
        - pastel

        brush available for skribble mode:\n
        - brush

        :param mode:
        """
        self.mouse = Mouse()
        self.mode = mode
        self.details = details

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

    def draw(self, start_to: tuple, image):
        """
        draw shape
        :param image:
        :param start_to:
        """
        current_color: int = 0  # remember the color used
        image_load = image.get_pixel()  # get image pixel list
        image_color: tuple = image.get_colors_value()

        # define draw width and height
        start_width, start_height = start_to
        image_width, image_height = image.get_size()
        width: int = image_width + start_width
        height: int = image_height + start_height

        # set mouse to start position
        self.mouse.move(x=start_width, y=start_height)

        # get each color key and verify all pixel for this color
        for color in image_color:
            pixel: list = [0, 0]
            for y in range(start_height, height):
                pixel[0] = 0
                for x in range(start_width, width):
                    r, g, b = image_load[pixel[0], pixel[1]]
                    total_color_value = r+g+b
                    if total_color_value != 765 and color != 765 and x % self.details == 0:
                        if current_color != color:
                            current_color = color
                            self.select_color(color=color)
                        else:
                            if total_color_value == current_color:
                                self.mouse.click()
                                time.sleep(0.01)
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
        time.sleep(0.01)
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
