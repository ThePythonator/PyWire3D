## NOTE: very unfinished

from PyWire3D.Wireframe.Node import Node
from PyWire3D.Wireframe.Polygon import Polygon
from PyWire3D.World.Chunk import Chunk
from PyWire3D.Utilities.Vector import get_square_distance_3d

SEA_LEVEL = -1

class World:
    def __init__(self, camera, chunk_size=8):
        self.camera = camera

        self.loaded_chunks = []
        # self.unloaded_chunks = []

        self._chunk_generator = None

        self.chunk_size = chunk_size

        # self.seed = 0
        
    def update(self):#, dt
        for chunk in self.loaded_chunks:
            chunk.update(self.camera)

    def render(self, display):
        # for chunk in self.loaded_chunks:
        #     chunk.render(display, camera)

        # Order the shapes
        all_shapes = []
        for chunk in self.loaded_chunks:
            all_shapes += chunk.shapes
            
        sorted_shapes = sorted(all_shapes, key=lambda shape : get_square_distance_3d(shape.nodes[0].position, self.camera.position), reverse=True)
        # sorted_shapes = sorted(all_shapes, key=lambda shape : shape.nodes[0].position[2], reverse=True)

        for shape in sorted_shapes:
            shape.render(display, self.camera)

    def load_chunk(self, position):
        # load from data, for now just generate.
        chunk = self.generate_chunk(position) # later, if already been generated before, load it from save file
        self.loaded_chunks.append(chunk)

    def generate_chunk(self, chunk_position):
        return self._chunk_generator(self, chunk_position)

    def set_chunk_generator(self, chunk_generator):
        '''
        Sets the chunk generator function, which is called when new chunks need to be created.
        '''
        self._chunk_generator = chunk_generator