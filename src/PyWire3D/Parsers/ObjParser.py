import inspect, os

from PyWire3D.Parsers.MtlParser import MtlFile
from PyWire3D.Parsers.FileReader import stack_search_and_read

class ObjFile:
    def __init__(self):
        self.vertices = []
        self.faces = []

        self.materials = []

    @staticmethod
    def read(filename):
        
        lines = [line.strip().split(' ') for line in stack_search_and_read(filename) if line[0] != '#']

        materials = []

        currentMaterial = -1
        
        obj_file = ObjFile()

        for line in lines:
            if line[0] == 'v':
                obj_file.vertices.append(
                    [
                        float(line[1]),
                        float(line[2]),
                        float(line[3])
                    ]
                )

            elif line[0] == 'f':
                obj_file.faces.append(
                    ObjFile.ObjFace(
                        [[int(item) for item in vertex.split('/')]+[0,0,0] for vertex in line[1:]],
                        material=(None if currentMaterial == -1 else materials[currentMaterial])
                    )
                )

            elif line[0] == 'mtllib':
                materials += MtlFile.read(line[1]).materials

            elif line[0] == 'usemtl':
                for i, material in enumerate(materials):
                    if material.name == line[1]:
                        currentMaterial = i
        
        return obj_file

    class ObjFace:
        def __init__(self, vertices, material=None):
            self.vertex_indices = []
            self.vertex_texture_indices = []
            self.vertex_normal_indices = []

            self.material = material

            for vertex in vertices:
                self.vertex_indices.append(vertex[0])
                self.vertex_texture_indices.append(vertex[1])
                self.vertex_normal_indices.append(vertex[2])