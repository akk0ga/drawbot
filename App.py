from Image.Image import Image
from mouse.Mouse import Mouse


class App:
    def __init__(self):
        self.image = Image('assets/circle.png')
        self.mouse = Mouse()

    def run(self):
        self.mouse.move(x=1920, y=500)


if __name__ == "__main__":
    app = App()
    app.run()
