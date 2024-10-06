from engine.actor.BaseActor import BaseActor

from engine.Material import Material
from engine.BaseGeometry import BaseGeometry


class DrawableActor(BaseActor):
    def __init__(self) -> None:
        super().__init__()

        self.geometry: BaseGeometry = None
        self.material: Material = None
