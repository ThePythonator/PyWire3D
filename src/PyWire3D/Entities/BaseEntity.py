import numpy

from PyWire3D.Utilities.Vector import add_3d

class BaseEntity:
    def __init__(self, position=[0, 0, 0], angle=[0, 0, 0]):
        '''
        A basic Entity class, used as the base for all entity systems with a position.
        '''
        self.position = position
        self.angle = angle
        # self.position = numpy.array(position)
        # self.angle = numpy.array(angle)

    def translate(self, amount):
        '''
        Translate the entity by the vector [x, y, z].
        '''
        # self.position += numpy.array(amount)
        self.position = add_3d(self.position, amount)
        
    def rotate(self, amount):
        '''
        Rotate the entity by the angles [x, y, z].
        '''
        # self.angle += numpy.array(amount)
        self.angle = add_3d(self.angle, amount)