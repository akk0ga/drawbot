from PIL import Image as img

class Image:
    def __init__(self, image_path: str):
        self.image = img.open(image_path)