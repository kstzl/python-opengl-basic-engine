import pygame as pg
import random

from engine.Engine import Engine

from MapGenerator import MapGenerator

from FPSCameraPlayer import FPSCameraPlayer
from geometries.QuadGeometry import QuadGeometry

from engine.ShaderProgram import ShaderProgram
from engine.Texture import Texture
from engine.Material import Material
from engine.actor.DrawableActor import DrawableActor

from pyrr import Vector3

if __name__ == "__main__":
    engine_instance = Engine(window_size=(1920, 1080))

    default_geometry = engine_instance.register_geometry(QuadGeometry())

    default_shader = ShaderProgram(
        "./assets/shaders/default.frag", "./assets/shaders/default.vert"
    )
    floor_material = engine_instance.register_material(
        Material(
            shader_program=default_shader,
            texture=Texture("./assets/textures/tile.jpg"),
            normal_texture=Texture("./assets/textures/tile_normal.png"),
        )
    )

    wall_material = engine_instance.register_material(
        Material(
            shader_program=default_shader,
            texture=Texture("./assets/textures/metrotile.jpg"),
            normal_texture=Texture("./assets/textures/metrotile_normal.png"),
        )
    )

    clock_material = engine_instance.register_material(
        Material(
            shader_program=default_shader,
            texture=Texture("./assets/textures/clock.png"),
            normal_texture=Texture("./assets/textures/metrotile_normal.png"),
        )
    )

    level = [
        1,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        0,
        0,
        1,
        0,
        0,
        1,
        0,
        1,
        1,
        1,
        0,
        1,
        0,
        1,
        1,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        0,
        0,
    ]

    mp = MapGenerator(level=level, sx=6, sy=6)

    result = mp.parse()

    for floor in result["floors"]:
        new_actor = DrawableActor()
        new_actor.geometry = default_geometry
        new_actor.material = floor_material
        new_actor.pitchDeg = -90
        new_actor.position = Vector3([floor[0], 0, floor[1]])
        engine_instance.actors.append(new_actor)

    for wall in result["walls"]:
        new_actor = DrawableActor()
        new_actor.geometry = default_geometry
        new_actor.material = wall_material
        new_actor.yawDeg = wall[2]
        new_actor.position = Vector3([wall[0], 0.5, wall[1]])
        engine_instance.actors.append(new_actor)

        new_actor = DrawableActor()
        new_actor.geometry = default_geometry
        new_actor.material = (
            clock_material if random.randint(0, 5) == 0 else wall_material
        )
        new_actor.yawDeg = wall[2]
        new_actor.position = Vector3([wall[0], 1.5, wall[1]])
        engine_instance.actors.append(new_actor)

    engine_instance.camera = FPSCameraPlayer()
    engine_instance.camera.position = Vector3([0, 0.6, 0])

    drone_snd = pg.mixer.Sound("./assets/sounds/drone.wav")
    drone_snd.set_volume(0.1)
    drone_snd.play()

    clock_snd = pg.mixer.Sound("./assets/sounds/clock.wav")
    clock_snd.set_volume(0.1)
    clock_snd.play()

    engine_instance.run()
