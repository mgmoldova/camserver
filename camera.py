from time import time


class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
    	f = open("1" + '.jpg', 'rb')
        self.frames = f.read()
        f.close()

    def get_frame(self):
        return self.frames[0]
