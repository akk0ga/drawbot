from Image.Image import Image
from mouse.Mouse import Mouse
from paint.Paint import Paint


class App:
    def __init__(self):
        self.image = Image('assets/circle.png')
        self.mouse = Mouse()
        self.paint = Paint(mode='3d', brush='marker')

    def run(self):
        self.paint.define_draw_zone()


if __name__ == "__main__":
    app = App()
    app.run()
