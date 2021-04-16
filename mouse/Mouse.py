from pynput.mouse import Button, Controller
from pynput import mouse


class Mouse:
    def __init__(self):
        self.mouse = Controller()
        self.position: tuple

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

    def get_position(self) -> tuple:
        """
        return mouse position
        """
        return self.mouse.position

    def __on_click(self, x, y, button, pressed):
        if pressed and button == Button.left:
            self.position = x, y
        if not pressed:
            # Stop listener
            return False

    def wait_click(self, message: str):
        """
        wait mouse click
        :return:
        """
        with mouse.Listener(on_click=self.__on_click) as listener:
            print(message)
            listener.join()
