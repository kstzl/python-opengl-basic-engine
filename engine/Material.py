from engine.ShaderProgram import ShaderProgram
from engine.Texture import Texture


class Material:
    def __init__(self, shader_program: ShaderProgram, texture: Texture) -> None:
        self.shader_program = shader_program
        self.texture = texture

    def use(self):
        self.shader_program.use()

        self.texture.bind(slot=0)
        self.shader_program.set_1i_uniform("imageTexture", 0)

    def destroy_all(self):
        print(f"Destroying material ressources :")
        self.shader_program.destroy()
        self.texture.destroy()
