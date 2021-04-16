from mouse.Mouse import Mouse


class Paint:
    def __init__(self, mode: str = 'classic'):
        """
        mode is equal to\n
        - classic (basic paint)
        - 3d (if u use paint 3d)
        :param mode:
        """
        self.mode = mode

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
                
            }