from Image.Image import Image
from mouse.Mouse import Mouse
from paint.Paint import Paint


class App:
    def __init__(self):
        self.image = Image('assets/complex.jpg')
        self.mouse = Mouse()
        self.paint = Paint(mode='classic', brush='brush')

    def run(self):
        # define the zone where draw
        print('define the zone')
        zone = self.paint.define_draw_zone()
        p1, p2 = zone  # to draw shape p2 = size, p1 = start_to

        # resize image
        new_height = p2[1] - p1[1]
        resize_path = self.image.resize(new_height=new_height, get_path=True)
        self.image.path = resize_path

        # get image color
        pixels_color = self.image.get_color()
        pixel_list = self.paint.define_color(pixel_list=pixels_color)

        # draw shape
        self.paint.draw_shape(size=p2, start_to=p1, pixel_list=pixel_list)


if __name__ == "__main__":
    app = App()
    app.run()
