from engine.Engine import Engine

from SpectatorCameraPlayer import SpectatorCameraPlayer
from geometries.BatchGeoTest import BatchGeoTest

from engine.ShaderProgram import ShaderProgram
from engine.Texture import Texture
from engine.Material import Material
from engine.actor.DrawableActor import DrawableActor

from openal import *

from pyrr import Vector3

if __name__ == "__main__":
    engine_instance = Engine(window_size=(1920, 1080))

    batch_geometry = engine_instance.register_geometry(BatchGeoTest())

    red_shader = ShaderProgram(
        "./assets/shaders/red.frag", "./assets/shaders/red.vert"
    )
    wall_material = engine_instance.register_material(
        Material(
            shader_program=red_shader,
            texture=Texture("./assets/textures/metrotile.jpg"),
        )
    )

    new_actor = DrawableActor()
    new_actor.geometry = batch_geometry
    new_actor.material = wall_material
    new_actor.position = Vector3([0, 0, 1])
    engine_instance.actors.append(new_actor)

    engine_instance.camera = SpectatorCameraPlayer()
    engine_instance.camera.position = Vector3([0, 0.6, 0])
    engine_instance.camera.yawDeg = 90

    drone_sound = oalOpen("./assets/sounds/drone2.wav")
    drone_sound.set_gain(0.1)
    drone_sound.play()
    drone_sound.set_looping(True)

    engine_instance.run()
