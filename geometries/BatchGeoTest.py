import OpenGL.GL as GL
import ctypes as ct

from engine.Vao import Vao
from engine.Ibo import Ibo

from engine.VtxConstructor import VtxConstructor
from engine.BaseGeometry import BaseGeometry


class BatchGeoTest(BaseGeometry):
    def __init__(self) -> None:
        super().__init__()

        self.vtxc = VtxConstructor()

        self.count = 5_000
        indices = []

        for i in range(self.count):

            d = 5
            px = (i%100) * -d
            py = (i//100) * d

            # Vertex 0
            self.vtxc.add_vertex(x=-0.5+px, y=0.5+py, z=0.0)

            # Vertex 1
            self.vtxc.add_vertex(x=0.5+px, y=0.5+py, z=0.0)

            # Vertex 2
            self.vtxc.add_vertex(x=-0.5+px, y=-0.5+py, z=0.0)

            # Vertex 3
            self.vtxc.add_vertex(x=0.5+px, y=-0.5+py, z=0.0)

            v = (i*4)
            indices.insert(len(indices), [0+v, 1+v, 2+v, 1+v, 3+v, 2+v])

        # indices = [
        #     0, 1, 2, 1, 3, 2,
        #     4, 5, 6, 5, 7, 6
            
        #     ]

        self.vao = Vao()
        self.vao.bind()

        self.vbo = self.vtxc.make_vbo()
        self.vbo.bind()

        self.ibo = Ibo(indices)
        self.ibo.bind()

        # Vertex position
        self.vao.enable_and_set_attribute_ptr(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 12, 0)

    def render(self):
        self.vao.bind()
        self.vbo.bind()
        self.ibo.bind()
        GL.glDrawElements(GL.GL_TRIANGLES, 6 * self.count, GL.GL_UNSIGNED_INT, ct.c_void_p(0))

    def get_geometry_name(self) -> str:
        raise "QuadGeometry"

    def destroy(self):
        self.vao.destroy()
        self.vbo.destroy()
