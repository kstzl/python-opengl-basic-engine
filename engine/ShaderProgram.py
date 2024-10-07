import OpenGL.GL as GL
import OpenGL.GL.shaders as GLS

import numpy as np

from pyrr import Matrix44


class ShaderProgram:
    def __init__(self, frag_shader_path: str, vert_shader_path: str) -> None:
        frag_shader_content = self.__get_file_data(frag_shader_path)
        vert_shader_content = self.__get_file_data(vert_shader_path)

        self.vertex_shader = self.try_compile_shader(
            vert_shader_content, GL.GL_VERTEX_SHADER
        )

        self.fragment_shader = self.try_compile_shader(
            frag_shader_content, GL.GL_FRAGMENT_SHADER
        )

        print("OK")
        self.program = GLS.compileProgram(self.vertex_shader, self.fragment_shader)

    def try_compile_shader(self, shader_content: str, shader_kind: any):
        try:
            return GLS.compileShader(shader_content, shader_kind)
        except GLS.ShaderCompilationError:
            raise Exception("Engine Fatal Error : shader compilation error.")

    def set_matrix4fv_uniform(self, uniform_name: str, mtx: Matrix44):
        loc = self.get_uniform_loc(uniform_name)
        GL.glUniformMatrix4fv(loc, 1, GL.GL_FALSE, mtx.astype(np.float32))

    def set_1i_uniform(self, uniform_name, value: int):
        loc = self.get_uniform_loc(uniform_name)
        GL.glUniform1i(loc, value)

    def set_1f_uniform(self, uniform_name, value: int):
        loc = self.get_uniform_loc(uniform_name)
        GL.glUniform1f(loc, value)

    def set_3f_uniform(self, uniform_name, vec: [int]):
        loc = self.get_uniform_loc(uniform_name)
        GL.glUniform3f(loc, *vec)

    def get_uniform_loc(self, uniform_name: str):
        return GL.glGetUniformLocation(self.program, uniform_name)

    def use(self):
        GL.glUseProgram(self.program)

    def destroy(self):
        print(f"    - Destroying Vertex Shader({self.vertex_shader})")
        GL.glDeleteShader(self.vertex_shader)

        print(f"    - Destroying Fragment Shader({self.fragment_shader})")
        GL.glDeleteShader(self.fragment_shader)

        print(f"    - Destroying Shader Program({self.program})")
        GL.glDeleteProgram(self.program)

    def __get_file_data(self, file_path: str):
        with open(file_path, encoding="UTF-8", mode="r") as file:
            return file.read()
