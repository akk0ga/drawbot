from pynput.mouse import Button, Controller


class Mouse:
    def __init__(self):
        self.mouse = Controller()

    def move(self, x: int, y: int):
        """
        move the mouse to select position
        :return:
        """
        self.mouse.position = (x, y)
