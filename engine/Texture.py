import pygame as pg

import OpenGL.GL as GL


class Texture:
    def __init__(self, texture_path: str) -> None:
        self.texture_id = GL.glGenTextures(1)

        GL.glBindTexture(GL.GL_TEXTURE_2D, self.texture_id)

        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)

        image = pg.image.load(texture_path).convert()
        image_width, image_height = image.get_rect().size
        image_data = pg.image.tostring(image, "RGBA")

        GL.glTexImage2D(
            GL.GL_TEXTURE_2D,
            0,
            GL.GL_RGBA,
            image_width,
            image_height,
            0,
            GL.GL_RGBA,
            GL.GL_UNSIGNED_BYTE,
            image_data,
        )

        GL.glGenerateMipmap(GL.GL_TEXTURE_2D)

    def bind(self, slot: int):
        GL.glActiveTexture(GL.GL_TEXTURE0 + slot)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self.texture_id)

    def destroy(self):
        GL.glDeleteTextures(1, (self.texture_id,))
