from PyWire3D.Parsers.FileReader import stack_search_and_read

class MtlFile:
    def __init__(self):
        self.materials = []

    @staticmethod
    def read(filename):

        lines = [line.strip().split(' ') for line in stack_search_and_read(filename) if line[0] != '#']
        
        mtl_file = MtlFile()

        for line in lines:
            if line[0] == 'newmtl':
                mtl_file.materials.append(MtlFile.MtlMaterial(line[1]))

            if len(mtl_file.materials) > 0:
                if line[0] == 'Ka':
                    mtl_file.materials[-1].Ka = (float(line[1]), float(line[2]), float(line[3]))
                
                elif line[0] == 'Kd':
                    mtl_file.materials[-1].Kd = (float(line[1]), float(line[2]), float(line[3]))
                    
                elif line[0] == 'Ks':
                    mtl_file.materials[-1].Ks = (float(line[1]), float(line[2]), float(line[3]))
                    
                elif line[0] == 'Ns':
                    mtl_file.materials[-1].Ns = float(line[1])
                    
                elif line[0] == 'd':
                    mtl_file.materials[-1].d = float(line[1])
                    
                elif line[0] == 'Tr':
                    mtl_file.materials[-1].d = 1 - float(line[1])
                    
                elif line[0] == 'Ni':
                    mtl_file.materials[-1].Ni = float(line[1])
        
        return mtl_file

    class MtlMaterial:
        def __init__(self, name, Ka = (1, 1, 1), Kd = (1, 1, 1), Ks = (0, 0, 0), Ns = 10, d = 1, Ni = 1):
            self.name = name
            self.Ka = Ka
            self.Kd = Kd
            self.Ks = Ks
            self.Ns = Ns
            self.d = d
            self.Ni = Ni