import pygame as pg
import glm

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

        return view_matrix

    def execute(self, dt: float):
        rel_x, rel_y = pg.mouse.get_rel()

        self.pitchDeg += rel_y * (-self.mouse_sensivity * dt)
        self.yawDeg += rel_x * (self.mouse_sensivity * dt)

        self.pitchDeg = glm.clamp(self.pitchDeg, -89, 89)

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.position = (
                self.position
                + self.get_forward_vector(ignore_pitch=False) * self.move_speed * dt
            )

        if keys[pg.K_s]:
            self.position = (
                self.position
                - self.get_forward_vector(ignore_pitch=False) * self.move_speed * dt
            )

        if keys[pg.K_a]:
            self.position = (
                self.position - self.get_right_vector() * self.move_speed * dt
            )

        if keys[pg.K_d]:
            self.position = (
                self.position + self.get_right_vector() * self.move_speed * dt
            )

        if keys[pg.K_SPACE]:
            self.position = self.position + self.get_up_vector() * self.move_speed * dt

        if keys[pg.K_LSHIFT]:
            self.position = self.position - self.get_up_vector() * self.move_speed * dt
