from Image.Image import Image
from mouse.Mouse import Mouse


class App:
    def __init__(self):
        self.image = Image('assets/circle.png')
        self.mouse = Mouse()

    def run(self):
        self.mouse.move(x=480, y=500)
        self.mouse.press_button()


if __name__ == "__main__":
    app = App()
    app.run()
