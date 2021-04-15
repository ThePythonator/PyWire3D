import noise

## NOTE: very unfinished, see PerlinNoise Demo for a working version

from Node import Node
from Polygon import Polygon
from Chunk import Chunk
from Vector_Utils import get_distance_3d

CHUNK_SIZE = 8

class World:
    def __init__(self, camera):
        self.loaded_chunks = []
        # self.unloaded_chunks = []

        self.camera = camera

        # self.seed = 0
        
        # Load some chunks for testing:
        for i in range(-1,2):
            for j in range(1,4):
                self.load_chunk([i,j])

    def update(self, dt):
        for chunk in self.loaded_chunks:
            chunk.update(self.camera)

    def render(self, display):
        # for chunk in self.loaded_chunks:
        #     chunk.render(display, camera)

        # Order the shapes
        all_shapes = []
        for chunk in self.loaded_chunks:
            all_shapes += chunk.shapes
            
        sorted_shapes = sorted(all_shapes, key=lambda shape : get_distance_3d(shape.nodes[0].position, self.camera.position), reverse=True)

        for shape in sorted_shapes:
            shape.render(display, self.camera)

    def load_chunk(self, position):
        # load from data, for now just generate.
        chunk = self.generate_chunk(position) # later, if already been generated before, load it from save file
        self.loaded_chunks.append(chunk)

    # def generate_chunk(self, seed, position):
    #     pass

    def generate_chunk(self, chunk_position):
        nodes = []
        for z in range(CHUNK_SIZE + 1):
            for x in range(CHUNK_SIZE + 1):
                actual_x = chunk_position[0] * CHUNK_SIZE + x
                actual_z = chunk_position[1] * CHUNK_SIZE + z
                # height = 0
                height = noise.pnoise2(actual_x*0.05, actual_z*0.05, repeatx=2**32, repeaty=2**32) * 10
                # print(height)
                nodes.append(Node([actual_x, height, actual_z]))#, colour=(255,255,255)

        shapes = []
        for z in range(CHUNK_SIZE):
            for x in range(CHUNK_SIZE):
                n1 = nodes[z * (CHUNK_SIZE + 1) + x]
                n2 = nodes[z * (CHUNK_SIZE + 1) + x + 1]
                n3 = nodes[(z + 1) * (CHUNK_SIZE + 1) + x + 1]
                n4 = nodes[(z + 1) * (CHUNK_SIZE + 1) + x]
                # shapes.append(Shape([n1, n2, n3, n4], colour=(0,200,50)))
                shapes.append(Polygon([n1, n2, n3], colour=(0,255,0)))
                shapes.append(Polygon([n1, n3, n4], colour=(0,200,50)))
        
        chunk = Chunk(chunk_position, shapes, nodes)
        return chunk