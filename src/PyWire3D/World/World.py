from PyWire3D.Utilities.Vector import get_sum_square_distance_3d, get_square_distance_3d

# Note: still very much a work-in-progress

class World:
    def __init__(self, camera, chunk_size=8, chunk_spawn_radius=4):#, seed=0
        self.camera = camera

        self.loaded_chunks = []
        # self.unloaded_chunks = []

        self._chunk_generator = None

        self.chunk_size = chunk_size

        self.chunk_spawn_radius = chunk_spawn_radius

        # self.seed = seed
        
    def update(self):
        # Calculate chunks we need to be loaded/unloaded
        chunks_required = []

        center_x = self.camera.position[0] // self.chunk_size
        center_y = self.camera.position[2] // self.chunk_size
        
        for x in range(-self.chunk_spawn_radius, self.chunk_spawn_radius + 1):
            for y in range(-self.chunk_spawn_radius, self.chunk_spawn_radius + 1):
                chunks_required.append([center_x + x, center_y + y])

        for chunk in self.loaded_chunks:
            if chunk.chunk_position in chunks_required:
                chunks_required.remove(chunk.chunk_position)

            else:
                self.loaded_chunks.remove(chunk)

        for chunk_position in chunks_required:
            self.load_chunk(chunk_position)

        for chunk in self.loaded_chunks:
            chunk.update(self.camera)

    def render(self, display):
        # for chunk in self.loaded_chunks:
        #     chunk.render(display, camera)

        # Order the shapes
        all_shapes = []
        for chunk in self.loaded_chunks:
            all_shapes += chunk.shapes
            
        # For more accuracy, use first line (reduces the chance of overlapping shapes). Second line is faster.
        # sorted_shapes = sorted(all_shapes, key=lambda shape : get_sum_square_distance_3d(*[node.position for node in shape.nodes], self.camera.position), reverse=True)
        sorted_shapes = sorted(all_shapes, key=lambda shape : get_square_distance_3d(shape.nodes[0].position, self.camera.position), reverse=True)

        for shape in sorted_shapes:
            shape.render(display, self.camera)

    def load_chunk(self, position):
        # Todo: allow previously generated but unloaded chunks to be cached, and quickly reloaded.
        self.loaded_chunks.append(self.generate_chunk(position))

    def generate_chunk(self, chunk_position):
        '''
        Calls the method set by set_chunk_generator - if set_chunk_generator has not been called prior to calling this method, it will fail.
        '''
        if self._chunk_generator is not None:
            return self._chunk_generator(self, chunk_position)
        
        else:
            raise RuntimeError('set_chunk_generator must be called before generate_chunk')

    def set_chunk_generator(self, chunk_generator):
        '''
        Sets the chunk generator method, which is called when new chunks need to be created.
        '''
        self._chunk_generator = chunk_generator