import math

from PyWire3D.Utilities.Vector import get_rotation_matrix_3d, rotate_point_3d, add, matrix_to_list_3d, get_rotation_matrix_3d_y

class Camera:
    def __init__(self, display_size=[100,100], position=[0,0,0], angle=[0,0,0], clip=[0,64], fov=90, flip_y=False):
        '''
        A Camera class, used to calculate the projection location of nodes/shapes.
        '''
        # Position and angle of camera
        self.position = position.copy()
        self.angle = angle.copy()

        # Clipping planes
        self.clip_near = clip[0]
        self.clip_far = clip[1]

        # Field of view
        self.fov = fov

        # Distance from camera to display
        self.f = display_size[0] / (2 * math.tan(self.fov / 2))

        # Determines whether to flip the y axis when rendering.
        self.flip_y = flip_y

        # Used for centering
        self.display_size = display_size

        # Rotation of camera
        self.rotation_matrix = get_rotation_matrix_3d(self.angle)

    def update(self):
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
        
    def move(self, vector):
        '''
        Move the camera by the vector [x, y, z].
        This rotates the vector supplied so that the z axis of the vector is aligned with the camera.
        '''
        # Currently broken?
        # self.position = add(self.position, matrix_to_list_3d(rotate_point_3d(vector, get_rotation_matrix_3d([-self.angle[0], -self.angle[1], -self.angle[2]]))))
        # self.position = add(self.position, matrix_to_list_3d(rotate_point_3d(vector, get_rotation_matrix_3d([0, -self.angle[1], 0]))))
        self.position = add(self.position, matrix_to_list_3d(rotate_point_3d(vector, get_rotation_matrix_3d_y(-self.angle[1]))))
        # print(vector, matrix_to_list_3d(rotate_point_3d(vector, self.rotation_matrix)))

    def rotate(self, angle):
        self.angle = add(self.angle, angle)

    def should_clip(self, z):
        '''
        Returns a boolean, determining whether z is outside the camera's clipping boundaries.
        '''
        return z <= self.clip_near or z >= self.clip_far

    def project_point(self, point, offset_to_center=False, flip_y=None):
        '''
        Returns the projected point [x, y, z_depth] as it should be displayed on the viewing surface (assuming center of surface is (0,0), unless offset_to_center == True).
        z_depth is only needed for calculating render order. 
        If z_depth == 0, the point has been clipped.
        If flip_y == True, y coord is inverted (changes positive to up instead of down).
        If flip_y == None, the camera's default flip_y is used.
        '''
        if flip_y is None:
            flip_y = self.flip_y

        difference = [point[0] - self.position[0], point[1] - self.position[1], point[2] - self.position[2]]

        d_x, d_y, d_z = matrix_to_list_3d(rotate_point_3d(difference, self.rotation_matrix))

        if d_z <= 0 or self.should_clip(d_z):
            return [0, 0, 0]

        x = (d_x * self.f) / d_z
        y = (d_y * self.f) / d_z

        if offset_to_center:
            x += self.display_size[0] // 2
            y += self.display_size[1] // 2

        if flip_y:
            y = -y

        return [x, y, d_z]

    def project_node(self, node):
        '''
        Returns the projected point [x, y, z_depth] as it should be displayed on the viewing surface.
        See project_point for more details.
        '''
        return self.project_point(node.position)