from Image.Image import Image
from mouse.Mouse import Mouse
from paint.Paint import Paint


class App:
    def __init__(self):
        self.mouse = Mouse()
        self.paint = Paint(mode='classic', brush='brush')

    def choose_image(self):
        """
        choose image to use
        :return:
        """
        image: input = input('Choose which type of path you want to use:\n1-local path\n2- url\nyour choice: ')
        while image != '1' and image != '2':
            image: input = input('Choose which type of path you want to use:\n1-local path\n2- url\nyour choice: ')

        if image == '1':
            image = input('Put your local path here: ')
            return Image(path_type='path', path=image)
        else:
            image = input('Put your url here: ')
            return Image(path_type='url', url=image)

    def run(self):
        # choose image to use
        image = self.choose_image()

        # define the zone where draw
        print('define the zone')
        zone = self.paint.define_draw_zone()
        p1, p2 = zone  # to draw shape p2 = size, p1 = start_to

        # resize image
        new_height = p2[1] - p1[1]
        resize_path = image.resize(new_height=new_height, get_path=True)
        image.path = resize_path

        # get and set image color
        pixels_color = image.get_color()
        pixel_list = self.paint.define_color(pixel_list=pixels_color)
        image.update_color(colors=pixel_list)

        # draw shape
        # self.paint.draw_shape(size=p2, start_to=p1, image=resize_path)


if __name__ == "__main__":
    app = App()
    app.run()
