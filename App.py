from Image.Image import Image


class App:
    def __init__(self):
        self.image = Image('assets/circle.png')

    def run(self):
        self.image.resize(new_width=200, new_height=200)


if __name__ == "__main__":
    app = App()
    app.run()
