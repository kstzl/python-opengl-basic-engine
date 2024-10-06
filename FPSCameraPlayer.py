import pygame as pg
import glm
import math
import random

from engine.actor.Camera import Camera

from pyrr import Vector3, Matrix44


class FPSCameraPlayer(Camera):
    def __init__(self) -> None:
        super().__init__()

        self.mouse_sensivity = 0.3
        self.move_speed = 1
        self.anim_i = 0

        self.anim_pos = Vector3([0, 0, 0])

        self.step_sounds = []
        self.step_i = 0

        for step_snd_idx in range(1, 8):
            step_snd_name = f"assets/sounds/Step{step_snd_idx}.wav"
            snd_obj = pg.mixer.Sound(step_snd_name)
            snd_obj.set_volume(0.1)
            self.step_sounds.append(snd_obj)

    def get_view_matrix(self):
        base_view_matrix = super().get_view_matrix()

        anim_matrix = Matrix44.from_translation(self.anim_pos)

        return anim_matrix @ base_view_matrix

    def move(self, additional_vector: Vector3, dt: float):
        keys = pg.key.get_pressed()

        sprint = 1

        if keys[pg.K_LSHIFT]:
            sprint = 3

        self.position = (
            self.position + additional_vector * self.move_speed * dt * sprint
        )
        self.anim_i += dt * 10 * sprint
        self.step_i += dt * 10 * sprint
        self.anim_pos = Vector3([0, -0.1 + math.cos(self.anim_i) * 0.03, 0])

        self.rollDeg = math.cos(self.anim_i / 2) * 0.25

        if self.step_i > 6:
            self.step_i = 0
            snd = random.choice(self.step_sounds)
            snd.play()

    def execute(self, dt: float):
        rel_x, rel_y = pg.mouse.get_rel()

        self.pitchDeg += rel_y * -self.mouse_sensivity
        self.yawDeg += rel_x * self.mouse_sensivity

        self.pitchDeg = glm.clamp(self.pitchDeg, -89, 89)

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.move(self.get_forward_vector(ignore_pitch=True), dt)

        if keys[pg.K_s]:
            self.move(-self.get_forward_vector(ignore_pitch=True), dt)

        if keys[pg.K_a]:
            self.move(-self.get_right_vector(), dt)

        if keys[pg.K_d]:
            self.move(self.get_right_vector(), dt)
