from PyWire3D.Entities.Entity import Entity

class CuboidEntity(Entity):
    def __init__(self, position=[0, 0, 0], angle=[0, 0, 0], velocity=[0, 0, 0], size=[1, 1, 1]):
        '''
        An CuboidEntity class, used for collidable entities, using an cuboid collision hitbox.
        '''
        super().__init__(position=position, angle=angle, velocity=velocity)
        
        self.size = size