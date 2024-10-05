import math

from engine.actor.BaseActor import BaseActor

from pyrr import Matrix44


class Camera(BaseActor):
    def __init__(self) -> None:
        super().__init__()

        self.mouse_sensivity = 10
        self.move_speed = 2

    def get_view_matrix(self):
        camera_target = self.position + self.get_forward_vector()

        view_matrix = Matrix44.look_at(
            self.position, camera_target, self.get_up_vector()
        )

        return view_matrix @ Matrix44.from_z_rotation(math.radians(self.rollDeg))
