from PyWire3D.Entities.BaseEntity import BaseEntity

class Entity(BaseEntity):
    def __init__(self, position=[0, 0, 0], angle=[0, 0, 0], velocity=[0, 0, 0], gravity=[0, 0, 0]):
        '''
        A basic Entity class, used as the base for all entity systems with velocity and gravity.
        '''
        super().__init__(position=position, angle=angle)

        self.velocity = velocity

        self.gravity = gravity