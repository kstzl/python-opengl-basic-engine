class BaseGeometry:
    def __init__(self) -> None:
        pass

    def get_geometry_name(self) -> str:
        raise Exception("Not implemented")

    def destroy(self):
        raise Exception("Not implemented")

    def render(self):
        raise Exception("Not implemented")
