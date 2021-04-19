from pygame.draw import circle as py_draw_circle

class Node:
    def __init__(self, position, colour=None):
        '''
        A basic node class, used for the vertices of polygons.
        '''
        self.position = position
        self.projected_point = [0, 0, 0]

        self.colour = colour
        self.visible = True if colour is not None else False

    def update(self, camera):
        '''
        Update the node's projected location.
        '''
        self.projected_point = camera.project_point(self.position, offset_to_center=True)
        # self.projected_point = camera.project_point(self.position)

    def render(self, display, camera):
        '''
        Render the node (if visible == True).
        '''
        if self.visible:
            py_draw_circle(display, self.colour, self.projected_point, 2)
