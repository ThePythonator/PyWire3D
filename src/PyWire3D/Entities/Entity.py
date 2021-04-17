from PyWire3D.Entities.BaseEntity import BaseEntity

class Entity(BaseEntity):
    def __init__(self, position=[0,0,0], angle=[0,0,0], velocity=[0,0,0]):
        '''
        A basic Entity class, used as the base for all entity systems with velocity and direction.
        '''
        super().__init__(position=position)

        self.angle = angle
        self.velocity = velocity