from mouse.Mouse import Mouse


class Paint:
    # define position and rgb code for color
    # 0 -> position
    # 1 -> rgb code
    __color_list: dict = {
        'classic': {
            'white': ((883, 84), (255, 255, 255)),
            'black': ((881, 61), (0, 0, 0)),
            'light_grey': ((902, 81), (195, 195, 195)),
            'grey': ((901, 59), (127, 127, 127)),
            'brown': ((925, 82), (185, 122, 87)),
            'dark_red': ((926, 61), (136, 0, 21)),
            'pink': ((946, 83), (255, 174, 201)),
            'red': ((945, 61), (237, 28, 36)),
            'gold': ((967, 83), (255, 201, 14)),
            'orange': ((969, 60), (255, 127, 39)),
            'light_yellow': ((991, 83), (239, 228, 176)),
            'yellow': ((989, 60), (255, 242, 0)),
            'light_green': ((1011, 81), (181, 230, 29)),
            'green': ((1011, 58), (34, 177, 76)),
            'sky_blue': ((1034, 83), (153, 217, 234)),
            'blue': ((1034, 59), (0, 162, 232)),
            'blue_gray': ((1056, 85), (112, 146, 190)),
            'indigo': ((1056, 59), (63, 72, 204)),
            'lavender': ((1078, 82), (200, 191, 231)),
            'purple': ((1077, 59), (163, 73, 164))
        },
        '3d': {
            'white': ((1697, 875), (255, 255, 255)),
            'black': ((1806, 871), (0, 0, 0)),
            'light_grey': ((1732, 871), (195, 195, 195)),
            'grey': ((1767, 874), (88, 88, 88)),
            'brown': ((1876, 944), (185, 122, 86)),
            'dark_red': ((1837, 874), (136, 0, 27)),
            'pink': ((1844, 943), (255, 174, 201)),
            'red': ((1874, 876), (237, 28, 36)),
            'gold': ((1733, 902), (255, 201, 14)),
            'orange': ((1695, 908), (255, 127, 39)),
            'light_yellow': ((1767, 904), (253, 236, 166)),
            'yellow': ((1803, 906), (255, 242, 0)),
            'light_green': ((1843, 911), (181, 230, 29)),
            'green': ((1881, 911), (34, 177, 76)),
            'sky_blue': ((1690, 946), (140, 255, 251)),
            'blue': ((1735, 944), (0, 168, 243)),
            'indigo': ((1771, 946), (63, 72, 204)),
            'purple': ((1805, 943), (163, 73, 164))
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
        self.mouse.wait_click(message='left angle')
        p1 = self.mouse.position
        self.mouse.wait_click(message='right angle')
        p2 = self.mouse.position
        print(f'point1: {p1}\npoint2: {p2}')

        p1_width, p1_height = p1
        p2_width, p2_height = p2

        width = p2_width - p1_width
        height = p2_height - p1_height

        return width, height, p1_width

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
        print(f'x: {self.color[color][0][0]}\ny: {self.color[color][0][1]}\nrgb: {self.color[color][1]}')
