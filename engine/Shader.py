import OpenGL.GL as GL
import OpenGL.GL.shaders as GLS

import numpy as np

from pyrr import Matrix44


class Shader:
    def __init__(self, frag_shader_path: str, vert_shader_path: str) -> None:
        frag_shader_content = self.__get_file_data(frag_shader_path)
        vert_shader_content = self.__get_file_data(vert_shader_path)

        self.shader = GLS.compileProgram(
            GLS.compileShader(frag_shader_content, GL.GL_FRAGMENT_SHADER),
            GLS.compileShader(vert_shader_content, GL.GL_VERTEX_SHADER),
        )

    def set_matrix4fv_uniform(self, uniform_name: str, mtx: Matrix44):
        loc = self.get_uniform_loc(uniform_name)
        GL.glUniformMatrix4fv(loc, 1, GL.GL_FALSE, mtx.astype(np.float32))

    def get_uniform_loc(self, uniform_name: str):
        return GL.glGetUniformLocation(self.shader, uniform_name)

    def use(self):
        GL.glUseProgram(self.shader)

    def __get_file_data(self, file_path: str):
        with open(file_path, encoding="UTF-8", mode="r") as file:
            return file.read()
