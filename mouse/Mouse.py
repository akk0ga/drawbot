from pynput.mouse import Button, Controller


class Mouse:
    def __init__(self):
        self.mouse = Controller()

    def move(self, x: int, y: int):
        """
        move the mouse to select position
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
        """
        if button == 'right':
            self.mouse.click(Button.right, number)
        elif button == 'left':
            self.mouse.click(Button.left, number)
        else:
            raise Exception('The button selected is not allow')

    def press_button(self, button: str = 'left'):
        """
        perform click but don't release it\n
        button is equal to:\n
        - right
        - left
        :param button:
        """
        if button == 'right':
            self.mouse.press(Button.right)
        elif button == 'left':
            self.mouse.press(Button.left)
        else:
            raise Exception('The button selected is not allow')

    def release_button(self, button: str = 'left'):
        """
        release button previously pressed
        :param button:
        """
        if button == 'right':
            self.mouse.release(Button.right)
        elif button == 'left':
            self.mouse.release(Button.left)
        else:
            raise Exception('The button selected is not allow')
