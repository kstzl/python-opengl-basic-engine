import OpenGL.GL as GL
import ctypes as ct

from engine.Vao import Vao
from engine.Ibo import Ibo

from engine.VtxConstructor import VtxConstructor
from engine.BaseGeometry import BaseGeometry


class QuadGeometry(BaseGeometry):
    def __init__(self) -> None:
        super().__init__()

        self.vtxc = VtxConstructor()

        # Vertex 0
        self.vtxc.add_vertex(
            x=-0.5, y=0.5, z=0.0, nx=0, ny=0, nz=1, r=1.0, g=1.0, b=1.0, u=0.0, v=1.0
        )

        # Vertex 1
        self.vtxc.add_vertex(
            x=0.5, y=0.5, z=0.0, nx=0, ny=0, nz=1, r=1.0, g=1.0, b=1.0, u=1.0, v=1.0
        )

        # Vertex 2
        self.vtxc.add_vertex(
            x=-0.5, y=-0.5, z=0.0, nx=0, ny=0, nz=1, r=1.0, g=1.0, b=1.0, u=0.0, v=0.0
        )

        # Vertex 3
        self.vtxc.add_vertex(
            x=0.5, y=-0.5, z=0.0, nx=0, ny=0, nz=1, r=1.0, g=1.0, b=1.0, u=1.0, v=0.0
        )

        indices = [0, 1, 2, 1, 3, 2]

        self.vao = Vao()
        self.vao.bind()

        self.vbo = self.vtxc.make_vbo()
        self.vbo.bind()

        self.ibo = Ibo(indices)
        self.ibo.bind()

        # Vertex position
        self.vao.enable_and_set_attribute_ptr(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 44, 0)

        # Vertex normal
        self.vao.enable_and_set_attribute_ptr(1, 3, GL.GL_FLOAT, GL.GL_FALSE, 44, 12)

        # Vertex color
        self.vao.enable_and_set_attribute_ptr(2, 3, GL.GL_FLOAT, GL.GL_FALSE, 44, 24)

        # Vertex texture coordinates
        self.vao.enable_and_set_attribute_ptr(3, 2, GL.GL_FLOAT, GL.GL_FALSE, 44, 36)

    def render(self):
        self.vao.bind()
        self.vbo.bind()
        self.ibo.bind()
        GL.glDrawElements(GL.GL_TRIANGLES, 6, GL.GL_UNSIGNED_INT, ct.c_void_p(0))

    def get_geometry_name(self) -> str:
        raise "QuadGeometry"

    def destroy(self):
        self.vao.destroy()
        self.vbo.destroy()
