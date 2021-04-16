import noise

## NOTE: very unfinished

from PyWire3D.Wireframe.Node import Node
from PyWire3D.Wireframe.Polygon import Polygon
from PyWire3D.World.Chunk import Chunk
from PyWire3D.Utilities.Vector import get_square_distance_3d

CHUNK_SIZE = 8
SEA_LEVEL = -1

class World:
    def __init__(self, camera):
        self.loaded_chunks = []
        # self.unloaded_chunks = []

        self.camera = camera

        # self.seed = 0
        
        # Load some chunks for testing:
        for i in range(-2,2):
            for j in range(0,5):
                self.load_chunk([i,j])

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

    # def generate_chunk(self, seed, position):
    #     pass

    def generate_chunk(self, chunk_position):
        nodes = []
        for z in range(CHUNK_SIZE + 1):
            for x in range(CHUNK_SIZE + 1):
                actual_x = chunk_position[0] * CHUNK_SIZE + x
                actual_z = chunk_position[1] * CHUNK_SIZE + z
                
                height = -noise.pnoise2(actual_x*0.05, actual_z*0.05, repeatx=2**32, repeaty=2**32) * 12
                if height < SEA_LEVEL:
                    height = SEA_LEVEL
                    
                nodes.append(Node([actual_x, height, actual_z]))#, colour=(255,255,255)

        shapes = []
        for z in range(CHUNK_SIZE):
            for x in range(CHUNK_SIZE):
                n1 = nodes[z * (CHUNK_SIZE + 1) + x]
                n2 = nodes[z * (CHUNK_SIZE + 1) + x + 1]
                n3 = nodes[(z + 1) * (CHUNK_SIZE + 1) + x + 1]
                n4 = nodes[(z + 1) * (CHUNK_SIZE + 1) + x]
                # shapes.append(Polygon([n1, n2, n3, n4], colour=(0,200,50)))
                # shapes.append(Polygon([n1, n2, n3], colour=(0,255,0)))
                # shapes.append(Polygon([n1, n3, n4], colour=(0,200,50)))
                
                shade = n1.position[1] + n2.position[1] + n3.position[1] + n4.position[1]
                shade *= -3
                shade = max(0, shade)

                if n1.position[1] == SEA_LEVEL and n3.position[1] == SEA_LEVEL:
                    # Check if at sea level

                    if n2.position[1] == SEA_LEVEL:
                        shapes.append(Polygon([n1, n2, n3], colour=(0,20,230)))
                    else:
                        shapes.append(Polygon([n1, n2, n3], colour=(shade // 2 + 15, 190, shade)))

                    if n4.position[1] == SEA_LEVEL:
                        shapes.append(Polygon([n1, n3, n4], colour=(0,40,240)))
                    else:
                        shapes.append(Polygon([n1, n3, n4], colour=(shade // 2 + 15, 195, shade)))

                else:
                    shapes.append(Polygon([n1, n2, n3], colour=(shade // 2 + 10, 190, shade)))
                    shapes.append(Polygon([n1, n3, n4], colour=(shade // 2 + 5, 200, shade)))
        
        chunk = Chunk(chunk_position, shapes, nodes)
        return chunk