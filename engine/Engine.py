import sys

import pygame as pg

import OpenGL.GL as GL

from geometries.TriangleGeometry import TriangleGeometry
from engine.Shader import Shader
from engine.actor.Camera import Camera

from pyrr import Matrix44


class Engine:
    def __init__(self, window_size=(900, 800)) -> None:
        self.window_size = window_size

        self.initialize_pygame()

        self.clock = pg.time.Clock()
        self.elapsed_time = 0

        self.projection_matrix = Matrix44.perspective_projection(
            90, self.window_size[0] / self.window_size[1], 0.1, 1000.0
        )

        self.camera = Camera()
        self.camera.yawDeg = -90

        ## TODO ##
        self.geo = TriangleGeometry()
        self.shader = Shader("./shaders/default.frag", "./shaders/default.vert")

    def initialize_pygame(self):
        pg.init()

        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(
            pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE
        )

        pg.display.set_mode(self.window_size, flags=pg.OPENGL | pg.DOUBLEBUF)

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        pg.display.set_caption("Python OpenGL Engine")

    def process_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            dt: float = self.clock.tick(60) / 1000

            self.process_events()
            self.execute_actors(dt)

            self.render(dt)
            self.check_for_gl_error()

    def check_for_gl_error(self):
        error = GL.glGetError()
        if error != GL.GL_NO_ERROR:
            print(f"OpenGL error: {error}")

    def execute_actors(self, dt: float):
        self.camera.execute(dt)

    def render(self, dt: float):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        self.shader.use()
        self.geo.vao.bind()

        pos_matrix = Matrix44.from_translation([0, 0, -1])
        self.shader.set_matrix4fv_uniform("modelMatrix", pos_matrix)
        self.shader.set_matrix4fv_uniform("viewMatrix", self.camera.get_view_matrix())
        self.shader.set_matrix4fv_uniform("projectionMatrix", self.projection_matrix)

        GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)

        pg.display.flip()
