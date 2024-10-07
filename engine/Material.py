from engine.ShaderProgram import ShaderProgram
from engine.Texture import Texture


class Material:
    def __init__(self, shader_program: ShaderProgram, texture: Texture, normal_texture: Texture = None) -> None:
        self.shader_program = shader_program
        self.texture = texture
        self.normal_texture = normal_texture

    def bind(self):
        self.shader_program.use()

        self.texture.bind(slot=0)
        self.shader_program.set_1i_uniform("imageTexture", 0)

        if self.normal_texture:
            self.normal_texture.bind(slot=1)
            self.shader_program.set_1i_uniform("normalMap", 1)
    
    def unbind(self):
        self.texture.unbind()
        
        if self.normal_texture is not None:
            self.normal_texture.unbind()

    def destroy_all(self):
        print("Destroying material ressources :")
        self.shader_program.destroy()
        self.texture.destroy()
