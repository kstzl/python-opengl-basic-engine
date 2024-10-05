import numpy as np

from engine.Vbo import Vbo


class VtxConstructor:
    def __init__(self) -> None:
        self.data = ()
        self.vtx_count = 0

    def add_vertex(
        self,
        x: float,
        y: float,
        z: float,
        r: float,
        g: float,
        b: float,
        u: float,
        v: float,
    ):
        self.data += (x, y, z, r, g, b, u, v)
        self.vtx_count += 1

    def as_np_f32_array(self):
        return np.array(self.data, dtype=np.float32)

    def make_vbo(self) -> Vbo:
        np_data = self.as_np_f32_array()

        vbo = Vbo(np_data, np_data.nbytes)

        return vbo

    def count(self) -> int:
        return self.vtx_count
