class BaseEngine:
    def __init__(self, world):
        self.world = world

        self._cull_method = self.default_cull_method

    def check_collision(self, entity, collider):
        raise NotImplementedError('Nope.')
        
    def resolve_collision(self, entity, collider):
        raise NotImplementedError('Nope.')
        
    def handle_collision(self, entity):
        raise NotImplementedError('Nope.')

    def set_cull_method(self, cull_method):
        self._cull_method = cull_method

    def cull_chunks(self, chunks):
        return self._cull_method(chunks)

    def default_cull_method(self, chunks):
        return [shape for chunk in chunks for shape in chunk.shapes]