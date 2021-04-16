import pygame, sys, os

# Get location of lib and add to path (this isn't needed normally)
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','..','src'))

from PyWire3D.World.World import World
from PyWire3D.Camera.Camera import Camera


pygame.init()
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 32)

display = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Perlin Noise Polygon Demo')

# Pygame defines increasing y values to be downwards, so we need to flip it when rendering
camera = Camera(display_size=(600,400), position=[0, 4, 0], clip=[0.5,24], flip_y=True)

world = World(camera)

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
    
    display.fill((30, 110, 200))

    world.render(display)
    
    fps_img = font.render(str(int(1/dt)), True, (50, 200, 150))
    display.blit(fps_img, (560, 15))

    pygame.display.flip()