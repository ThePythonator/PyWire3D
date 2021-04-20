import math
import numpy

from PyWire3D.Entities.BaseEntity import BaseEntity
from PyWire3D.Utilities.Vector import get_rotation_matrix_3d, add_3d, matrix_to_list_3d, get_rotation_matrix_3d_y

class Camera(BaseEntity):
    def __init__(self, display_size=[100,100], position=[0,0,0], angle=[0,0,0], clip=[0,64], fov=90, flip_y=False):
        '''
        A Camera class, used to calculate the projection location of nodes/shapes.
        '''
        super().__init__(position=position, angle=angle)

        # Clipping planes
        self.clip_near = clip[0]
        self.clip_far = clip[1]

        # Field of view
        self.fov = math.radians(fov)

        # Distance from camera to display
        self.f = display_size[0] / (2 * math.tan(self.fov / 2))

        # Determines whether to flip the y axis when rendering.
        self.flip_y = flip_y

        # Used for centering
        self.display_size = display_size

        self.display_size_half = (display_size[0] // 2, display_size[1] // 2)

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
        
    def move(self, vector):
        '''
        Move the camera by the vector [x, y, z].
        This rotates the vector supplied so that the z axis of the vector is aligned with the camera.
        '''
        # Currently broken?
        # self.position = add(self.position, matrix_to_list_3d(rotate_point_3d(vector, get_rotation_matrix_3d([-self.angle[0], -self.angle[1], -self.angle[2]]))))
        # self.position = add(self.position, matrix_to_list_3d(rotate_point_3d(vector, get_rotation_matrix_3d([0, -self.angle[1], 0]))))
        # print(vector, matrix_to_list_3d(rotate_point_3d(vector, self.rotation_matrix)))

        # self.translate(matrix_to_list_3d(rotate_point_3d(vector, get_rotation_matrix_3d_y(-self.angle[1]))))
        self.translate(matrix_to_list_3d(numpy.matmul(get_rotation_matrix_3d_y(-self.angle[1]), vector)))

    def rotate(self, angle):
        self.angle = add_3d(self.angle, angle)

    def should_clip(self, z):
        '''
        Returns a boolean, determining whether z is outside the camera's clipping boundaries.
        '''
        return z <= self.clip_near or z >= self.clip_far

    def project_point(self, point, offset_to_center=False, flip_y=None, clip_sides=True):
        '''
        Returns the projected point [x, y, z_depth] as it should be displayed on the viewing surface (assuming center of surface is (0,0), unless offset_to_center == True).
        z_depth is only needed for calculating render order. 
        If z_depth == 0, the point has been clipped.
        If flip_y == True, y coord is inverted (changes positive to up instead of down).
        If flip_y == None, the camera's default flip_y is used.
        If clip_sides, points with x or y coordinates deemed too far outside the screen are set as clipped points instead, to reduce unnecessary renderings, and prevent overflows.
        '''
        if flip_y is None:
            flip_y = self.flip_y

        difference = [point[0] - self.position[0], point[1] - self.position[1], point[2] - self.position[2]]

        d_x, d_y, d_z = matrix_to_list_3d(numpy.matmul(self.rotation_matrix, difference))
        # d_x, d_y, d_z = matrix_to_list_3d(rotate_point_3d(difference, self.rotation_matrix))

        if d_z <= 0 or self.should_clip(d_z):
            return [0, 0, 0]

        x = (d_x * self.f) / d_z
        y = (d_y * self.f) / d_z

        if flip_y:
            y = -y

        if offset_to_center:
            x += self.display_size_half[0]
            y += self.display_size_half[1]

        if clip_sides:
            if x < -self.display_size[0] or x > self.display_size[0] * 2 or y < -self.display_size[1] or y > self.display_size[1] * 2:
                return [0, 0, 0]

        return [x, y, d_z]

    def project_node(self, node):
        '''
        Returns the projected point [x, y, z_depth] as it should be displayed on the viewing surface.
        See project_point for more details.
        '''
        return self.project_point(node.position)