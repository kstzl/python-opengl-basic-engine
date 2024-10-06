import numpy as np
import OpenGL.GL as GL


class Ibo:
    def __init__(self, indices: list[int]) -> None:
        self.ibo_id = GL.glGenBuffers(1)

        np_indices = np.array(indices, dtype=np.uint32)

        self.bind()
        GL.glBufferData(
            GL.GL_ELEMENT_ARRAY_BUFFER, np_indices.nbytes, np_indices, GL.GL_STATIC_DRAW
        )

    def bind(self):
        GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, self.ibo_id)

    def destroy(self):
        print(f"Destroying Ibo({self.ibo_id})")
        GL.glDeleteBuffers(1, (self.ibo_id,))
