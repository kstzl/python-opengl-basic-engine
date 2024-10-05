import OpenGL.GL as GL
import ctypes as ct


class Vao:
    def __init__(self) -> None:
        self.vao_id = GL.glGenVertexArrays(1)

    def bind(self):
        GL.glBindVertexArray(self.vao_id)

    def enable_and_set_attribute_ptr(
        self,
        idx: int,
        size: int,
        _type: any,
        normalized: any,
        stride: any,
        ptr_value: int,
    ):
        GL.glEnableVertexAttribArray(idx)
        GL.glVertexAttribPointer(
            idx, size, _type, normalized, stride, ct.c_void_p(ptr_value)
        )

    def destroy(self):
        print(f"Destroying Vao({self.vao_id})")
        GL.glDeleteVertexArrays(1, (self.vao_id,))
