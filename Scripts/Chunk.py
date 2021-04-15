class Chunk:
    def __init__(self, chunk_position, shapes, nodes):
        '''
        A basic chunk class, used to group nodes and shapes.
        '''
        self.chunk_position = chunk_position
        self.shapes = shapes
        self.nodes = nodes

    def update(self, camera):
        '''
        Update the projected location of all nodes in this chunk.
        '''
        for node in self.nodes:
            node.update(camera)

    def render(self, display, camera):
        '''
        Render the nodes and shapes in this chunk, ignoring depth.
        Do not use this method if you want objects which are furthest away to be rendered first.
        If layering is needed, use World.depth_render().
        '''
        for node in self.nodes:
            node.render(display, camera)

        for shape in self.shapes:
            shape.render(display, camera)