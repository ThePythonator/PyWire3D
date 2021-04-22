from PyWire3D.Physics.BaseEngine import BaseEngine

class CubeEngine(BaseEngine):
    def __init__(self, world):
        super().__init__(world)
        raise NotImplementedError('In progress.')

    def check_collision(self, entity, collider):
        raise NotImplementedError('Todo.')
        
    def resolve_collision(self, entity, collider):
        raise NotImplementedError('Todo.')
        
    def handle_collision(self, entity):
        cubes = self.cull_chunks(self.world.loaded_chunks)

        raise NotImplementedError('Todo.')

        # if len(collisions) > 0:
        #     self.resolve_collision(entity, sorted(collisions, key=lambda collision: collision[1]))