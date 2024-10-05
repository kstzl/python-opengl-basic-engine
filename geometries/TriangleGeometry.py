import numpy as np
import OpenGL.GL as GL

import ctypes

from engine.Vao import Vao
from engine.Vbo import Vbo

class TriangleGeometry:
    def __init__(self) -> None:
        # x, y, z, r, g, b, s, t
        self.vertex_data = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0,
            0.0, 0.5, 0.0, 0.0, 0.0, 1.0, 0.5, 1.0
        )

        self.vertex_data = np.array(self.vertex_data, dtype=np.float32)

        self.vao = Vao()
        self.vao.bind()
        
        self.vbo = Vbo(self.vertex_data, self.vertex_data.nbytes)
        self.vbo.bind()

        # Vertex position
        self.vao.enable_and_set_attribute_ptr(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 32, 0)

        # Vertex color
        self.vao.enable_and_set_attribute_ptr(1, 3, GL.GL_FLOAT, GL.GL_FALSE, 32, 12)

        # Vertex texture coordinates
        # self.vao.enable_and_set_attribute_ptr(2, 2, GL.GL_FLOAT, GL.GL_FALSE, 32, 20)


    def destroy(self):
        self.vao.destroy()
        self.vbo.destroy()