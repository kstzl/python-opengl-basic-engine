import OpenGL.GL as GL
import OpenGL.GL.shaders as GLS


class Shader:
    def __init__(self, frag_shader_path: str, vert_shader_path: str) -> None:
        frag_shader_content = self.__get_file_data(frag_shader_path)
        vert_shader_content = self.__get_file_data(vert_shader_path)

        self.shader = GLS.compileProgram(
            GLS.compileShader(frag_shader_content, GL.GL_FRAGMENT_SHADER),
            GLS.compileShader(vert_shader_content, GL.GL_VERTEX_SHADER),
        )
    
    def use(self):
        GL.glUseProgram(self.shader)

    def __get_file_data(self, file_path: str):
        with open(file_path, encoding="UTF-8", mode="r") as file:
            return file.read()
