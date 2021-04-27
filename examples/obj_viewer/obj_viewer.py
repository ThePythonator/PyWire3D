import pygame, sys, os, noise

# Get location of lib and add to path (this isn't needed normally)
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','..','src'))


from PyWire3D.Entities.Camera import Camera
from PyWire3D.Entities.Entity import Entity

from PyWire3D.World.Chunk import Chunk
from PyWire3D.World.World import World

from PyWire3D.Wireframe.Node import Node
from PyWire3D.Wireframe.Polygon import Polygon

from PyWire3D.Parsers.ObjParser import ObjFile

from PyWire3D.Utilities.Vector import scale_3d


# Used in chunk generation
# model = ObjFile.read('demo.obj')
model = ObjFile.read('f:/Repositories/PyWire3D/examples/obj_viewer/demo.obj')

# Custom chunk generator function - World class requires this.
def custom_chunk_gen(world, chunk_position):
    # For simplicity, load everything into one chunk.

    if chunk_position == [0, 0]:
        nodes = [Node(vertex) for vertex in model.vertices]

        triangles = []
        
        for face in model.faces:
            triangles.append(Polygon([nodes[vertex_index - 1] for vertex_index in face.vertex_indices], colour=scale_3d(face.material.Kd, 255)))

        return Chunk(chunk_position, triangles, nodes)

    else:
        return Chunk(chunk_position, [], [])



pygame.init()
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 32)

display = pygame.display.set_mode((800, 500))
pygame.display.set_caption('.obj File Viewer Polygon Demo')

# Pygame defines increasing y values to be downwards, so we need to flip it when rendering
camera = Camera(display_size=(800,500), position=[0, 0, 0], clip=[0,32], flip_y=True)
world = World(camera, chunk_size=4, chunk_spawn_radius=6)
world.set_chunk_generator(custom_chunk_gen)

# Main loop
while True:
    # Update section
    
    dt = clock.tick(60)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        camera.move([3*dt, 0, 0])
    if keys[pygame.K_a]:
        camera.move([-3*dt, 0, 0])

    if keys[pygame.K_w]:
        camera.move([0, 0, 3*dt])
    if keys[pygame.K_s]:
        camera.move([0, 0, -3*dt])
        
    if keys[pygame.K_SPACE]:
        camera.move([0, 3*dt, 0])
    if keys[pygame.K_LSHIFT]:
        camera.move([0, -3*dt, 0])
        
    if keys[pygame.K_DOWN]:
        camera.rotate([0.5*dt, 0, 0])
    if keys[pygame.K_UP]:
        camera.rotate([-0.5*dt, 0, 0])
        
    if keys[pygame.K_RIGHT]:
        camera.rotate([0, 0.5*dt, 0])
    if keys[pygame.K_LEFT]:
        camera.rotate([0, -0.5*dt, 0])
        
    
    world.update()
    camera.update()


    # ----------------------------------------
    # Render section
    
    display.fill((30, 100, 200))

    world.render(display)
    
    # Display fps
    fps_img = font.render(str(int(1/dt)), True, (50, 200, 150))
    display.blit(fps_img, (760, 15))

    pygame.display.flip()