from Image.Image import Image


class App:
    def __init__(self):
        self.image = Image('assets/circle.png')

    def run(self):
        self.image.resize(new_width=20, new_height=20)


if __name__ == "__main__":
    app = App()
    app.run()
