import pygame as pg
import openal as AL
import glm

from engine.actor.Camera import Camera

from pyrr import Vector3

class SpectatorCameraPlayer(Camera):
    def __init__(self) -> None:
        super().__init__()

        self.mouse_sensivity = 0.3
        self.move_speed = 3
        self.velx = 0
        self.vely = 0

        self.whoosh_sound = AL.oalOpen("./assets/sounds/fling_whoosh.wav")
        self.whoosh_sound.play()
        self.whoosh_sound.set_looping(True)

    def move(self, additional_vector: Vector3, dt: float):
        keys = pg.key.get_pressed()

        sprint = 5

        if keys[pg.K_LALT]:
            sprint = 13

        self.position = (
            self.position + additional_vector * self.move_speed * dt * sprint
        )

    def execute(self, dt: float):
        rel_x, rel_y = pg.mouse.get_rel()

        self.pitchDeg += rel_y * -self.mouse_sensivity
        self.yawDeg += rel_x * self.mouse_sensivity

        self.pitchDeg = glm.clamp(self.pitchDeg, -89, 89)

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.move(self.get_forward_vector(ignore_pitch=False), dt)
            self.velx = 1

        if keys[pg.K_s]:
            self.move(-self.get_forward_vector(ignore_pitch=False), dt)
            self.velx = -1

        if keys[pg.K_a]:
            self.move(-self.get_right_vector(), dt)
            self.vely = -1

        if keys[pg.K_d]:
            self.move(self.get_right_vector(), dt)
            self.vely = 1

        if keys[pg.K_SPACE]:
            self.move(self.get_up_vector(), dt)

        if keys[pg.K_LSHIFT]:
            self.move(-self.get_up_vector(), dt)

        self.move(self.get_forward_vector(), dt * self.velx)
        self.move(self.get_right_vector(), dt * self.vely)

        v = (abs(self.velx) + abs(self.vely)) * 0.1
        
        self.whoosh_sound.set_gain(v)

        self.velx += (0 - self.velx) * dt * 5
        self.vely += (0 - self.vely) * dt * 5