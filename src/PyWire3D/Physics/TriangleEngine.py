from PyWire3D.Physics.BaseEngine import BaseEngine

from PyWire3D.Utilities.Vector import get_sum_square_distance_3d

class TriangleEngine(BaseEngine):
    def __init__(self, world):
        super().__init__(world)
        raise NotImplementedError('In progress.')

    def check_collision(self, entity, collider):
        raise NotImplementedError('Todo.')
        
    def resolve_collision(self, entity, collider):
        raise NotImplementedError('Todo.')
        
    def handle_collision(self, entity):
        triangles = self.cull_chunks(self.world.loaded_chunks)

        collisions = [(triangle, get_sum_square_distance_3d(entity.position, *[node.position for node in triangle.nodes])) for triangle in triangles if self.check_collision(entity, triangle)]

        if len(collisions) > 0:
            self.resolve_collision(entity, sorted(collisions, key=lambda collision: collision[1]))