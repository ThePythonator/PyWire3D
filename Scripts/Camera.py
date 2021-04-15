import math

from Vector_Utils import get_rotation_matrix_3d, rotate_point_3d, add

class Camera:
    def __init__(self, position=[0,0,0], angle=[0,0,0], clip=[0,64], f=1, display_size=[100,100]):
        '''
        A Camera class, used to calculate the projection location of nodes/shapes.
        '''
        # Position and angle of camera
        self.position = position.copy()
        self.angle = angle.copy()

        # Clipping planes
        self.clip_near = clip[0]
        self.clip_far = clip[1]

        # Distance from camera to display
        self.f = f

        # Used for centering
        self.display_size = display_size

        # Rotation of camera
        self.rotation_matrix = get_rotation_matrix_3d(self.angle)

    def update(self, dt):
        '''
        Update the camera's rotation matrix.
        '''
        self.rotation_matrix = get_rotation_matrix_3d(self.angle)

    def render(self, display):
        '''
        This doesn't do anything.
        '''

    def translate(self, vector):
        '''
        Translate the camera by the vector [x, y, z].
        '''
        self.position = add(self.position, vector)

    def should_clip(self, z):
        '''
        Returns a boolean, determining whether z is outside the camera's clipping boundaries.
        '''
        return z <= self.clip_near or z >= self.clip_far

    def project_point(self, point, offset_to_center=False):
        '''
        Returns the projected point [x, y, z_depth] as it should be displayed on the viewing surface (assuming center of surface is (0,0), unless offset_to_center == True).
        z_depth is only needed for calculating render order. 
        If z_depth == 0, the point has been clipped.
        '''
        difference = [point[0] - self.position[0], point[1] - self.position[1], point[2] - self.position[2]]

        d_mat = rotate_point_3d(difference, self.rotation_matrix)
        d_x = d_mat.item(0)
        d_y = d_mat.item(1)
        d_z = d_mat.item(2)

        if d_z <= 0 or self.should_clip(d_z):
            return [0, 0, 0]

        x = (d_x * self.f) / d_z
        y = (d_y * self.f) / d_z

        if offset_to_center:
            x += self.display_size[0] // 2
            y += self.display_size[1] // 2

        return [x, y, d_z]

    def project_node(self, node):
        '''
        Returns the projected point [x, y, z_depth] as it should be displayed on the viewing surface.
        See project_point for more details.
        '''
        return self.project_point(node.position)