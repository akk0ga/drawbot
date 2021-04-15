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
