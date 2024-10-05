import OpenGL.GL as GL


class Vbo:
    def __init__(self, data: any, data_size: int) -> None:
        self.vbo_id = GL.glGenBuffers(1)

        self.bind()
        GL.glBufferData(GL.GL_ARRAY_BUFFER, data_size, data, GL.GL_STATIC_DRAW)

    def bind(self):
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo_id)

    def destroy(self):
        print(f"Destroying Vbo({self.vbo_id})")
        GL.glDeleteBuffers(1, (self.vbo_id,))
