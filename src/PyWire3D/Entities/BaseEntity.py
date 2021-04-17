from PyWire3D.Utilities.Vector import add

class BaseEntity:
    def __init__(self, position=[0,0,0]):
        '''
        A basic Entity class, used as the base for all entity systems with a position.
        '''
        self.position = position

    def translate(self, amount):
        '''
        Translate the camera by the vector [x, y, z].
        '''
        self.position = add(self.position, amount)