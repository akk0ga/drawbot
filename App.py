from Image.Image import Image


class App:
    def __init__(self):
        self.image = Image('assets/square.jpg')

    def run(self):
        self.image.show_image()


if __name__ == "__main__":
    app = App()
    app.run()
