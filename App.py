from Image.Image import Image
from mouse.Mouse import Mouse
from paint.Paint import Paint


class App:
    def __init__(self):
        self.image = Image('assets/circle.png')
        self.mouse = Mouse()
        self.paint = Paint(mode='classic', brush='brush')

    def run(self):
        # define the zone where draw
        print('define the zone')
        zone = self.paint.define_draw_zone()
        p1, p2 = zone

        # resize image
        new_width = p2[0] - p1[0]
        new_height = p2[1] - p1[1]
        resize_path = self.image.resize(new_width=new_width, new_height=new_height, get_path=True)
        self.image.path = resize_path
        

if __name__ == "__main__":
    app = App()
    app.run()
