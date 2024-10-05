import numpy as np
import OpenGL.GL as GL

from engine.Vao import Vao

from engine.actor.DrawableActor import DrawableActor
from engine.VtxConstructor import VtxConstructor


class TriangleGeometry(DrawableActor):
    def __init__(self) -> None:
        super().__init__()

        self.vtxc = VtxConstructor()
        self.vtxc.add_vertex(x=-0.5, y=-0.5, z=0.0, r=1.0, g=0.0, b=0.0, u=0.0, v=0.0)
        self.vtxc.add_vertex(x=0.5, y=-0.5, z=0.0, r=0.0, g=1.0, b=0.0, u=1.0, v=0.0)
        self.vtxc.add_vertex(x=0.0, y=0.5, z=0.0, r=0.0, g=0.0, b=1.0, u=0.5, v=1.0)

        self.vao = Vao()
        self.vao.bind()

        self.vbo = self.vtxc.make_vbo()
        self.vbo.bind()

        # Vertex position
        self.vao.enable_and_set_attribute_ptr(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 32, 0)

        # Vertex color
        self.vao.enable_and_set_attribute_ptr(1, 3, GL.GL_FLOAT, GL.GL_FALSE, 32, 12)

        # Vertex texture coordinates
        # self.vao.enable_and_set_attribute_ptr(2, 2, GL.GL_FLOAT, GL.GL_FALSE, 32, 20)

    def render(self):
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vtxc.count())
        
    def get_vao(self) -> Vao:
        return self.vao

    def destroy(self):
        self.vao.destroy()
        self.vbo.destroy()
