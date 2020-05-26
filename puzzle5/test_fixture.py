
from turtle import *


class MockTurtle(Turtle):

    def speed(self, speed=None):
        super().speed(0)
        print("set speed ", speed)

    def getscreen(self):
        return MockScreen(super().getscreen())

class MockScreen:
    def __init__(self, screen):
        self.screen = screen

    def bgcolor(self, color):
        self.screen.bgcolor(color)
        print("set screen color ", color)

    def title(self, title):
        self.screen.title(title)
        print("set screen title ", title)

    def setup(self, width=1.0, height=1.0):
        self.screen.setup(width, height)
        print("set screen setup width ", width, " height ", height)

    def window_width(self):
        return self.screen.window_width()

    def window_height(self):
        return self.screen.window_height()

    def mainloop(self):
        return self.screen.mainloop()

