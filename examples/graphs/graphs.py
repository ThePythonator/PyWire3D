import pygame, sys, os
from math import sin, cos

# Get location of lib and add to path (this isn't needed normally)
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','..','src'))


from PyWire3D.Entities.Camera import Camera

from PyWire3D.World.Chunk import Chunk
from PyWire3D.World.World import World

from PyWire3D.Wireframe.Node import Node
from PyWire3D.Wireframe.Polygon import Polygon

# Custom chunk generator function - World class requires this.
def custom_chunk_gen(world, chunk_position):
    # Generate nodes, which all polygons will then be based off.

    if chunk_position[0] < -9 or chunk_position[0] > 9 or chunk_position[1] < -9 or chunk_position[1] > 9:
        # Limit the size of the map, so it isn't infinite.
        return Chunk(chunk_position, [], [])

    nodes = []
    for z in range(world.chunk_size + 1):
        for x in range(world.chunk_size + 1):
            actual_x = chunk_position[0] * world.chunk_size + x
            actual_z = chunk_position[1] * world.chunk_size + z
            
            # Uncomment the second height equation to get a different graph

            height = cos((actual_x * 0.08) ** 2 + (actual_z * 0.08) ** 2) * 3
            # height = sin(0.5 * actual_x) * cos(0.5 * actual_z) * 2
                
            nodes.append(Node([actual_x, height, actual_z]))

    # Generate polygons, which is what is seen when the demo is run.

    polygons = []
    for z in range(world.chunk_size):
        for x in range(world.chunk_size):
            n1 = nodes[z * (world.chunk_size + 1) + x]
            n2 = nodes[z * (world.chunk_size + 1) + x + 1]
            n3 = nodes[(z + 1) * (world.chunk_size + 1) + x + 1]
            n4 = nodes[(z + 1) * (world.chunk_size + 1) + x]

            # Shade is used to add a bit of variation in to the colours, based on the height of the nodes.
            
            shade = n1.position[1] + n2.position[1] + n3.position[1] + n4.position[1]
            shade = max(0, shade)

            shade2 = max(min((n1.position[1]+5)*20, 255), 40)

            polygons.append(Polygon([n1, n2, n3], colour=(shade * 2 + 40, 140 + shade * 2, shade2)))
            polygons.append(Polygon([n1, n3, n4], colour=(shade * 2 + 50, 135 + shade * 2, shade2)))
    
    # Create and return chunk.
    return Chunk(chunk_position, polygons, nodes)


pygame.init()
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 32)

display = pygame.display.set_mode((800, 500))
pygame.display.set_caption('3D Graph Polygon Demo')

# Pygame defines increasing y values to be downwards, so we need to flip it when rendering
camera = Camera(display_size=(800,500), position=[4, 4, 4], clip=[0.5,40], flip_y=True)

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
    
    world.update()
    camera.update()

    if keys[pygame.K_d]:
        camera.move([4*dt, 0, 0])
    if keys[pygame.K_a]:
        camera.move([-4*dt, 0, 0])

    if keys[pygame.K_w]:
        camera.move([0, 0, 4*dt])
    if keys[pygame.K_s]:
        camera.move([0, 0, -4*dt])
        
    if keys[pygame.K_SPACE]:
        camera.move([0, 4*dt, 0])
    if keys[pygame.K_LSHIFT]:
        camera.move([0, -4*dt, 0])
        
    if keys[pygame.K_DOWN]:
        camera.rotate([0.5*dt, 0, 0])
    if keys[pygame.K_UP]:
        camera.rotate([-0.5*dt, 0, 0])
        
    if keys[pygame.K_RIGHT]:
        camera.rotate([0, 0.5*dt, 0])
    if keys[pygame.K_LEFT]:
        camera.rotate([0, -0.5*dt, 0])


    # ----------------------------------------
    # Render section
    
    display.fill((30, 100, 200))

    world.render(display)
    
    # Display fps
    fps_img = font.render(str(int(1/dt)), True, (50, 200, 150))
    display.blit(fps_img, (760, 15))

    pygame.display.flip()