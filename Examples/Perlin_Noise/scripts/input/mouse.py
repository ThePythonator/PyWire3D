from pygame import mouse

from scripts.utilities import position

class Mouse:
    def __init__(self, CONSTANTS):
        self.DISPLAY_SIZE = CONSTANTS.DISPLAY_SIZE

        self.visible = True
        self.image = None

        self.position = [0,0]

        self.left = self.middle = self.right = False
        self.leftLast = self.middleLast = self.rightLast = False
        self.leftPressed = self.middlePressed = self.rightPressed = None

    def update(self, app):
        ratio = position.divide2D(app.data.actualDisplaySize, self.DISPLAY_SIZE)

        self.leftLast = self.left; self.middleLast = self.middle; self.rightLast = self.right
        self.left,self.middle,self.right = mouse.get_pressed()

        pos = mouse.get_pos()
        self.position = position.divide2D(pos, ratio)

        self.leftPressed = self.position if not self.leftLast and self.left else None
        self.middlePressed = self.position if not self.middleLast and self.middle else None
        self.rightPressed = self.position if not self.rightLast and self.right else None

    def render(self, display):
        if self.image is not None:
            display.blit(self.image, self.position.vector())

    def change_visibility(self, visible):
        self.visible = visible
        mouse.set_visible(self.visible)