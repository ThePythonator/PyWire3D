from pygame.draw import polygon as py_draw_polygon

class Polygon:
    def __init__(self, nodes, colour=None):
        '''
        A basic polygon class, used to create larger structures.
        '''
        self.nodes = nodes

        self.colour = colour
        self.visible = True if colour is not None else False

    def update(self, camera):
        '''
        This doesn't do anything.
        '''

    def render(self, display, camera):
        '''
        Render the polygon (if visible == True).
        '''
        if self.visible:
            on_screen = True
            
            for node in self.nodes:
                if node.projected_point[2] == 0:
                    on_screen = False
                    break

            if on_screen:
                points = [[node.projected_point[0] + camera.display_size[0] // 2, node.projected_point[1] + camera.display_size[1] // 2] for node in self.nodes]
                py_draw_polygon(display, self.colour, points)