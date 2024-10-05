import sys

import pygame as pg

import OpenGL.GL as GL

from geometries.TriangleGeometry import TriangleGeometry
from geometries.QuadGeometry import QuadGeometry
from engine.ShaderProgram import ShaderProgram
from engine.actor.Camera import Camera
from engine.actor.DrawableActor import DrawableActor

from pyrr import Matrix44


class Engine:
    def __init__(self, window_size=(900, 800)) -> None:
        self.window_size = window_size

        self.initialize_pygame()
        GL.glEnable(GL.GL_DEPTH_TEST)

        self.clock = pg.time.Clock()
        self.elapsed_time = 0

        self.projection_matrix = Matrix44.perspective_projection(
            90, self.window_size[0] / self.window_size[1], 0.1, 1000.0
        )

        self.camera = Camera()
        self.camera.yawDeg = -90

        self.actors = [TriangleGeometry(), TriangleGeometry(), QuadGeometry()]
        self.actors[0].position.z -= 1
        self.actors[1].position.z -= 1

        self.actors[0].position.x += 1

        ## TODO ##
        self.shader_program = ShaderProgram("./shaders/default.frag", "./shaders/default.vert")

    def initialize_pygame(self):
        pg.init()

        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(
            pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE
        )

        pg.display.set_mode(self.window_size, flags=pg.OPENGL | pg.DOUBLEBUF  )

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        pg.display.set_caption("Python OpenGL Engine")

    def process_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                self.cleanup()
                pg.quit()
                sys.exit()

    def cleanup(self):
        for actor in self.actors:
            actor.destroy()
        self.shader_program.destroy()

    def run(self):
        while True:
            dt: float = self.clock.tick(120) / 1000

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

        for actor in self.actors:
            actor.execute(dt)

    def render(self, dt: float):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        self.shader_program.use()
        self.shader_program.set_matrix4fv_uniform("viewMatrix", self.camera.get_view_matrix())
        self.shader_program.set_matrix4fv_uniform("projectionMatrix", self.projection_matrix)

        for actor in self.actors:
            if isinstance(actor, DrawableActor):
                actor_vao = actor.get_vao()
                actor_vao.bind()

                position_matrix = actor.get_model_matrix()
                self.shader_program.set_matrix4fv_uniform("modelMatrix", position_matrix)

                GL.glDrawArrays(GL.GL_TRIANGLES, 0, 6)

        pg.display.flip()
