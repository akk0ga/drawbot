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

    def click(self, button: str = 'left', number: int = 1):
        """
        perform click on screen\n
        button is equal to:\n
        - right
        - left
        :param number:
        :param button:
        :return:
        """
        if button == 'right':
            self.mouse.click(Button.right, number)
        elif button == 'left':
            self.mouse.click(Button.left, number)
