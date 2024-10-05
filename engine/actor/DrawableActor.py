from engine.actor.BaseActor import BaseActor

from engine.Vao import Vao
from engine.Material import Material


class DrawableActor(BaseActor):
    def __init__(self) -> None:
        super().__init__()

        self.material: Material = None

    def get_vao(self) -> Vao:
        raise Exception("Not implemented")

    def render(self):
        pass
