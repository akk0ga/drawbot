from mouse.Mouse import Mouse


class Paint:
    def __init__(self, mode: str = 'classic', brush: str = 'brush'):
        """
        mode is equal to\n
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
        self.mode = mode
        self.__brush_available: dict = {
            'classic': ('brush', 'calligraphy', 'air-brush'),
            '3d': ('brush', 'calligraphy', 'pen', 'pastel')
        }
        
        # define position and rgb code for color
        # 0 -> position
        # 1 -> rgb code
        if mode == 'classic':
            self.color: dict = {
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
            }
        elif mode == '3d':
            self.color: dict = {
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
        else:
            raise Exception('the mode you choose is not available please select one between: classic, 3d')
