from time import time


class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
        self.frames = [1, 2]
        f = open("1" + '.jpg', 'rb')
        self.frames[0] = f.read()
        f.close()
        f = open("2" + '.jpg', 'rb')
        self.frames[1] = f.read()
        f.close()

    def get_frame(self):
        f = open("1" + '.jpg', 'rb')
        self.frames[0] = f.read()
        f.close()
        return self.frames[0]
