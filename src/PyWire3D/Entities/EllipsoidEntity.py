from PyWire3D.Entities.Entity import Entity

class EllipsoidEntity(Entity):
    def __init__(self, position=[0, 0, 0], angle=[0, 0, 0], velocity=[0, 0, 0], radii=[1, 1, 1]):
        '''
        An EllipsoidEntity class, used for collidable entities, using an ellipsoid collision hitbox.
        '''
        super().__init__(position=position, angle=angle, velocity=velocity)
        
        self.radii = radii