import pygame, sys, os, noise

# Get location of lib and add to path (this isn't needed normally)
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','..','src'))


from PyWire3D.Entities.Camera import Camera

from PyWire3D.World.Chunk import Chunk
from PyWire3D.World.World import World

from PyWire3D.Wireframe.Node import Node
from PyWire3D.Wireframe.Polygon import Polygon


# Used in chunk generation
SEA_LEVEL = -1

def custom_chunk_gen(world, chunk_position):
    # Generate nodes, which all polygons will then be based off.
    # Uses perlin noise to calculate the height of the nodes.
    # Height is made sure to never be lower than SEA_LEVEL.

    nodes = []
    for z in range(world.chunk_size + 1):
        for x in range(world.chunk_size + 1):
            actual_x = chunk_position[0] * world.chunk_size + x
            actual_z = chunk_position[1] * world.chunk_size + z
            
            height = -noise.pnoise2(actual_x*0.05, actual_z*0.05, repeatx=2**32, repeaty=2**32) * 12

            if height < SEA_LEVEL:
                height = SEA_LEVEL
                
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
            shade *= -3
            shade = max(0, shade)

            if n1.position[1] == SEA_LEVEL and n3.position[1] == SEA_LEVEL:
                # Check if all three vertices of triangles are at sea level.
                # If so, make the polygon blue instead of green.

                if n2.position[1] == SEA_LEVEL:
                    polygons.append(Polygon([n1, n2, n3], colour=(0,20,230)))
                else:
                    polygons.append(Polygon([n1, n2, n3], colour=(shade // 3 + 10, 190 + shade // 2, shade)))

                if n4.position[1] == SEA_LEVEL:
                    polygons.append(Polygon([n1, n3, n4], colour=(0,40,240)))
                else:
                    polygons.append(Polygon([n1, n3, n4], colour=(shade // 3 + 5, 200 + shade // 2, shade)))

            else:
                polygons.append(Polygon([n1, n2, n3], colour=(shade // 3 + 10, 190 + shade // 2, shade)))
                polygons.append(Polygon([n1, n3, n4], colour=(shade // 3 + 5, 200 + shade // 2, shade)))
    
    chunk = Chunk(chunk_position, polygons, nodes)
    return chunk


pygame.init()
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 32)

display = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Perlin Noise Polygon Demo')

# Pygame defines increasing y values to be downwards, so we need to flip it when rendering
camera = Camera(display_size=(800,500), position=[0, 4, 0], clip=[0.5,24], flip_y=True)

world = World(camera)
world.set_chunk_generator(custom_chunk_gen)


# Load some chunks for viewing (because currently chunks aren't loaded/unloaded based on distance):
for i in range(-2,2):
    for j in range(0,5):
        world.load_chunk([i,j])


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
        camera.move([3*dt, 0, 0])
    if keys[pygame.K_a]:
        camera.move([-3*dt, 0, 0])

    if keys[pygame.K_w]:
        camera.move([0, 0, 2*dt])
    if keys[pygame.K_s]:
        camera.move([0, 0, -2*dt])
        
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


    # ----------------------------------------
    # Render section
    
    display.fill((30, 100, 200))

    world.render(display)
    
    fps_img = font.render(str(int(1/dt)), True, (50, 200, 150))
    display.blit(fps_img, (560, 15))

    pygame.display.flip()