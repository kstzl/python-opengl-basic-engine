import math
import glm

from pyrr import Vector3, Matrix44


class BaseActor:
    def __init__(self) -> None:
        self.position = Vector3([0, 0, 0])
        self.scale = Vector3([1, 1, 1])

        self.pitchDeg = 0
        self.yawDeg = 0
        self.rollDeg = 0

    def destroy(self):
        pass

    def execute(self, dt: float):
        pass

    def get_model_matrix(self):
        pitchRads = math.radians(self.pitchDeg)
        yawRads = math.radians(self.yawDeg)
        rollRads = math.radians(self.rollDeg)

        position_matrix = Matrix44.from_translation(self.position)
        rotation_matrix = Matrix44.from_x_rotation(pitchRads)
        rotation_matrix = rotation_matrix @ Matrix44.from_y_rotation(yawRads)
        rotation_matrix = rotation_matrix @ Matrix44.from_z_rotation(rollRads)

        return rotation_matrix @ position_matrix

    def get_forward_vector(self, ignore_pitch=False):

        pitchRads = math.radians(self.pitchDeg)
        yawRads = math.radians(self.yawDeg)

        forward_vector = Vector3(
            [
                math.cos(yawRads) * math.cos(pitchRads),
                math.sin(pitchRads),
                math.sin(yawRads) * math.cos(pitchRads),
            ]
        )

        if ignore_pitch:
            forward_vector.y = 0

        return forward_vector.normalized

    def get_right_vector(self):
        forward_vector = glm.vec3(self.get_forward_vector().tolist())
        up_vector = glm.vec3(self.get_up_vector().tolist())

        right = glm.cross(forward_vector, up_vector)

        return Vector3(glm.normalize(right).to_list())

    def get_up_vector(self):
        return Vector3([0.0, 1.0, 0.0])
